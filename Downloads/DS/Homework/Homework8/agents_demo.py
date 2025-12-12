import json
import time
import threading
import os
from datetime import datetime
from typing import Dict, Any, List
from kafka import KafkaProducer, KafkaConsumer, KafkaAdminClient
from kafka.admin import NewTopic
from kafka.errors import TopicAlreadyExistsError
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage

# Configuration
KAFKA_BOOTSTRAP_SERVERS = ['localhost:9092']
TOPIC_TASKS = 'agent-tasks'
TOPIC_RESULTS = 'agent-results'
CONSUMER_GROUP = 'worker-agents'

class KafkaSetup:
    """Initialize Kafka topics"""
    
    @staticmethod
    def create_topics():
        admin_client = KafkaAdminClient(
            bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
            client_id='setup'
        )
        
        topics = [
            NewTopic(name=TOPIC_TASKS, num_partitions=3, replication_factor=1),
            NewTopic(name=TOPIC_RESULTS, num_partitions=3, replication_factor=1)
        ]
        
        try:
            admin_client.create_topics(new_topics=topics, validate_only=False)
            print("Topics created successfully")
        except TopicAlreadyExistsError:
            print("✓ Topics already exist")
        finally:
            admin_client.close()


class OrchestratorAgent:
    """Orchestrator that distributes tasks to worker agents via Kafka"""
    
    def __init__(self):
        self.producer = KafkaProducer(
            bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
            value_serializer=lambda v: json.dumps(v).encode('utf-8'),
            key_serializer=lambda k: k.encode('utf-8') if k else None
        )
        
        self.consumer = KafkaConsumer(
            TOPIC_RESULTS,
            bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
            value_deserializer=lambda m: json.loads(m.decode('utf-8')),
            group_id='orchestrator',
            auto_offset_reset='latest',
            enable_auto_commit=True
        )
        
        self.results = {}
        self.running = True
        
    def distribute_tasks(self, tasks: List[Dict[str, Any]]):
        """Send tasks to Kafka topic for workers to process"""
        print("\n=== ORCHESTRATOR: Distributing Tasks ===")
        
        for task in tasks:
            task_id = task['task_id']
            # Use task_id as partition key for ordered processing
            self.producer.send(
                TOPIC_TASKS,
                key=task_id,
                value=task
            )
            print(f"→ Sent task {task_id}: {task['query']}")
        
        self.producer.flush()
        print(f"✓ Distributed {len(tasks)} tasks\n")
    
    def collect_results(self, expected_count: int, timeout: int = 60):
        """Collect results from worker agents"""
        print("=== ORCHESTRATOR: Collecting Results ===")
        start_time = time.time()
        
        while len(self.results) < expected_count:
            if time.time() - start_time > timeout:
                print(f"Timeout after {timeout}s")
                break
                
            message = self.consumer.poll(timeout_ms=1000)
            
            for topic_partition, records in message.items():
                for record in records:
                    result = record.value
                    task_id = result['task_id']
                    self.results[task_id] = result
                    print(f"← Received result for task {task_id}")
        
        print(f"✓ Collected {len(self.results)} results\n")
        return self.results
    
    def display_results(self):
        """Display all collected results"""
        print("\n" + "="*60)
        print("FINAL RESULTS SUMMARY")
        print("="*60)
        
        for task_id in sorted(self.results.keys()):
            result = self.results[task_id]
            print(f"\nTask: {result['query']}")
            print(f"Agent: {result['agent_id']}")
            print(f"Response: {result['response']}...")
            print(f"Time: {result['timestamp']}")
            print("-" * 60)
    
    def shutdown(self):
        self.running = False
        self.producer.close()
        self.consumer.close()


class WorkerAgent:
    """Worker agent that processes tasks using OpenAI"""
    
    def __init__(self, agent_id: str, specialty: str):
        self.agent_id = agent_id
        self.specialty = specialty
        
        # Initialize OpenAI via LangChain
        api_key = os.getenv('OPENAI_API_KEY')
        if not api_key:
            raise ValueError("OPENAI_API_KEY environment variable not set")
        
        self.llm = ChatOpenAI(
            model="gpt-4o-mini",
            temperature=0.7,
            api_key=api_key
        )
        
        self.consumer = KafkaConsumer(
            TOPIC_TASKS,
            bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
            value_deserializer=lambda m: json.loads(m.decode('utf-8')),
            group_id=CONSUMER_GROUP,
            auto_offset_reset='earliest',
            enable_auto_commit=True
        )
        
        self.producer = KafkaProducer(
            bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
            value_serializer=lambda v: json.dumps(v).encode('utf-8')
        )
        
        self.running = True
        print(f"✓ Worker {self.agent_id} ({self.specialty}) initialized")
    
    def process_task(self, task: Dict[str, Any]) -> Dict[str, Any]:
        """Process a task using OpenAI"""
        query = task['query']
        task_id = task['task_id']
        
        print(f"[{self.agent_id}] Processing: {query}")
        
        # Create specialized system prompt
        system_prompt = f"""You are a {self.specialty} specialist agent.
Provide a concise, expert response focusing on your area of expertise.
Keep responses under 150 words."""
        
        try:
            messages = [
                SystemMessage(content=system_prompt),
                HumanMessage(content=query)
            ]
            
            response = self.llm.invoke(messages)
            
            result = {
                'task_id': task_id,
                'query': query,
                'agent_id': self.agent_id,
                'specialty': self.specialty,
                'response': response.content,
                'timestamp': datetime.now().isoformat(),
                'status': 'success'
            }
            
        except Exception as e:
            result = {
                'task_id': task_id,
                'query': query,
                'agent_id': self.agent_id,
                'specialty': self.specialty,
                'response': f"Error: {str(e)}",
                'timestamp': datetime.now().isoformat(),
                'status': 'error'
            }
        
        return result
    
    def start(self):
        """Start consuming and processing tasks"""
        print(f"[{self.agent_id}] Started listening for tasks...")
        
        try:
            for message in self.consumer:
                if not self.running:
                    break
                
                task = message.value
                result = self.process_task(task)
                
                # Send result back to orchestrator
                self.producer.send(TOPIC_RESULTS, value=result)
                self.producer.flush()
                
                print(f"[{self.agent_id}] ✓ Completed task {task['task_id']}")
                
        except Exception as e:
            print(f"[{self.agent_id}] Error: {e}")
        finally:
            self.shutdown()
    
    def shutdown(self):
        self.running = False
        self.consumer.close()
        self.producer.close()
        print(f"[{self.agent_id}] Shutdown complete")


def run_demo():
    """Run the multi-agent orchestration demo"""
    
    print("MULTI-AGENT KAFKA ORCHESTRATION DEMO")
    print("="*60 + "\n")
    
    # Setup Kafka topics
    print("Step 1: Setting up Kafka topics...")
    time.sleep(2)  # Wait for Kafka to be ready
    KafkaSetup.create_topics()
    time.sleep(1)
    
    # Create worker agents with different specialties
    print("\nStep 2: Initializing worker agents...")
    agents = [
        WorkerAgent("agent-1", "Data Science & Machine Learning"),
        WorkerAgent("agent-2", "Software Architecture & Design"),
        WorkerAgent("agent-3", "Cloud Infrastructure & DevOps")
    ]
    
    # Start worker agents in separate threads
    print("\nStep 3: Starting worker agents...")
    agent_threads = []
    for agent in agents:
        thread = threading.Thread(target=agent.start, daemon=True)
        thread.start()
        agent_threads.append(thread)
    
    time.sleep(2)  # Give agents time to start
    
    print("\nStep 4: Creating orchestrator...")
    orchestrator = OrchestratorAgent()
    
    tasks = [
        {
            'task_id': 'task-001',
            'query': 'Explain the benefits of using Apache Kafka for event streaming'
        },
        {
            'task_id': 'task-002',
            'query': 'What are best practices for microservices architecture?'
        },
        {
            'task_id': 'task-003',
            'query': 'How do you implement a machine learning pipeline in production?'
        },
        {
            'task_id': 'task-004',
            'query': 'Describe the advantages of containerization with Docker'
        },
        {
            'task_id': 'task-005',
            'query': 'What are key considerations for distributed system design?'
        },
        {
            'task_id': 'task-006',
            'query': 'Explain feature engineering best practices in ML'
        }
    ]
    
    # Distribute tasks
    print("\nStep 5: Distributing tasks to workers...")
    orchestrator.distribute_tasks(tasks)
    
    # Collect results
    print("Step 6: Waiting for results...")
    results = orchestrator.collect_results(expected_count=len(tasks), timeout=90)
    
    # Display results
    orchestrator.display_results()
    
    # Cleanup
    print("\n\nStep 7: Shutting down...")
    orchestrator.shutdown()
    for agent in agents:
        agent.shutdown()
    
    print("\ncompleted successfully!")


if __name__ == "__main__":
    try:
        run_demo()
    except KeyboardInterrupt:
        print("\n\nDemo interrupted by user")
    except Exception as e:
        print(f"\n\nError running demo: {e}")
        print("\nTroubleshooting:")
        print("1. Ensure Kafka is running: docker ps")
        print("2. Check OPENAI_API_KEY is set")
        print("3. Verify network connectivity to localhost:9092")
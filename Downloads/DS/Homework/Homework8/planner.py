"""
Planner Agent - Part 2 of HW8
Reads questions from 'inbox' topic, creates a plan, and sends to 'tasks' topic
"""

import json
import os
import time
from kafka import KafkaConsumer, KafkaProducer
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage

# Kafka configuration
KAFKA_BOOTSTRAP_SERVERS = ['localhost:9092']
INBOX_TOPIC = 'inbox'
TASKS_TOPIC = 'tasks'

# Initialize OpenAI LLM
api_key = os.getenv('OPENAI_API_KEY')
if not api_key:
    raise ValueError("OPENAI_API_KEY environment variable not set")

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.7,
    api_key=api_key
)

# Kafka consumer for inbox
consumer = KafkaConsumer(
    INBOX_TOPIC,
    bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
    value_deserializer=lambda m: json.loads(m.decode('utf-8')),
    group_id='planner-group',
    auto_offset_reset='earliest',
    enable_auto_commit=True
)

# Kafka producer for tasks
producer = KafkaProducer(
    bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

print("🤖 Planner Agent Started")
print(f"📥 Listening for questions on topic: {INBOX_TOPIC}")
print(f"📤 Sending plans to topic: {TASKS_TOPIC}")
print("=" * 60 + "\n")

def create_plan(question):
    """Create a plan for answering the question"""
    system_prompt = """You are a Planning Agent. Your job is to analyze questions and create a structured plan for answering them.

Create a clear, step-by-step plan that breaks down the question into actionable tasks.
Return your plan as a JSON object with:
- "steps": array of step objects, each with "step_number", "description", and "focus"
- "estimated_complexity": "low", "medium", or "high"

Keep plans concise but comprehensive."""
    
    user_prompt = f"Create a plan for answering this question: {question}"
    
    try:
        messages = [
            SystemMessage(content=system_prompt),
            HumanMessage(content=user_prompt)
        ]
        
        response = llm.invoke(messages)
        
        # Try to parse as JSON, if not, wrap it
        try:
            plan_data = json.loads(response.content)
        except json.JSONDecodeError:
            # If not JSON, create a structured plan from the text
            plan_data = {
                "steps": [
                    {
                        "step_number": 1,
                        "description": "Understand the question context",
                        "focus": "Analyze what is being asked"
                    },
                    {
                        "step_number": 2,
                        "description": "Gather relevant information",
                        "focus": "Identify key concepts and facts"
                    },
                    {
                        "step_number": 3,
                        "description": "Formulate comprehensive answer",
                        "focus": "Provide clear, detailed response"
                    }
                ],
                "estimated_complexity": "medium",
                "raw_plan": response.content
            }
        
        return plan_data
    except Exception as e:
        print(f"❌ Error creating plan: {e}")
        return {
            "steps": [{"step_number": 1, "description": "Answer the question", "focus": "Provide response"}],
            "estimated_complexity": "low",
            "error": str(e)
        }

def process_question(message):
    """Process incoming question and create plan"""
    try:
        payload = message.value
        question_id = payload.get('question_id', 'unknown')
        question = payload.get('question', '')
        timestamp = payload.get('timestamp', '')
        
        print(f"\n{'='*60}")
        print(f"📨 Received Question (ID: {question_id})")
        print(f"   Question: {question}")
        print(f"   Time: {timestamp}")
        print(f"{'='*60}")
        
        # Create plan
        print("🧠 Creating plan...")
        plan = create_plan(question)
        
        # Prepare task message
        task_message = {
            'question_id': question_id,
            'original_question': question,
            'plan': plan,
            'created_by': 'planner',
            'timestamp': time.strftime('%Y-%m-%d %H:%M:%S'),
            'status': 'planned'
        }
        
        # Send to tasks topic
        producer.send(TASKS_TOPIC, value=task_message)
        producer.flush()
        
        print(f"✅ Plan created and sent to '{TASKS_TOPIC}' topic")
        print(f"   Plan complexity: {plan.get('estimated_complexity', 'unknown')}")
        print(f"   Number of steps: {len(plan.get('steps', []))}")
        print(f"{'='*60}\n")
        
    except Exception as e:
        print(f"❌ Error processing question: {e}")
        import traceback
        traceback.print_exc()

# Main loop
try:
    print("🔄 Waiting for questions...\n")
    for message in consumer:
        process_question(message)
        
except KeyboardInterrupt:
    print("\n\n🛑 Planner Agent shutting down...")
    consumer.close()
    producer.close()
    print("✅ Shutdown complete")

"""
Writer Agent - Part 2 of HW8
Reads plans from 'tasks' topic, writes a draft answer, and sends to 'drafts' topic
"""

import json
import os
import time
from kafka import KafkaConsumer, KafkaProducer
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage

# Kafka configuration
KAFKA_BOOTSTRAP_SERVERS = ['localhost:9092']
TASKS_TOPIC = 'tasks'
DRAFTS_TOPIC = 'drafts'

# Initialize OpenAI LLM
api_key = os.getenv('OPENAI_API_KEY')
if not api_key:
    raise ValueError("OPENAI_API_KEY environment variable not set")

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.7,
    api_key=api_key
)

# Kafka consumer for tasks
consumer = KafkaConsumer(
    TASKS_TOPIC,
    bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
    value_deserializer=lambda m: json.loads(m.decode('utf-8')),
    group_id='writer-group',
    auto_offset_reset='earliest',
    enable_auto_commit=True
)

# Kafka producer for drafts
producer = KafkaProducer(
    bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

print("✍️  Writer Agent Started")
print(f"📥 Listening for plans on topic: {TASKS_TOPIC}")
print(f"📤 Sending drafts to topic: {DRAFTS_TOPIC}")
print("=" * 60 + "\n")

def write_answer(question, plan):
    """Write an answer based on the question and plan"""
    system_prompt = """You are a Writing Agent. Your job is to write clear, comprehensive, and well-structured answers to questions.

Follow the provided plan and create a detailed answer that:
- Directly addresses the question
- Is well-organized and easy to read
- Provides sufficient detail and context
- Uses clear language and examples when appropriate

Keep answers concise but thorough (150-300 words)."""
    
    # Format plan steps for context
    plan_text = "Plan:\n"
    if isinstance(plan, dict) and 'steps' in plan:
        for step in plan['steps']:
            if isinstance(step, dict):
                plan_text += f"- Step {step.get('step_number', '?')}: {step.get('description', '')}\n"
            else:
                plan_text += f"- {step}\n"
    else:
        plan_text = f"Plan: {str(plan)}\n"
    
    user_prompt = f"""Question: {question}

{plan_text}

Please write a comprehensive answer following this plan."""
    
    try:
        messages = [
            SystemMessage(content=system_prompt),
            HumanMessage(content=user_prompt)
        ]
        
        response = llm.invoke(messages)
        return response.content
    except Exception as e:
        print(f"❌ Error writing answer: {e}")
        return f"Error writing answer: {str(e)}"

def process_task(message):
    """Process incoming task and write draft answer"""
    try:
        payload = message.value
        question_id = payload.get('question_id', 'unknown')
        question = payload.get('original_question', '')
        plan = payload.get('plan', {})
        timestamp = payload.get('timestamp', '')
        
        print(f"\n{'='*60}")
        print(f"📋 Received Task (ID: {question_id})")
        print(f"   Question: {question}")
        print(f"   Plan complexity: {plan.get('estimated_complexity', 'unknown')}")
        print(f"   Time: {timestamp}")
        print(f"{'='*60}")
        
        # Write answer
        print("✍️  Writing draft answer...")
        draft_answer = write_answer(question, plan)
        
        # Prepare draft message
        draft_message = {
            'question_id': question_id,
            'original_question': question,
            'plan': plan,
            'draft_answer': draft_answer,
            'created_by': 'writer',
            'timestamp': time.strftime('%Y-%m-%d %H:%M:%S'),
            'status': 'draft'
        }
        
        # Send to drafts topic
        producer.send(DRAFTS_TOPIC, value=draft_message)
        producer.flush()
        
        print(f"✅ Draft written and sent to '{DRAFTS_TOPIC}' topic")
        print(f"   Answer length: {len(draft_answer)} characters")
        print(f"   Preview: {draft_answer[:100]}...")
        print(f"{'='*60}\n")
        
    except Exception as e:
        print(f"❌ Error processing task: {e}")
        import traceback
        traceback.print_exc()

# Main loop
try:
    print("🔄 Waiting for tasks...\n")
    for message in consumer:
        process_task(message)
        
except KeyboardInterrupt:
    print("\n\n🛑 Writer Agent shutting down...")
    consumer.close()
    producer.close()
    print("✅ Shutdown complete")

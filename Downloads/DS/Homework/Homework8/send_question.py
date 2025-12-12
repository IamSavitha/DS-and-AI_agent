"""
Send Question Script - Part 2 of HW8
Sends a question to the 'inbox' topic to trigger the 3-agent pipeline
"""

import json
import sys
import time
from kafka import KafkaProducer

# Kafka configuration
KAFKA_BOOTSTRAP_SERVERS = ['localhost:9092']
INBOX_TOPIC = 'inbox'

# Kafka producer
producer = KafkaProducer(
    bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

def send_question(question):
    """Send a question to the inbox topic"""
    question_id = f"q_{int(time.time())}"
    
    message = {
        'question_id': question_id,
        'question': question,
        'timestamp': time.strftime('%Y-%m-%d %H:%M:%S'),
        'source': 'user'
    }
    
    print(f"📤 Sending question to '{INBOX_TOPIC}' topic...")
    print(f"   Question ID: {question_id}")
    print(f"   Question: {question}")
    print("=" * 60)
    
    try:
        producer.send(INBOX_TOPIC, value=message)
        producer.flush()
        print("✅ Question sent successfully!")
        print(f"\n💡 The question will be processed by:")
        print("   1. Planner Agent → creates plan → 'tasks' topic")
        print("   2. Writer Agent → writes draft → 'drafts' topic")
        print("   3. Reviewer Agent → reviews and approves → 'final' topic")
        print(f"\n📋 Check the 'final' topic for the approved answer with question_id: {question_id}")
        print("=" * 60 + "\n")
        
    except Exception as e:
        print(f"❌ Error sending question: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    # Get question from command line or use default
    if len(sys.argv) > 1:
        question = " ".join(sys.argv[1:])
    else:
        # Default question
        question = "What are the key benefits of using Apache Kafka for distributed systems?"
        print("ℹ️  No question provided, using default question")
        print("   Usage: python send_question.py 'Your question here'\n")
    
    send_question(question)
    
    # Close producer
    producer.close()

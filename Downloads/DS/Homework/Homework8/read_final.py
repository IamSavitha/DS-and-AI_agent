"""
Read Final Topic - Part 2 of HW8
Reads and displays approved answers from the 'final' topic
"""

import json
from kafka import KafkaConsumer

KAFKA_BOOTSTRAP_SERVERS = ['localhost:9092']
FINAL_TOPIC = 'final'

print("📖 Reading from 'final' topic...")
print("=" * 60 + "\n")

consumer = KafkaConsumer(
    FINAL_TOPIC,
    bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
    value_deserializer=lambda m: json.loads(m.decode('utf-8')),
    group_id='final-reader',
    auto_offset_reset='earliest',
    enable_auto_commit=True
)

print("🔄 Waiting for messages... (Press Ctrl+C to stop)\n")

try:
    for message in consumer:
        data = message.value
        
        print("=" * 60)
        print(f"📋 Question ID: {data.get('question_id', 'unknown')}")
        print(f"❓ Question: {data.get('original_question', 'N/A')}")
        print(f"✅ Status: {data.get('status', 'unknown')}")
        print(f"⭐ Quality Score: {data.get('quality_score', 0)}/10")
        print(f"📝 Answer:")
        print("-" * 60)
        print(data.get('answer', 'N/A'))
        print("-" * 60)
        
        if 'review' in data:
            review = data['review']
            if isinstance(review, dict):
                print(f"💬 Review Feedback: {review.get('feedback', 'N/A')}")
        
        print(f"⏰ Approved At: {data.get('approved_at', 'N/A')}")
        print("=" * 60 + "\n")
        
except KeyboardInterrupt:
    print("\n\n🛑 Stopping reader...")
    consumer.close()
    print("✅ Shutdown complete")

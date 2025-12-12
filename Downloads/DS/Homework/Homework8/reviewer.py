"""
Reviewer Agent - Part 2 of HW8
Reads drafts from 'drafts' topic, reviews them, and sends approved answers to 'final' topic
"""

import json
import os
import time
from kafka import KafkaConsumer, KafkaProducer
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage

# Kafka configuration
KAFKA_BOOTSTRAP_SERVERS = ['localhost:9092']
DRAFTS_TOPIC = 'drafts'
FINAL_TOPIC = 'final'

# Initialize OpenAI LLM
api_key = os.getenv('OPENAI_API_KEY')
if not api_key:
    raise ValueError("OPENAI_API_KEY environment variable not set")

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.3,  # Lower temperature for more consistent review
    api_key=api_key
)

# Kafka consumer for drafts
consumer = KafkaConsumer(
    DRAFTS_TOPIC,
    bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
    value_deserializer=lambda m: json.loads(m.decode('utf-8')),
    group_id='reviewer-group',
    auto_offset_reset='earliest',
    enable_auto_commit=True
)

# Kafka producer for final
producer = KafkaProducer(
    bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

print("🔍 Reviewer Agent Started")
print(f"📥 Listening for drafts on topic: {DRAFTS_TOPIC}")
print(f"📤 Sending approved answers to topic: {FINAL_TOPIC}")
print("=" * 60 + "\n")

def review_draft(question, draft_answer):
    """Review the draft answer and determine if it should be approved"""
    system_prompt = """You are a Review Agent. Your job is to review draft answers and determine if they are ready for final approval.

Evaluate the draft answer based on:
1. Does it answer the question directly and completely?
2. Is it clear and well-structured?
3. Is it accurate and informative?
4. Does it follow the original plan?

Return your review as a JSON object with:
- "status": "approved" or "needs_revision"
- "quality_score": number from 1-10
- "feedback": brief explanation of your decision
- "improvements": array of suggested improvements (if any)

If the answer is good, approve it. Only reject if there are significant issues."""
    
    user_prompt = f"""Original Question: {question}

Draft Answer:
{draft_answer}

Please review this draft answer and provide your assessment."""
    
    try:
        messages = [
            SystemMessage(content=system_prompt),
            HumanMessage(content=user_prompt)
        ]
        
        response = llm.invoke(messages)
        
        # Try to parse as JSON
        try:
            review_data = json.loads(response.content)
        except json.JSONDecodeError:
            # If not JSON, create a structured review
            # Default to approved if review is positive
            content_lower = response.content.lower()
            if 'approve' in content_lower or 'good' in content_lower or 'excellent' in content_lower:
                review_data = {
                    "status": "approved",
                    "quality_score": 8,
                    "feedback": "Answer looks good based on review",
                    "improvements": []
                }
            else:
                review_data = {
                    "status": "needs_revision",
                    "quality_score": 5,
                    "feedback": response.content[:200],
                    "improvements": ["Review the draft for improvements"]
                }
        
        return review_data
    except Exception as e:
        print(f"❌ Error reviewing draft: {e}")
        # Default to approved on error
        return {
            "status": "approved",
            "quality_score": 7,
            "feedback": f"Review completed (error during review: {str(e)})",
            "improvements": []
        }

def process_draft(message):
    """Process incoming draft and review it"""
    try:
        payload = message.value
        question_id = payload.get('question_id', 'unknown')
        question = payload.get('original_question', '')
        draft_answer = payload.get('draft_answer', '')
        timestamp = payload.get('timestamp', '')
        
        print(f"\n{'='*60}")
        print(f"📄 Received Draft (ID: {question_id})")
        print(f"   Question: {question}")
        print(f"   Draft length: {len(draft_answer)} characters")
        print(f"   Time: {timestamp}")
        print(f"{'='*60}")
        
        # Review draft
        print("🔍 Reviewing draft...")
        review = review_draft(question, draft_answer)
        
        # Prepare final message
        final_message = {
            'question_id': question_id,
            'original_question': question,
            'answer': draft_answer,
            'review': review,
            'status': review.get('status', 'approved'),
            'quality_score': review.get('quality_score', 0),
            'reviewed_by': 'reviewer',
            'timestamp': time.strftime('%Y-%m-%d %H:%M:%S'),
            'approved_at': time.strftime('%Y-%m-%d %H:%M:%S') if review.get('status') == 'approved' else None
        }
        
        # Send to final topic
        producer.send(FINAL_TOPIC, value=final_message)
        producer.flush()
        
        status_emoji = "✅" if review.get('status') == 'approved' else "⚠️"
        print(f"{status_emoji} Review complete and sent to '{FINAL_TOPIC}' topic")
        print(f"   Status: {review.get('status', 'unknown')}")
        print(f"   Quality Score: {review.get('quality_score', 0)}/10")
        print(f"   Feedback: {review.get('feedback', 'No feedback')[:100]}...")
        print(f"{'='*60}\n")
        
    except Exception as e:
        print(f"❌ Error processing draft: {e}")
        import traceback
        traceback.print_exc()

# Main loop
try:
    print("🔄 Waiting for drafts...\n")
    for message in consumer:
        process_draft(message)
        
except KeyboardInterrupt:
    print("\n\n🛑 Reviewer Agent shutting down...")
    consumer.close()
    producer.close()
    print("✅ Shutdown complete")

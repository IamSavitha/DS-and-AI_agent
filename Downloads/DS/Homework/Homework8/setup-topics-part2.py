"""
Setup Script for Part 2 - Creates Kafka topics for multi-agent system
"""

from kafka import KafkaAdminClient
from kafka.admin import NewTopic
from kafka.errors import TopicAlreadyExistsError

KAFKA_BOOTSTRAP_SERVERS = ['localhost:9092']

topics = [
    'inbox',
    'tasks',
    'drafts',
    'final'
]

def create_topics():
    """Create all required topics for Part 2"""
    admin_client = KafkaAdminClient(
        bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
        client_id='setup-part2'
    )
    
    topic_list = [
        NewTopic(name=topic, num_partitions=1, replication_factor=1)
        for topic in topics
    ]
    
    try:
        admin_client.create_topics(new_topics=topic_list, validate_only=False)
        print("✅ Topics created successfully:")
        for topic in topics:
            print(f"   - {topic}")
    except TopicAlreadyExistsError:
        print("ℹ️  Topics already exist:")
        for topic in topics:
            print(f"   - {topic}")
    except Exception as e:
        print(f"❌ Error creating topics: {e}")
    finally:
        admin_client.close()

if __name__ == "__main__":
    print("🔧 Setting up Kafka topics for Part 2 (Multi-Agent System)...\n")
    create_topics()
    print("\n✅ Setup complete!")

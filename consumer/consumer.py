import os
import pika
import json
from pymongo import MongoClient
from statistics import mean

# Connection to RabbitMQ
rabbitmq_host = os.getenv("RABBITMQ_HOST")
rabbitmq_port = int(os.getenv("RABBITMQ_PORT", 5672))
rabbitmq_user = os.getenv("RABBITMQ_USER")
rabbitmq_pass = os.getenv("RABBITMQ_PASS")
queue_name = os.getenv("RABBITMQ_QUEUE")

# Connection to MongoDB
mongodb_uri = os.getenv("MONGODB_URI")
mongodb_db = os.getenv("MONGODB_DB", "stockmarket")
mongodb_collection_name = os.getenv("MONGODB_COLLECTION", "stocks")

# Buffer for messages
buffer = []  # Global buffer to store messages temporarily

def connect_to_rabbitmq():
    credentials = pika.PlainCredentials(rabbitmq_user, rabbitmq_pass)
    parameters = pika.ConnectionParameters(
        host=rabbitmq_host,
        port=rabbitmq_port,
        credentials=credentials
    )
    return pika.BlockingConnection(parameters)

def connect_to_mongodb():
    client = MongoClient(mongodb_uri)
    return client[mongodb_db][mongodb_collection_name]

def main():
    global buffer  # Declare buffer as global

    try:
        rabbitmq_connection = None
        # Establish connection
        rabbitmq_connection = connect_to_rabbitmq()
        mongodb_collection = connect_to_mongodb()
        channel = rabbitmq_connection.channel()

        # Declare queue
        channel.queue_declare(queue=queue_name, durable=False)

        def callback(ch, method, properties, body):
            global buffer  # Access global buffer
            try:
                # Parse message
                message = json.loads(body)

                # Add message to buffer
                buffer.append(message)

                # If 1000 messages collected
                if len(buffer) >= 1000:
                    prices = [msg["price"] for msg in buffer]
                    avg_price = sum(prices) / len(prices)
                    company = buffer[0]["company"]

                    # Save result in MongoDB
                    result = {
                        "company": company,
                        "avgPrice": avg_price
                    }
                    mongodb_collection.insert_one(result)
                    print(f"Saved: {result}")

                    # Clear buffer
                    buffer = []

                # Acknowledge message
                ch.basic_ack(delivery_tag=method.delivery_tag)

            except json.JSONDecodeError as e:
                print(f"Error parsing message: {e}")

        # Consume messages
        channel.basic_qos(prefetch_count=1)
        channel.basic_consume(queue=queue_name, on_message_callback=callback)
        print(f"Consumer listens to queue: {queue_name}")
        channel.start_consuming()

    except Exception as e:
        print(f"Error: {e}")
    finally:
        if rabbitmq_connection:
            rabbitmq_connection.close()

if __name__ == "__main__":
    main()

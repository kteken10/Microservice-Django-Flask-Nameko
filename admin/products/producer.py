import pika, json

params = pika.URLParameters('amqps://slgeuguf:cP46sDBe2XwOfwYufaBkV4YugaEmC-Q1@toad.rmq.cloudamqp.com/slgeuguf')

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='main', body=json.dumps(body), properties=properties)
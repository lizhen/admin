import pika, json


params = pika.URLParameters('amqps://zygrvmge:QKKPsifSOzIhs5-hsY0nHC1rK_mA4WZ6@elk.rmq2.cloudamqp.com/zygrvmge')

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='main', body=json.dumps(body), properties=properties)
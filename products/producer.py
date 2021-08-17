import pika


params = pika.URLParameters('amqps://zygrvmge:QKKPsifSOzIhs5-hsY0nHC1rK_mA4WZ6@elk.rmq2.cloudamqp.com/zygrvmge')

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish():
    channel.basic_publish(exchange='', routing_key='main', body='hello main')
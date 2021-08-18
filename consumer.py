import pika, json


params = pika.URLParameters('amqps://zygrvmge:QKKPsifSOzIhs5-hsY0nHC1rK_mA4WZ6@elk.rmq2.cloudamqp.com/zygrvmge')

connection = pika.BlockingConnection(params)

channel = connection.channel()


channel.queue_declare(queue='admin')


def callback(ch, method, properties, body):
    print('Received in admin')
    data = json.loads(body)
    print(data)
    product = Product.objects.get(id=id)
    product.likes = product.likes + 1
    product.save()
    print('Product likes increased!')
    

channel.basic_consume(queue='admin', on_message_callback=callback, auto_ack=True)

print('Started Consuming')

channel.start_consuming()

channel.close()
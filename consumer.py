import pika, json, os, django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "main.settings")
django.setup()

# Create your views here.
from products.models import Product, ProductUser

params = pika.URLParameters('amqps://gnibdxxp:4SkiD512SI28LgMrfIP-AobgSRNBaNGv@jackal.rmq.cloudamqp.com/gnibdxxp')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='main')

def callback(ch, method, properties, body):
    print('Received in main')
    # print(body)
    data = json.loads(body)
    print(data)

    if properties.content_type == 'product_created':
        product = Product(id = data['id'], title = data['title'], image=data['image'])
        product.save()
        print('Product Created!')

    elif properties.content_type == 'product_updated':
        product = Product.objects.filter(id = data['id']).all()
        product.title = data['title']
        product.image = data['image']
        product.save()
        print('Product Updated!')

    elif properties.content_type == 'product_deleted':
        product = Product.objects.filter(id = data['id']).all()
        product.delete()
        print('Product deleted!')

channel.basic_consume(queue='main', on_message_callback=callback, auto_ack=True)

print('Started Consuming')

channel.start_consuming()

channel.close()
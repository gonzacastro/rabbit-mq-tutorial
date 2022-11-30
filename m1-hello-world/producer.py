import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Se crea la cola con nombre hello, si ya existe no hace nada
channel.queue_declare(queue='hello')

# En este modulo no se aborda el tema de Exchanges (modulo 3).
# Por lo tanto, se va a utilizar el valor por defecto ''.
# Con routing_key se especifica el nombre de la queue.
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World!')
print(" [x] Sent 'Hello World!'")

connection.close()
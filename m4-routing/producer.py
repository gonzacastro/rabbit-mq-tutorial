import pika
import sys

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

# Se crea un exchange de tipo direct, que lo que hace es enviar los mensajes
# a todas las queues que tengan el mismo routing_key que el mensaje.
channel.exchange_declare(exchange='direct_logs', exchange_type='direct')

severity = sys.argv[1] if len(sys.argv) > 1 else 'info'
message = ' '.join(sys.argv[2:]) or 'Hello World!'

channel.basic_publish(
    exchange='direct_logs', routing_key=severity, body=message)

print(" [x] Sent %r:%r" % (severity, message))
connection.close()
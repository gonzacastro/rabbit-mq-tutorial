import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

# Se crea el exchange del tipo fanout.
# Un exchange es una entidad que recibe mensajes de producers y los
# redirige a la/s queues correspondientes. Este comportamiento se define
# con los exchange types (en este caso fanout hace un broadcast a todas
# las queues que escuchen en ese exchange).
# En los modulos anteriores se usaba el exchange por default, que manda
# los mensajes solamente a la queue que se le indica.
channel.exchange_declare(exchange='logs', exchange_type='fanout')

# Se crea una queue sin nombre, ya que no hace falta definir el destinatario.
# El parametro exclusive borra la queue una vez que se cierra la conexion.
result = channel.queue_declare(queue='', exclusive=True)
queue_name = result.method.queue

# Se suscribe a la queue al exchange de logs.
channel.queue_bind(exchange='logs', queue=queue_name)

print(' [*] Waiting for logs. To exit press CTRL+C')

def callback(ch, method, properties, body):
    print(" [x] %r" % body)

channel.basic_consume(
    queue=queue_name, on_message_callback=callback, auto_ack=True)

channel.start_consuming()
import pika
import sys

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

message = ' '.join(sys.argv[1:]) or "info: Hello World!"

# No se establece una routing_key ya que al ser una difusion no hace falta.
# Los mensajes se descartas siempre, haya o no alguien escuchando.
channel.basic_publish(exchange='logs', routing_key='', body=message)

print(" [x] Sent %r" % message)
connection.close()
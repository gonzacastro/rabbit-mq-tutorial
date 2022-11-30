import pika
import time

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

# Se setea el flag durable en True para denotar que si se cae
# la instancia de RabbitMQ®, no se va a perder ningun mensaje.
channel.queue_declare(queue='task_queue', durable=True)

print(' [*] Waiting for messages. To exit press CTRL+C')


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body.decode())
    time.sleep(body.count(b'.'))
    print(" [x] Done")
    
    # Se establece el mecanismo de ack.
    ch.basic_ack(delivery_tag=method.delivery_tag)

# Se desactiva Round-robin y se establece que un worker va a
# tomar una task ni bien este libre, o sea, tampoco se le va
# a asignar un mensaje estando ocupado.
# Round-robin consiste en distribuir los mensajes equitativamente
# siguiendo un patron, sin importar si el worker puede o no atenderlo
# instantaneamente. Es decir, si tenemos dos workers, a uno le van
# a llegar los mensajes pares y a otro los impares.
channel.basic_qos(prefetch_count=1)

# Notese que ya no esta el flag de auto_ack.
channel.basic_consume(queue='task_queue', on_message_callback=callback)

channel.start_consuming()
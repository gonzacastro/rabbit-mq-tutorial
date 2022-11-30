import pika, sys, os

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    
    # Se crea la cola con nombre hello, si ya existe no hace nada
    channel.queue_declare(queue='hello')

    # Se define la funcion callback que va a atender el mensaje.
    def callback(ch, method, properties, body):
        print(" [x] Received %r" % body)

    # Se establece la conexion del callback con los mensajes que lleguen de la cola hello.
    # Auto_ack=True desactiva el aviso que se manda al terminar una task.
    # Si no se recibe dicho aviso dentro de un timeout definido (30' por defecto), se
    # vuelve a mandar el mensaje.
    channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    
    # Se pone a consumir.
    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
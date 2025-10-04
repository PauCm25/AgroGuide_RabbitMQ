import pika

def conectar_rabbitmq():
    """Establece conexión con RabbitMQ en localhost."""
    conexion = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    canal = conexion.channel()
    return canal


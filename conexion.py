import pika

def conectar_rabbitmq():
    """Establece conexión con RabbitMQ en localhost."""

    """Credenciales del RabbitMQ"""
    credentials = pika.PlainCredentials('paula', '123456')

    conexion = pika.BlockingConnection(
        pika.ConnectionParameters(host="localhost",credentials=credentials)
        )
    
    canal = conexion.channel()
    return canal


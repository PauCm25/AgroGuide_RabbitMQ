import pika

#función de conexión con RabbitMQ por medio de la URL http://localhost:15672
def conectar_rabbitmq():
    
    conexion = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

    canal = conexion.channel() #Se abre un canal dentro de la conexión con Rabitt
    return canal #se devuelve el canal para posteriormente poder ser usado en las otras partes

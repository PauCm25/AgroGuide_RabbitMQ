from conexion import conectar_rabbitmq


"""
def publicar_evento(mensaje)
Función encargada de publicar un evento en la cola "recordatorios" en Rabbit
"""
def publicar_evento(mensaje):
    canal = conectar_rabbitmq()
    canal.queue_declare(queue='recordatorios') #Si no existe la cola, la crea
    canal.basic_publish(exchange='',
                        routing_key='recordatorios',
                        body=mensaje)
    print(f"[Agroguide Productor] Recordatorio publicado: {mensaje}")

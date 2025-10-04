from conexion import conectar_rabbitmq


"""
def iniciar_procesador()
Función encargada de escuchar la cola "recordatorios" (creada y modificada en 
el .py "productor")
cuando encuentra un mensaje en la cola, lo procesa con la funcion
"procesar_recordatorio")
"""
def iniciar_procesador():
    """Escucha recordatorios en la cola 'recordatorios'."""
    canal = conectar_rabbitmq()
    canal.queue_declare(queue='recordatorios') #crea la cola si no existe
    canal.basic_consume(queue='recordatorios',
                        on_message_callback=procesar_recordatorio,
                        auto_ack=True)
    print("[Procesador] Esperando recordatorios...")
    canal.start_consuming()


"""
def procesar_recordatorio(ch, method, properties, body)
Función encargada procesar el recordatorio recibido y, por consiguiente,
lo convierte en una notificación que va para el usuario.
Cabe aclarar que la notificación se publica si el usuario está conectado,
sino, se mantendrá en la cola de resultados hasta que se ejecute.
"""
def procesar_recordatorio(ch, method, properties, body):
    recordatorio = body.decode()
    print(f"[Procesador Agroguide] Recordatorio recibido: {recordatorio}")

    notificacion = f"Notificador Agroguide: {recordatorio}"
    canal = conectar_rabbitmq()
    canal.queue_declare(queue='resultados')#crea la cola si no existe
    canal.basic_publish(exchange='',
                        routing_key='resultados',
                        body=notificacion)
    print(f"[Procesador Agroguide] Notificación enviada: {notificacion}")

#Ejecución
if __name__ == "__main__":
    iniciar_procesador()

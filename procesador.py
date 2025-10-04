from conexion import conectar_rabbitmq


def iniciar_procesador():
    """Escucha recordatorios en la cola 'recordatorios'."""
    canal = conectar_rabbitmq()
    canal.queue_declare(queue='recordatorios')
    canal.basic_consume(queue='recordatorios',
                        on_message_callback=procesar_recordatorio,
                        auto_ack=True)
    print("[Procesador] Esperando recordatorios...")
    canal.start_consuming()


def procesar_recordatorio(ch, method, properties, body):
    """Procesa el recordatorio y lo convierte en una notificación para el usuario"""
    recordatorio = body.decode()
    print(f"[Procesador Agroguide] Recordatorio recibido: {recordatorio}")

    notificacion = f"Notificador Agroguide: {recordatorio}"
    canal = conectar_rabbitmq()
    canal.queue_declare(queue='resultados')
    canal.basic_publish(exchange='',
                        routing_key='resultados',
                        body=notificacion)
    print(f"[Procesador Agroguide] Notificación enviada: {notificacion}")



if __name__ == "__main__":
    iniciar_procesador()

from conexion import conectar_rabbitmq

def mostrar_noti(ch, method, properties, body):
    """Recibe la notificación procesada previamente y la muestra al usuario final."""
    notificacion = body.decode()
    print(f"[Web AgroGuide] {notificacion}")

def iniciar_consumidor():
    """Escucha notificaciones en la cola 'resultados'."""
    canal = conectar_rabbitmq()
    canal.queue_declare(queue='resultados')
    canal.basic_consume(queue='resultados',
                        on_message_callback=mostrar_noti,
                        auto_ack=True)
    print("[Web AgroGuide] Esperando notificaciones...")
    canal.start_consuming()


if __name__ == "__main__":
    iniciar_consumidor()


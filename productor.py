from conexion import conectar_rabbitmq

def publicar_evento():
    """Publica un evento en la cola 'recordatorios'."""
    canal = conectar_rabbitmq()
    canal.queue_declare(queue='recordatorios')  # Crea la cola si no existe

    mensaje = "Aplicar fertilizante en el cultivo de fresa"
    canal.basic_publish(exchange='',
                        routing_key='recordatorios',
                        body=mensaje)
    print(f"[Agroguide Productor] Recordatorio publicado: {mensaje}")


if __name__ == "__main__":
    publicar_evento()

import tkinter as tk
from tkinter import ttk
from conexion import conectar_rabbitmq
from productor import publicar_evento
import threading

CULTIVOS = ["Fresa", "Papa", "Cebolla", "Cacao"]

def publicar_desde_gui(cultivo):
    mensaje = f"Aplicar fertilizante en el cultivo de {cultivo.lower()}"
    publicar_evento(mensaje)

def escuchar_resultados(caja_texto):
    def mostrar_noti(ch, method, properties, body):
        notificacion = body.decode()
        caja_texto.insert(tk.END, f"[Web AgroGuide] {notificacion}\n")
        caja_texto.see(tk.END)

    canal = conectar_rabbitmq()
    canal.queue_declare(queue='resultados')
    canal.basic_consume(queue='resultados',
                        on_message_callback=mostrar_noti,
                        auto_ack=True)
    print("[Web AgroGuide] Esperando notificaciones...")
    canal.start_consuming()

def iniciar_gui():
    ventana = tk.Tk()
    ventana.title("AgroGuide Notificador")
    ventana.geometry("500x400")
    ventana.configure(bg="#f0f8f5")

    etiqueta = tk.Label(ventana, text="Selecciona el cultivo:", font=("Arial", 12), bg="#f0f8f5")
    etiqueta.pack(pady=10)

    cultivo_var = tk.StringVar()
    selector = ttk.Combobox(ventana, textvariable=cultivo_var, values=CULTIVOS, state="readonly", font=("Arial", 11))
    selector.pack(pady=5)
    selector.current(0)

    boton_publicar = tk.Button(ventana, text="📤 Publicar Recordatorio", font=("Arial", 11), bg="#d0f0c0",
                               command=lambda: publicar_desde_gui(cultivo_var.get()))
    boton_publicar.pack(pady=10)

    etiqueta_noti = tk.Label(ventana, text="📥 Notificaciones recibidas:", font=("Arial", 12), bg="#f0f8f5")
    etiqueta_noti.pack(pady=10)

    caja_texto = tk.Text(ventana, height=10, width=60, font=("Arial", 10))
    caja_texto.pack(pady=5)

    hilo_consumidor = threading.Thread(target=escuchar_resultados, args=(caja_texto,), daemon=True)
    hilo_consumidor.start()

    ventana.mainloop()

if __name__ == "__main__":
    iniciar_gui()

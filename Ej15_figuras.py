#cbtis89
#carreon tellez melany
#3b de programacion

import tkinter as tk

ventana = tk.Tk()
ventana.title("Nombre y Apellido")
ventana.geometry("300x200")

etiqueta = tk.Label(ventana, text="Nombre y Apellido:", font=("Arial", 12))
etiqueta.pack(pady=10)

entrada = tk.Entry(ventana, font=("Arial", 12))
entrada.pack(pady=5)
def mostrar_texto():
    texto = entrada.get()
    etiqueta_resultado.config(text=(texto))
    entrada2 = tk.Entry(ventana, font=("Arial", 12))
    entrada2.pack(pady=5)
boton = tk.Button(ventana, text="Mostrar texto", command=mostrar_texto)
boton.pack(pady=10)

etiqueta_resultado = tk.Label(ventana, text="", font=("Arial", 12), fg="blue")
etiqueta_resultado.pack(pady=5)

# Iniciar el loop principal
ventana.mainloop()
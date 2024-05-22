import tkinter as tk
from tkinter import font

def guardar_texto():
    texto = entrada.get()
    print(f'Texto guardado: {texto}')
    ventana1 = tk.Tk()
    ventana1.title("Ventana 2")
    ventana1.geometry("300x200")
    # Aquí puedes hacer lo que necesites con la variable 'texto'
    fuente = font.Font(size=16)
    etiqueta = tk.Label(ventana1, text=texto, font=fuente)
    etiqueta.pack()

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Ventana de entrada de texto")
ventana.geometry("300x200")

# Crear un campo de entrada (Entry)
entrada = tk.Entry(ventana, width=30)
entrada.pack(pady=20)

# Crear un botón que llame a la función guardar_texto cuando se presiona
boton_guardar = tk.Button(ventana, text="Guardar", command=guardar_texto)
boton_guardar.pack(pady=10)

# Ejecutar el bucle principal
ventana.mainloop()

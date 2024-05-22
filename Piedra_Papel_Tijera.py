import random
import tkinter as tk
from tkinter import font #Modifica las fuentes
from tkinter import messagebox #Crea una ventana para mostrar resultado

#Creación de la ventana principal
ventanaPrincipal =tk.Tk()
ventanaPrincipal.title('Ventana Principal')
ventanaPrincipal.geometry("350x150+500+200")

texto = "¡Bienvenid@ a este divertido juego!\n¿Te animas a jugar?"
textoV ="Elige una de las opciones"
fuenteTama = 16
fuente = font.Font(size=fuenteTama)

etiqueta = tk.Label(ventanaPrincipal, text=texto, font=fuente)
etiqueta.pack()

#Variables globales para contabilizar los resultados.
jugador = 0
compu = 0
empates = 0

#Creación de funciones
def inicio():

    ventanaPrincipal.withdraw()
    ventanaJuego = tk.Toplevel(ventanaPrincipal)
    ventanaJuego.geometry("350x150+500+200")
    ventanaJuego.title('¿Piedra, papel o tijera?')
    ventanaJuego.configure(bg="#288BA8")
    ventanaJuego.deiconify()


    botonPiedra = tk.Button(ventanaJuego, text='Piedra', width=10, height=2, bg="yellow", fg="black", command=lambda: jugar('Piedra'))
    botonPapel = tk.Button(ventanaJuego, text='Papel', width=10, height=2, bg="white", fg="black",command=lambda: jugar('Papel'))
    botonTijera = tk.Button(ventanaJuego, text='Tijera', width=10, height=2, bg="blue", fg="white",command=lambda: jugar('Tijera'))
    botonSalir = tk.Button(ventanaJuego, text='Salir', width=5, height=2, bg="red", fg="white", command=salir)
    botonPiedra.pack(side="left", padx=10)
    botonPapel.pack(side="left", padx=10)
    botonTijera.pack(side="left", padx=10)
    botonSalir.pack(side= "right", padx=10)

def jugar(opcion):

    resultado = ""
    usuario = opcion
    computadora = random.choice(['Piedra', 'Papel', 'Tijera'])

    print(f"Elegiste '{usuario}' y la computadora eligió '{computadora}'")

    if usuario == computadora:
        resultado = '¡Empate!'
        global empates
        empates += 1

    elif ganó_el_jugador (usuario, computadora):
        resultado = '¡Ganaste!'
        global jugador #Es necesario aclarar hacer referencia a la variable global para poder modificarla.
        jugador += 1

    else:
        resultado = '¡Perdiste!'
        global compu
        compu += 1
    
    #Ventana emergente que muestra el resultado.    
    messagebox.showinfo("Resultado",f"Tu opción fue {opcion}\nLa computadora eligió {computadora}\n{resultado}")

def ganó_el_jugador (jugador, oponente):

    if ((jugador == "Piedra" and oponente == "Tijera") or 
        (jugador == "Tijera" and oponente == "Papel") or 
        (jugador == "Papel" and oponente == "Piedra")):
        return True

    else:
        return False

def salirBye():
    messagebox.showinfo("Despedida", "¡Hasta la próxima!")
    exit()

def salir():
    messagebox.showinfo("Resultado Final", f"La puntuación final es de:\nTú: {jugador}\nComputadora: {compu}\nEmpates: {empates}")
    salirBye()

boton1 = tk.Button(ventanaPrincipal, text="SÍ", width=10, height=2, bg="green", fg="white",command=inicio)
boton2 = tk.Button(ventanaPrincipal, text="NO", width=10, height=2, bg="red", fg="white", command=salirBye)
boton1.pack(side="left", padx=60)
boton2.pack(side="left")

ventanaPrincipal.mainloop()
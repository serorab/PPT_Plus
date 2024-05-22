import pickle
import random
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

puntaje = 0
#Función que detecta si el nombre ya se encuentra dentro de la lista
def busqueda(nombre):
    with open('jugadores.bin', 'rb+') as archivo:
            archivoAbierto = pickle.load(archivo)
    
            for i in archivoAbierto:
                for e in i:
                    if nombre.lower() == e.lower():
                        return True

#Acción del botón cuando se va a iniciar el juego
def guardar():
    nombre = entrada.get().lower()
    if nombre == '':
        mensajeError = tk.Label(ventana, text='Ingrese un nombre por favor', font=12)
        mensajeError.pack()
    else:    
        try:
            with open('jugadores.bin', 'rb+') as archivo:
                archivoAbierto = pickle.load(archivo)
                diccionario = {}
            
                if busqueda(nombre):

                    alerta = tk.Label(ventana, text=f'¡{nombre.capitalize()} ya participó!\nsi continúa se borrará la anterior puntuación', font=8)
                    alerta.pack()

                    pregunta = messagebox.askyesno("¡Advertencia!", "¿Desea continuar?")
                    entrada.delete(0, tk.END)
                    alerta.destroy()

                    if pregunta:
                        pickle.dump(archivoAbierto, archivo)
                
                else:
                    diccionario[nombre]= puntaje
                    archivoAbierto.append(diccionario)

                archivo.seek(0, 2)
                archivo.seek(0)
                pickle.dump(archivoAbierto, archivo)
            juego(nombre)

        except FileNotFoundError:        
            with open('jugadores.bin', 'wb') as archivo:
                if nombre == '':
                    nombre = 'Humano'
                JugadorNuevo = {nombre:puntaje}
                jugadores = []
                jugadores.append(JugadorNuevo)
                archivo.seek(0)
                pickle.dump(jugadores, archivo)  
            juego(nombre)

#Variables globales para contabilizar los resultados.
jugador = 0
compu = 0
empates = 0

#Código del juego --> Ventana 
def juego(usuario):
    def on_closing():
        if messagebox.askokcancel('Salir', '¿Está seguro que desea salir?'):
            ventanaJuego.destroy()
            ventana.deiconify()
    ventana.withdraw()
    ventanaJuego = tk.Tk()
    ventanaJuego.title('¡A Jugar!')
    ventanaJuego.geometry(f'400x200+{x}+{y}')
    ventanaJuego.configure(bg="#288BA8")

    ventanaJuego.protocol("WM_DELETE_WINDOW", on_closing)
    
    botonPiedra = tk.Button(ventanaJuego, text='Piedra', width=10, height=2, bg="yellow", fg="black", command=lambda: jugar('Piedra'))
    botonPapel = tk.Button(ventanaJuego, text='Papel', width=10, height=2, bg="white", fg="black",command=lambda: jugar('Papel'))
    botonTijera = tk.Button(ventanaJuego, text='Tijera', width=10, height=2, bg="blue", fg="white",command=lambda: jugar('Tijera'))
    botonSalir = tk.Button(ventanaJuego, text='Salir', width=5, height=2, bg="red", fg="white", command=lambda: salir(usuario))
    botonPiedra.pack(side="left", padx=10)
    botonPapel.pack(side="left", padx=10)
    botonTijera.pack(side="left", padx=10)
    botonSalir.pack(side= "right", padx=10)
    
    ventanaJuego.mainloop()    
    ventana.deiconify()

#Código del juego --> Juego
def jugar(opcion):
    
    resultado = ""
    elemento = opcion
    computadora = random.choice(['Piedra', 'Papel', 'Tijera'])

    if elemento == computadora:
        resultado = '¡Empate!'
        global empates
        empates += 1

    elif ganó_el_jugador (elemento, computadora):
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

def terminar():
    exit()

def salirBye():
    def on_closing():
        if messagebox.askokcancel('salir', '¿Está seguro que desea salir?'):
            ventanaResultados.destroy()

    ventanaResultados = tk.Tk()
    ventanaResultados.title('¡Resultados!')
    ventanaResultados.geometry(f'400x400+{x}+{y}')
    etiqueta = tk.Label(ventanaResultados, text='¡Resultados!', font=12)
    etiqueta.pack()

    tree = ttk.Treeview(ventanaResultados)
    tree['columns'] = ('col1', 'col2')

    # Formato de las columnas
    tree.column('#0', width=0, stretch=tk.NO)  # Columna fantasma
    tree.column('col1', anchor=tk.CENTER, width=80)
    tree.column('col2', anchor=tk.CENTER, width=80)

    # Encabezados de las columnas
    tree.heading('#0', text='', anchor=tk.CENTER)
    tree.heading('col1', text='Jugador', anchor=tk.CENTER)
    tree.heading('col2', text='Resultado', anchor=tk.CENTER)

    ventanaResultados.protocol("WM_DELETE_WINDOW", on_closing)

    with open('jugadores.bin', 'rb+') as archivo:
        jugadores = pickle.load(archivo)
        listaPuntaje = []
        listaJugadores = []
        listaResultados = []
        
        for i in jugadores:
            for e in i.items():
                listaPuntaje.append(e[1])

        listaPuntaje.sort(reverse=True)

        if len(listaPuntaje) == 1:
            listaJugadores.append(jugadores[0])

        for ext in range(0,len(listaPuntaje)):
            for elemento in jugadores:
                for toco in elemento.items():
                    print(elemento)
                    if (listaPuntaje[ext] == toco[1])and(listaPuntaje[ext]!=listaPuntaje[ext-1]):
                        listaJugadores.append(elemento)
        
        listaResultados = [[clave, valor] for dic in listaJugadores for clave, valor in dic.items()]

        for item in listaResultados:
            tree.insert('', 'end', values=item)
        
    boton_end = tk.Button(ventanaResultados, text='Terminar', command=terminar)
    boton_end.pack(pady=30)

    tree.pack(padx=20)
    ventanaResultados.mainloop()

def salir(usuario):

    nombre = usuario
    with open('jugadores.bin', 'rb+') as archivo:
        jugadores = pickle.load(archivo)
        dicc = {}

        for var1 in jugadores:
            for var2 in var1.items():
                if var2[0] == nombre.lower():
                    jugadores.remove(var1)
                    dicc[nombre] = jugador
                    jugadores.append(dicc)
                    
        archivo.seek(0,2)
        archivo.seek(0)
        pickle.dump(jugadores, archivo)

    messagebox.showinfo("Resultado Final", f"La puntuación final es de:\nTú: {jugador}\nComputadora: {compu}\nEmpates: {empates}")
    salirBye()

ventana = tk.Tk()
ventana.title('¡Piedra, papel o tijera!')
ancho = ventana.winfo_screenwidth() // 2
alto = ventana.winfo_screenheight() // 2
x = (ancho) - (400 // 2)
y = (alto) - (150* 2)
ventana.geometry(f'450x200+{x}+{y}')

bienvenida = tk.Label(ventana, text='Ingrese su nombre', font=16)
bienvenida.pack()

entrada = tk.Entry(ventana, width=30)
entrada.pack(pady=20)

button_Start = tk.Button(ventana, text='¡Empezar!', command=guardar)  
button_Start.pack(pady=5) 

ventana.mainloop()
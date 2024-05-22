lista_de_diccionarios = [
    {'nombre': 'Lucas', 'edad': 30, 'ciudad': 'Buenos Aires'},
    {'nombre': 'Ana', 'edad': 25, 'ciudad': 'Córdoba'},
    {'nombre': 'Juan', 'edad': 35, 'ciudad': 'Rosario'}
]

# Convertir cada diccionario en una lista de sus valores
lista_de_listas = [list(dic.values()) for dic in lista_de_diccionarios]

print(lista_de_listas)
# Salida: [['Lucas', 30, 'Buenos Aires'], ['Ana', 25, 'Córdoba'], ['Juan', 35, 'Rosario']]

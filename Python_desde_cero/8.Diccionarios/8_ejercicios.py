# Ejercicio 1
mi_diccionario = {"name":"Ismael", "age":33, "country":"España"}
print(mi_diccionario)

#Ejercicio 2
print(mi_diccionario["name"])

# Ejercicio 3
mi_diccionario["job"] = "Programador"
print(mi_diccionario)

# Ejercicio 4
mi_diccionario["age"] = 38
print(mi_diccionario)

# Ejercicio 5
del mi_diccionario["country"]
print(mi_diccionario)

# Ejercicio 6
mi_diccionario = {1:1, 2:4, 3:9, 4:16, 5:25}
print(mi_diccionario)
# tambien valdría así
squares = {x: x**2 for x in range(1, 6)}
print(squares)

# Ejercicio 7
mi_diccionario = {"name": "Brais", "age": 37, "country": "Galicia"}
print("age" in mi_diccionario)

# Ejercicio 8
print(mi_diccionario.keys())

# Ejercicio 9
my_list = list(mi_diccionario.keys())
print(my_list)
# tambien valdría así
# print(list(my_dict.keys()))

# Ejercicio 10
mi_lista = ["name", "age", "job"]
mi_diccionario = dict.fromkeys(mi_lista, "Desconocido")
print(mi_diccionario)
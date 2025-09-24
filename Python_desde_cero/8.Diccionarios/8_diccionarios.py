# Diccionarios

my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {"Nombre":"Ismael", "Apellido":"Hernandez", "Edad":33, 1:"Python"}

my_dict = {
    "Nombre":"Ismael", 
    "Apellido":"Hernandez", 
    "Edad":33,
    "Lenguajes":{"Python","Java","PHP"}, 
    1:1.77
}

print(my_other_dict)
print(my_dict)

print(len(my_other_dict))
print(len(my_dict))

print(my_dict["Nombre"])

my_dict["Nombre"] = "Jose" # Para modificar el valor de la clave "Nombre" que ya existe en el diccionario
print(my_dict["Nombre"])

print(my_dict[1])

my_dict["Calle"] = "Naturaleza" # Para añadir un nuevo clave:valor al diccionario
print(my_dict)

del my_dict["Calle"] # Elimina la clave que se le indica del diccionario, si no se le pone clave elimina el diccionario completo como ocurria en las 
                     # clases anteriores(listas, tuplas, etc)
print(my_dict)

print("Hernandez" in my_dict)
print("Apellido" in my_dict)  # Va a buscar siempre por la clave no por el valor, por eso al buscar "Hernandez" indica False

print(my_dict.items()) # Se obtiene un listado con cada uno de los items (clave-valor)
print(my_dict.keys()) # Se obtiene solo las claves
print(my_dict.values()) # Se obtienen solo los valores

my_list = ["Nombre", 1, "Piso"]

my_new_dict = dict.fromkeys((my_list))
print(my_new_dict) # Obtiene el listado de claves pero sin valores
my_new_dict = dict.fromkeys(("Nombre", 1, "Piso"))
print(my_new_dict)
my_new_dict = dict.fromkeys(my_dict)
print(my_new_dict)
my_new_dict = dict.fromkeys(my_dict, "Telefonica")
print(my_new_dict)

print(list(my_new_dict))
print(tuple(my_new_dict))
print(set(my_new_dict))
# Sets

my_set = set()
my_other_set = {}

print(type(my_set))
print(type(my_other_set)) # Inicialmente es un diccionario

my_other_set = {"Ismael", "Hernandez", 33}
print(type(my_other_set))

print(len(my_other_set))

my_other_set.add("Telefonica")
print(my_other_set) # Un set no es una estructura ordenada

my_other_set.add("Telefonica") # Un set no admite repetidos
print(my_other_set)

print("Hernandez" in my_other_set) # Para comprobar o buscar si esa palabra existe dentro del set
print("Hernandes" in my_other_set)

my_other_set.remove("Hernandez")
print(my_other_set)

my_other_set.clear() # Elimina todos los elementos que contenga el set
print(len(my_other_set))

del my_other_set # Elimina el set al completo
# print(my_other_set) NameError: name 'my_other_set' is not defined

my_set = {"Ismael", "Hernandez", 33}
my_list = list(my_set)
print(my_list)
print(my_list[0]) # Sacar el primer elemento no tiene mucho sentido cuando el set no sigue un orden, va a sacar uno distinto por cada vez que se ejecute

my_other_set = {"Cordoba", "Valencia", "Zaragoza"}

my_new_set = my_set.union(my_other_set)
print(my_new_set.union(my_new_set).union(my_set).union({"Cadiz", "Oviedo"}))

print(my_new_set.difference(my_set)) # De my_new_set le estamos quitando los elementos de my_set y nos saca lo que sobra. 
                                     # No añade la union hecha en el print anterior porque no se ha guardado en una variable, sino que se hizo directamente en el print.
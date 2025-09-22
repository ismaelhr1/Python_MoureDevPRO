# Listas

my_list = list()
my_other_list = []

print(len(my_list))

my_list = [33, 63, 89, 12, 12, 102, 99]

print(my_list)
print(len(my_list))

my_other_list = [33, 1.70, "Ismael", "Hernandez"]

print(type(my_list))
print(type(my_other_list))

print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1])
print(my_other_list[-4])
print(my_list.count(12))
#print(my_other_list[4]) IndexError
#print(my_other_list[-5]) IndexError

print(my_other_list.index("Ismael"))

edad, estatura, nombre, apellido = my_other_list
print(nombre)

print(my_list + my_other_list)
#print(my_list - my_other_list)

my_other_list.append("Telefonica Tech") # Inserta al final de la lista
print(my_other_list)

my_other_list.insert(1, "Rojo") # Inserta en la posición que le indiques, en este caso en la la posición 1 (las posiciones empiezan por 0,1,2,3,4,5)
print(my_other_list)

my_other_list[1] = "Azul" # Se cambia el valor de la posición, en este caso el 1
print(my_other_list)

my_other_list.remove("Azul") # Elimina lo que se indica
print(my_other_list)

my_list.remove(12) # Elimina el primer 12 que encuentra, al haber dos, solamente elimina uno
print(my_list)

print(my_list.pop()) # Elimina el ultimo elemento de la lista
print(my_list)

print(my_list.pop(2)) # Elimina el elemento numero dos de la lista(las posiciones empiezan por 0,1,2,3,4,5)
print(my_list)

my_pop_element = my_list.pop(2) # Se puede hacer asi para guardar la variables que quita "pop"
print(my_pop_element)
print(my_list)

del my_list[2] # Elimina por indice, se le indica la posición (0,1,2,3,4,5)
print(my_list)

my_new_list = my_list.copy() # Copia la lista

my_list.clear() # Elimina/Limpia toda la lista
print(my_list)
print(my_new_list)

my_new_list.reverse() # Muestra la lista del revés
print(my_new_list)

my_new_list.sort() # Ordena la lista de menor a mayor
print(my_new_list)

print(my_new_list[0:2]) # Sublista/Subindices con slicing

my_list = "Hola Python"
print(my_list)
print(type(my_list))
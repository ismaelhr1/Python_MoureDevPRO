# Ejercicio 1
my_set = {1, 2, 3, 4, 5}
print(my_set)

# Ejercicio 2
my_set = {1, 2, 3, 4, 5}
my_set.add(6)
print(my_set)

# Ejercicio 3
my_set = {1, 2, 3, 4, 5}
my_set.add(5)
print(my_set) # No añade el 5 que le hemos puesto en el add porque ya tiene un 5 y los sets no admiten duplicados

# Ejercicio 4
my_set = {1, 2, 3, 4, 5}
print(3 in my_set)

#Ejercicio 5
my_set = {1, 2, 3, 4, 5}
my_set.remove(4)
print(my_set)

# Ejercicio 6
my_set = {1, 2, 3, 4, 5}
my_set.clear()
print(len(my_set))

# Ejercicio 7
my_set = {"manzana", "naranja", "plátano"}
my_list = list(my_set)
print(my_list[0])

# Ejercicio 8
my_first_set = {1, 2, 3}
my_second_set = {4, 5, 6}
my_final_set = my_first_set.union(my_second_set)
print(my_final_set)

# Ejercicio 9
my_first_set = {1, 2, 3, 4}
my_second_set = {3, 4, 5, 6}
print(my_first_set.difference(my_second_set))
# tambien valdria asi
my_set1 = {1, 2, 3, 4}
my_set2 = {3, 4, 5, 6}
my_difference_set = my_set1.difference(my_set2)
print(my_difference_set)

# Ejercicio 10
my_set = {"Sevilla", "Cadiz", "Cordoba", "Huelva"}
del my_set
print(my_set) # Esto da un error NameError porque con el "del" se ha eliminado el set al completo
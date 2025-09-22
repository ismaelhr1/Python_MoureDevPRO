# Ejercicio 1
my_tupla = (10, 20, 30, 40, 50)
print(my_tupla)

# Ejercicio 2
my_tupla = (100, 200, 300, 400, 500)
print(my_tupla[1])

# Ejercicio 3
my_tupla = (1, 2, 3)
# my_tupla[0] = 10  Esto generará un error: TypeError

# Ejercicio 4
my_tupla = (1, 2, 3, 3, 4, 5, 3)
print(my_tupla.count(3))

# Ejercicio 5
my_tupla = ("Java", "Python", "JavaScript", "Python")
print(my_tupla.index("Python"))

# Ejercicio 6
my_first_tupla = (1, 2, 3)
my_second_tupla = (4, 5, 6)
my_final_tupla = my_first_tupla + my_second_tupla
print(my_final_tupla)

# Ejercicio 7
my_tupla = (10, 20, 30, 40, 50)
print(my_tupla[2:4])
# tambien valdría así
my_tuple = (10, 20, 30, 40, 50)
my_subtuple = my_tuple[2:4]
print(my_subtuple)

# Ejercicio 8
my_tupla = ("rojo", "verde", "azul")
print(type(my_tupla))
my_tupla= list(my_tupla)
my_tupla[1] = "Amarillo"
print(type(my_tupla))
my_tupla = tuple(my_tupla)
print(type(my_tupla))
print(my_tupla)
# tambien valdría así
my_tuple = ("rojo", "verde", "azul")
my_list = list(my_tuple)
my_list[1] = "amarillo"
my_modified_tuple = tuple(my_list)
print(my_modified_tuple)

# Ejercicio 9
my_tuple = (12, 55, 62, "Ismael", "Remiro", "Sevilla")
del my_tuple
# print(my_tuple)

# Ejercicio 10
my_tupla_unic = (100, )
print(my_tupla_unic)
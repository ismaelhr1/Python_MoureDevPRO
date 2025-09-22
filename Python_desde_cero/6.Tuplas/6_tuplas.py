# Tuplas

my_tuple = tuple()
my_other_tuple = ()

my_tuple = (33, 1.70, "Ismael", "Hernandez", "Ismael")
my_other_tuple = (35, 60, 30)

print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])
# print(my_tuple[4]) IndexError
# print(my_tuple[-6]) IndexError

print(my_tuple.count("Ismael"))
print(my_tuple.index("Hernandez"))
print(my_tuple.index("Ismael"))

#mytuple[1] = 1.80 No lo permite porqu la tupla no puede editase ni permite añadir nada nuevo

my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)

print(my_sum_tuple[3:6])

my_tuple = list(my_tuple)
print(type(my_tuple))

my_tuple[4] = "Telefonica"
my_tuple.insert(1, "Rojo")
my_tuple = tuple(my_tuple)
print(my_tuple)
print(type(my_tuple))

# del my_tuple[2] TypeError: 'tuple' object doesn't support item deletion

del my_tuple
# print(my_tuple) NameError: name 'my_tuple' is not defined
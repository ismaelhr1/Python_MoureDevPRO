# Bucles

# while
my_condition = 0

while my_condition < 10:
    print(my_condition)
    my_condition += 2
else: # Es opcional
    print("Mi condición es igual o mayor que 10")

print("La ejecución continúa")

while my_condition < 20:
    my_condition += 1
    if my_condition == 15:
        print("Se detiene la ejecución")
        break # Detiene la ejecución y se termina el bucle
    print(my_condition)

print("La ejecución continúa")

# for
my_list = [35, 24, 62, 52, 30, 30, 17]

for element in my_list:
    print(element)

my_tuple = (33, 1.70, "Ismael", "Hernandez", "Ismael")
for element in my_tuple:
    print(element)

my_set = {"Ismael", "Hernandez", 33}
for element in my_set:
    print(element)

my_dict = {"Nombre":"Ismael", "Apellido":"Hernandez", "Edad":33, 1:"Python"}
for element in my_dict: # Va a sacar solamente las "claves" para que pinte el "valor" hay que añadir values() EJ: my_dict.values()
    print(element)
    if element == "Edad":
        break
else:
    print("El bucle for para diccionario ha finalizado")

print("La ejecución continúa")

my_dict = {"Nombre":"Ismael", "Apellido":"Hernandez", "Edad":33, 1:"Python"}
for element in my_dict: 
    print(element)
    if element == "Edad":
        continue
    print("Se ejecuta")
else:
    print("El bucle for para diccionario ha finalizado")
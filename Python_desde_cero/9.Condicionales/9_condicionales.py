# Condicionales

my_condition = False

if my_condition: # Es lo mismo que my_condition == True:
    print("Se ejecuta la condición del if")

my_condition = 5 * 1

if my_condition == 10: 
    print("Se ejecuta la condición del segundo if")

if my_condition > 10 and my_condition < 20:   # "Sí"
    print("Es mayor que 10 y menor que 20")
elif my_condition == 25:   # "Si no, entonces si..""
    print("Es igual a 25")
else:     # "Si no / en cualquier otro caso"
    print("Es menor o igual que 10 o mayor o igual que 20 o distinto de 25")

print("La ejecución continúa")

my_string = ""

if not my_string:
    print("Mi cadena de texto es vacia")

if my_string == "Mi cadena de textooo":
    print("Estas cadenas de texto coinciden")

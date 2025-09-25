# Ejercicio 1
numero = -10
if numero > 0:
    print("Este número es positivo.")
elif numero < 0:
    print("Este número es negativo.")
else:
    print("Este número es 0.")
 # también valdría así
number = int(input("Introduce un número: "))
if number > 0:
    print("El número es positivo")
elif number < 0:
    print("El número es negativo")
else:
    print("El número es cero")

# Ejercicio 2
edad = int(input("Introduzca su edad: "))
if edad >= 18:
    print("La persona es mayor de edad.")
else:
    print("La persona es menor de edad")

# Ejercicio 3
mi_texto = "hh"
if not mi_texto:
    print("El texto esta vacio")
else:
    print("El texto no esta vacio")
# también valdría así
text = input("Introduce una cadena: ")
if not text:
    print("La cadena está vacía")
else:
    print("La cadena no está vacía")

# Ejercicio 4
num1 = int(input("Primer número: "))
num2 = int(input("Segundo número: "))
if num1 > num2:
    print("El primer número es mayor que el segundo número")
elif num1 < num2:
    print("El segundo número es mayor que el primer número")
else:
    print("Los dos números son iguales")
#también valdría así
number1 = int(input("Introduce el primer número: "))
number2 = int(input("Introduce el segundo número: "))
if number1 > number2:
    print(f"{number1} es mayor que {number2}")
elif number1 < number2:
    print(f"{number1} es menor que {number2}")
else:
    print("Ambos números son iguales")

# Ejercicio 5
numero = int(input("Ingrese un número: "))
if numero % 3==0 and numero % 5==0:
    print(f"El número {numero} es divisible por 3 y por 5 ")
else:
    print(f"El número {numero} no es divisible por 3 y por 5.")

# Ejercicio 6
numero = int(input("Ingrese un número: "))
if numero % 2==0:
    print(f"El número {numero} es par.")
else:
    print(f"El número {numero} es impar.")

# Ejercicio 7
edad = int(input("Introduce tu edad: "))
if edad >=18:
    print("Esta persona puede votar.")
elif edad == 16 or edad == 17:
    print("Esta persona puede votar con permiso especial.")
else:
    print("Esta persona no puede votar.")
# también valdría así
age = int(input("Introduce tu edad: "))
if age >= 18:
    print("Puedes votar")
elif 16 <= age < 18:
    print("Puedes votar con permiso especial")
else:
    print("No puedes votar")

# Ejercicio 8
contraseña_predefinida = "sevilla"
contraseña = input("Introduce una contraseña: ")
if contraseña == contraseña_predefinida:
    print("La contraseña es válida.")
else:
    print("ERROR: La contraseña no es válida.")

# Ejercicio 9
numero = int(input("Ingrese un número: "))
if numero >= 10 and numero <= 20:
    print(f"El número {numero} esta entre el 10 y el 20")
else:
    print(f"El número {numero} no esta entre el 10 y el 20")

# Ejercicio 10
color = input("Introduce un color: ")
if color == "rojo":
    print("La persona tiene que detenerse.")
elif color == "amarillo":
    print("La persona debe estar en alerta.")
elif color == "verde":
    print("La persona puede avanzar.")
else:
    print("Color no válido")
# también valdría así
color = input("Introduce un color (rojo, amarillo, verde): ").lower() # "lower" es para que lo ponga todo en minuscula y que lo sepa interpretar tambien. Ej: ROJO, Rojo
if color == "rojo":
    print("Detente")
elif color == "amarillo":
    print("Precaución")
elif color == "verde":
    print("Avanza")
else:
    print("Color no válido")
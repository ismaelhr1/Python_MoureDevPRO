# Strings

my_string = "Mi String"
my_other_string = "Mi otro String"

print(len(my_string))
print(len(my_other_string))

print(my_string + " " + my_other_string)

my_new_line_string = "Este es un string\ncon salto de línea"
print(my_new_line_string)

my_tab_string = "\tEste es un string con tabulación"
print(my_tab_string)

my_scape_string = "\\tEste es un string \\nescapado"
print(my_scape_string)

# Formateo

name, surname, age = "Ismael", "Hernandez", 33

print("Mi nombre es {} {} y mi edad es {}".format(name, surname, age))
print("Mi nombre es %s %s y mi edad es %d" %(name, surname, age))
print("Mi nombre es " + name + " " + surname + " y mi edad es " + str(age)) #este no es aconsejable por ser un poco mas farragoso
print(f"Mi nombre es {name} {surname} y mi edad es {age}")

# Desempaquetado de caracteres

language = "python"
a, b, c, d, e, f = language
print(a)
print(b)

# División

language_slice = language[1:3]
print(language_slice)

language_slice = language[1:]
print(language_slice)

language_slice = language[-2]
print(language_slice)

language_slice = language[0:6:2]
print(language_slice)

# Reverse

reversed_language = language[::-1]
print(reversed_language)

# Funciones

print(language.capitalize()) # Pone en mayusculas la primera letra
print(language.upper()) # Pone en mayusculas todas las letras
print(language.count("n")) # Cuenta cuantas n tiene
print(language.isnumeric()) # Indica si es un numero (True o False)
print("1".isnumeric()) # Indica si es un numero (True o False)
print(language.lower()) # Pone en minusculas todas las letras
print(language.lower().isupper()) # Indica si esta en mayusculas (True o False)
print(language.startswith("Py")) # Indica si empieza por las letras que se le indica (True o False)
print("py" == "Py") # Hace lo mismo que el startwith (True o False)

# PRIMER EJERCICIO 
suma = 0

for i in range(5):
    numero = int(input("Ingrese un número: "))
    if numero > 0 and numero % 2 == 0:
        suma += numero

print(f"\nLa suma de los positivos y pares es: {suma}")

#SEGUNDO EJERCICIO 

try:
    edad = int(input("Ingrese la edad de la persona: "))

    if edad <= 0:
        print("Error: La edad debe ser un número entero positivo.")
    elif edad < 13:
        print("Niño")
    elif edad <= 17:
        print("Adolescente")
    elif edad <= 59:
        print("Adulto")
    else:
        print("Adulto mayor")

except ValueError:
    print("Error: Ingrese un número entero válido.")

# TERCER EJERCICIO
# Solicitar una palabra sin espacios
palabra = input("Ingrese una palabra (sin espacios): ")5

# Verificar que la palabra no tenga espacios
if " " in palabra:
    print("Error: La palabra no debe contener espacios.")
else:
    # Crear un diccionario para contar vocales
    conteo_vocales = {
        'a': 0, 'A': 0,
        'e': 0, 'E': 0,
        'i': 0, 'I': 0,
        'o': 0, 'O': 0,
        'u': 0, 'U': 0
    }

    # Recorrer la palabra letra por letra
    for letra in palabra:
        if letra in conteo_vocales:
            conteo_vocales[letra] += 1

    # Mostrar los resultados
    print("La palabra tiene:")
    for vocal in ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']:
        print(f"{vocal}: {conteo_vocales[vocal]}")







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
palabra = input("Ingrese una palabra (sin espacios): ")

# Verificar que la palabra no tenga espacios
if " " in palabra:
    print("Error: La palabra no debe contener espacios.")
else:
    # Iniciar contador por cada vocal (mayúscula y minúscula)
    a = A = e = E = i = I = o = O = u = U = 0

    # Recorrer la palabra letra por letra
    for letra in palabra:
        if letra == 'a':
            a += 1
        elif letra == 'A':
            A += 1
        elif letra == 'e':
            e += 1
        elif letra == 'E':
            E += 1
        elif letra == 'i':
            i += 1
        elif letra == 'I':
            I += 1
        elif letra == 'o':
            o += 1
        elif letra == 'O':
            O += 1
        elif letra == 'u':
            u += 1
        elif letra == 'U':
            U += 1

    # Mostrar los resultados
    print("\nLa palabra tiene:")
    print("a:", a)
    print("A:", A)
    print("e:", e)
    print("E:", E)
    print("i:", i)
    print("I:", I)
    print("o:", o)
    print("O:", O)
    print("u:", u)









# Desafío 1: Clasificar números
# Este programa recibe tres números distintos,
# los compara utilizando operadores lógicos y
# los muestra ordenados de menor a mayor.

print("Desafío 1: Clasificar números")

# Solicitar al usuario que ingrese tres números distintos
numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))
numero3 = int(input("Ingrese el tercer número: "))
# Determinar cuál es el número menor utilizando comparaciones y operadores lógicos
if numero1 < numero2 and numero1 < numero3:
    menor = numero1


elif numero2 < numero1 and numero2 < numero3:
    menor = numero2


else:
    menor = numero3


# Determinar cuál es el número mayor utilizando comparaciones y operadores lógicos
if numero1 > numero2 and numero1 > numero3:
    mayor = numero1


elif numero2 > numero1 and numero2 > numero3:
    mayor = numero2


else:
    mayor = numero3


# El número del medio será el que no es ni el menor ni el mayor
if numero1 != menor and numero1 != mayor:
    medio = numero1


elif numero2 != menor and numero2 != mayor:
    medio = numero2


else:
    medio = numero3


# Mostrar el resultado final
print()


print("Los números ordenados de menor a mayor son:")


print(menor, medio, mayor)

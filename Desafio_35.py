# Desafío 35: Generador de contraseña aleatoria
# Este programa genera una contraseña aleatoria de 8 caracteres
# que incluye letras minúsculas, letras mayúsculas y números.


print("Desafío 35: Generador de contraseña aleatoria")


# Importar los módulos necesarios
import random
import string




# Crear una función para generar la contraseña
def generar_contrasena():
    """Genera una contraseña aleatoria de 8 caracteres."""


    # Elegir al menos una letra minúscula
    minuscula = random.choice(string.ascii_lowercase)


    # Elegir al menos una letra mayúscula
    mayuscula = random.choice(string.ascii_uppercase)


    # Elegir al menos un número
    numero = random.choice(string.digits)


    # Crear el conjunto de caracteres disponibles
    caracteres = string.ascii_letters + string.digits


    # Generar los 5 caracteres restantes
    restantes = random.choices(caracteres, k=5)


    # Crear una lista con los 8 caracteres
    contrasena = [minuscula, mayuscula, numero] + restantes


    # Mezclar los caracteres para que los primeros tres
    # no aparezcan siempre en el mismo orden
    random.shuffle(contrasena)


    # Unir los caracteres de la lista en una sola cadena
    return "".join(contrasena)




# Crear la función principal
def main():
    """Genera y muestra la contraseña."""


    # Generar una contraseña aleatoria
    contrasena = generar_contrasena()


    # Mostrar el resultado
    print("Contraseña generada:", contrasena)




# Ejecutar el programa
if __name__ == "__main__":
    main()
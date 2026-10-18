# Desafío 63: Herencia y sobrescritura de métodos


# Clase base
class Autor:
    def __init__(self, nombre, nacionalidad):
        self.nombre = nombre
        self.nacionalidad = nacionalidad


    def biografia(self):
        print("Biografía de la clase Autor:")
        print(f"{self.nombre} es un autor de nacionalidad {self.nacionalidad}.")




# Clase Escritor que hereda de Autor
class Escritor(Autor):
    def __init__(self, nombre, nacionalidad, genero_literario):
        super().__init__(nombre, nacionalidad)
        self.genero_literario = genero_literario


    # Sobrescritura del método biografia
    def biografia(self):
        print("Biografía de la clase Escritor:")
        print(f"Nombre: {self.nombre}")
        print(f"Nacionalidad: {self.nacionalidad}")
        print(f"Género literario: {self.genero_literario}")




# Crear un objeto de la clase Escritor
escritor1 = Escritor(
    "Mario Benedetti",
    "Uruguaya",
    "Poesía y narrativa"
)


# Llamar al método de la clase Escritor
print("MÉTODO DE LA CLASE ESCRITOR")
escritor1.biografia()


print()


# Acceder al método original de la clase Autor
print("MÉTODO DE LA CLASE AUTOR")
super(Escritor, escritor1).biografia()




# Reflexión:
# La clase Escritor hereda de Autor y sobrescribe biografia().
# Al llamar escritor1.biografia(), se ejecuta el método de Escritor.
# Con super(Escritor, escritor1).biografia() se accede
# al método original de la clase Autor.

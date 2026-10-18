# Desafío 58: Herencia entre Usuario y Bibliotecario


# Clase base
class Usuario:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad


    def mostrar_informacion(self):
        print("Nombre:", self.nombre)
        print("Edad:", self.edad)




# Clase Bibliotecario que hereda de Usuario
class Bibliotecario(Usuario):
    def __init__(self, nombre, edad, seccion, años_experiencia):
        # Inicializar los atributos heredados
        super().__init__(nombre, edad)


        # Atributos específicos del bibliotecario
        self.seccion = seccion
        self.años_experiencia = años_experiencia


    def mostrar_informacion(self):
        # Mostrar los datos heredados
        super().mostrar_informacion()


        # Mostrar los atributos específicos
        print("Sección:", self.seccion)
        print("Años de experiencia:", self.años_experiencia)




# Crear un objeto Bibliotecario
bibliotecario1 = Bibliotecario(
    "María González",
    35,
    "Literatura infantil",
    10
)


# Mostrar información del bibliotecario
print("INFORMACIÓN DEL BIBLIOTECARIO")
bibliotecario1.mostrar_informacion()




# Reflexión:
# La clase Bibliotecario hereda los atributos nombre y edad
# de la clase Usuario.
# Además, incorpora sus propios atributos: sección y
# años_experiencia.
# Utilizamos super() para reutilizar el código de la clase base.



# Desafío 60: Herencia múltiple


class Escritor:
    def __init__(self, nombre, **kwargs):
        super().__init__(**kwargs)
        self.nombre = nombre


    def mostrar_escritor(self):
        print("Nombre del escritor:", self.nombre)




class Academico:
    def __init__(self, universidad, **kwargs):
        super().__init__(**kwargs)
        self.universidad = universidad


    def mostrar_academico(self):
        print("Universidad:", self.universidad)




# Clase que hereda de Escritor y Academico
class EscritorAcademico(Escritor, Academico):
    def __init__(self, nombre, universidad):
        # Inicializa las clases base mediante super()
        super().__init__(nombre=nombre, universidad=universidad)
        self.articulos = []


    # Método adicional para publicar artículos
    def publicar_articulo(self, titulo):
        self.articulos.append(titulo)
        print("Artículo publicado:", titulo)


    def mostrar_informacion(self):
        self.mostrar_escritor()
        self.mostrar_academico()


        print("Artículos académicos:")
        for articulo in self.articulos:
            print("-", articulo)




# Crear un objeto EscritorAcademico
escritor1 = EscritorAcademico(
    "Ana Martínez",
    "Universidad de la República"
)


# Publicar artículos académicos
escritor1.publicar_articulo("La educación en la era digital")
escritor1.publicar_articulo("Inteligencia artificial y aprendizaje")


# Mostrar información completa
print("\nINFORMACIÓN DEL ESCRITOR ACADÉMICO")
escritor1.mostrar_informacion()




# Reflexión:
# EscritorAcademico hereda de dos clases: Escritor y Academico.
# Utilizamos super() y **kwargs para inicializar ambas clases
# respetando el orden de resolución de métodos de Python (MRO).
# Además, agregamos un método propio para publicar artículos.



# Desafío 64: Herencia con LibroEspecializado


# Clase base
class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor


    def mostrar_informacion(self):
        print("Título:", self.titulo)
        print("Autor:", self.autor)




# Subclase que hereda de Libro
class LibroEspecializado(Libro):
    def __init__(self, titulo, autor, campo_estudio, nivel_especializacion):
        # Inicializar los atributos heredados
        super().__init__(titulo, autor)


        # Atributos propios de LibroEspecializado
        self.campo_estudio = campo_estudio


        # Validar el nivel de especialización
        niveles_validos = ["básico", "intermedio", "avanzado"]


        if nivel_especializacion.lower() not in niveles_validos:
            raise ValueError(
                "El nivel debe ser básico, intermedio o avanzado."
            )


        self.nivel_especializacion = nivel_especializacion.lower()


    # Sobrescribir el método para mostrar todos los datos
    def mostrar_informacion(self):
        super().mostrar_informacion()
        print("Campo de estudio:", self.campo_estudio)
        print("Nivel de especialización:", self.nivel_especializacion)




# Crear un libro especializado
libro1 = LibroEspecializado(
    "Introducción a Python",
    "Ana Martínez",
    "Informática",
    "básico"
)


# Crear otro libro especializado
libro2 = LibroEspecializado(
    "Inteligencia Artificial",
    "Carlos Pérez",
    "Tecnología",
    "avanzado"
)


# Mostrar la información de ambos libros
print("LIBRO ESPECIALIZADO 1")
libro1.mostrar_informacion()


print()


print("LIBRO ESPECIALIZADO 2")
libro2.mostrar_informacion()




# Reflexión:
# LibroEspecializado hereda los atributos título y autor de Libro.
# Con super() reutilizamos el constructor de la clase base.
# Agregamos campo_estudio y nivel_especializacion.
# También validamos que el nivel sea uno de los permitidos.




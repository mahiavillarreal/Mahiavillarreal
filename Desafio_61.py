# Desafío 61: Herencia múltiple y composición
# en una biblioteca




# Clase base
class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario


    def mostrar_informacion(self):
        print("Nombre:", self.nombre)
        print("Salario: $", self.salario)




# Clase para tareas administrativas
class Administrador:
    def gestionar_recursos(self):
        print("Gestionando recursos de la biblioteca.")




# Clase para tareas de mantenimiento
class Mantenimiento:
    def realizar_mantenimiento(self):
        print("Realizando mantenimiento de equipos.")




# Gerente hereda de Empleado y Administrador
# Ejemplo de herencia múltiple
class Gerente(Empleado, Administrador):
    def __init__(self, nombre, salario):
        super().__init__(nombre, salario)


    def mostrar_rol(self):
        print("Cargo: Gerente")




# Técnico hereda de Empleado
# y utiliza composición con Mantenimiento
class Tecnico(Empleado):
    def __init__(self, nombre, salario):
        super().__init__(nombre, salario)
        self.mantenimiento = Mantenimiento()


    def mostrar_rol(self):
        print("Cargo: Técnico")


    def reparar_equipo(self):
        self.mantenimiento.realizar_mantenimiento()




# Voluntario hereda de Empleado
class Voluntario(Empleado):
    def __init__(self, nombre):
        super().__init__(nombre, 0)


    def mostrar_rol(self):
        print("Cargo: Voluntario")




# Crear objetos
gerente = Gerente("María González", 65000)
tecnico = Tecnico("Juan Pérez", 45000)
voluntario = Voluntario("Lucía Rodríguez")




# Mostrar información del gerente
print("GERENTE")
gerente.mostrar_informacion()
gerente.mostrar_rol()
gerente.gestionar_recursos()


print()


# Mostrar información del técnico
print("TÉCNICO")
tecnico.mostrar_informacion()
tecnico.mostrar_rol()
tecnico.reparar_equipo()


print()


# Mostrar información del voluntario
print("VOLUNTARIO")
voluntario.mostrar_informacion()
voluntario.mostrar_rol()
# Reflexión:
# La herencia permite reutilizar atributos y métodos.
# Gerente utiliza herencia múltiple porque hereda
# de Empleado y Administrador.
# Tecnico utiliza composición porque contiene
# un objeto de la clase Mantenimiento.
# Así se pueden combinar diferentes responsabilidades.

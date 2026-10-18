# Desafío 66: Polimorfismo en operaciones matemáticas


# Clase base
class Operacion:
    def __init__(self, numero1, numero2):
        self.numero1 = numero1
        self.numero2 = numero2


    def resultado(self):
        raise NotImplementedError(
            "Las subclases deben implementar el método resultado()."
        )




# Subclase Suma
class Suma(Operacion):
    def resultado(self):
        return self.numero1 + self.numero2




# Subclase Multiplicacion
class Multiplicacion(Operacion):
    def resultado(self):
        return self.numero1 * self.numero2




# Crear objetos de las subclases
suma = Suma(8, 4)
multiplicacion = Multiplicacion(8, 4)


# Guardar las operaciones en una lista
operaciones = [suma, multiplicacion]


# Demostrar el polimorfismo
print("DESAFÍO 66: POLIMORFISMO EN OPERACIONES MATEMÁTICAS")
print()


for operacion in operaciones:
    print("Operación:", type(operacion).__name__)
    print("Número 1:", operacion.numero1)
    print("Número 2:", operacion.numero2)
    print("Resultado:", operacion.resultado())
    print()




# Reflexión:
# Suma y Multiplicacion heredan de Operacion.
# Ambas sobrescriben el método resultado().
# Al llamar resultado() sobre distintos objetos,
# cada uno realiza su propia operación matemática.
# Esto demuestra el polimorfismo.

# Desafío 62: Polimorfismo con músicos


# Clase base
class Musico:
    def instrumento(self):
        print("El músico toca un instrumento.")




# Subclase Guitarrista
class Guitarrista(Musico):
    def instrumento(self):
        print("El guitarrista toca la guitarra.")




# Subclase Baterista
class Baterista(Musico):
    def instrumento(self):
        print("El baterista toca la batería.")




# Crear objetos
musico = Musico()
guitarrista = Guitarrista()
baterista = Baterista()


# Guardar los objetos en una lista
musicos = [musico, guitarrista, baterista]


# Demostrar el polimorfismo
print("DESAFÍO 62: POLIMORFISMO CON MÚSICOS")
print()


for persona in musicos:
    persona.instrumento()




# Reflexión:
# Guitarrista y Baterista heredan de Musico.
# Ambas subclases sobrescriben el método instrumento().
# Al llamar al mismo método sobre diferentes objetos,
# cada uno ejecuta su propia implementación.
# Esto demuestra el polimorfismo.

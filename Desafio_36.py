# Desafío 36: Módulo personalizado para formatear texto
# Este programa importa un módulo personalizado llamado formateo
# y utiliza sus funciones para aplicar diferentes formatos
# a un texto ingresado por el usuario.


print("Desafío 36: Módulo personalizado de formateo")


# Importar el módulo personalizado creado en formateo.py
import formateo




def main():
    """Solicita un texto y muestra diferentes formatos."""


    # Solicitar al usuario que ingrese un texto
    texto = input("Ingrese un texto: ")


    # Utilizar las funciones creadas en el módulo formateo
    texto_negrita = formateo.negrita(texto)
    texto_italica = formateo.italica(texto)
    texto_subrayado = formateo.subrayado(texto)
    texto_tachado = formateo.tachado(texto)


    # Mostrar los diferentes formatos
    print()
    print("FORMATOS DEL TEXTO:")
    print("Negrita:", texto_negrita)
    print("Itálica:", texto_italica)
    print("Subrayado:", texto_subrayado)
    print("Tachado:", texto_tachado)




# Ejecutar el programa principal
if __name__ == "__main__":
    main()
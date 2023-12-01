"""
27/11/2023

Práctica del examen para realizar en casa
-----------------------------------------

* El programa debe estar correctamente documentado.

* Debes intentar ajustarte lo máximo que puedas a lo que se pide en los comentarios TODO.

* Tienes libertad para desarrollar los métodos o funciones que consideres, pero estás obligado a usar como mínimo todos los que se solicitan en los comentarios TODO.

* Además, tu programa deberá pasar correctamente las pruebas unitarias que se adjuntan en el fichero test_agenda.py, por lo que estás obligado a desarrollar los métodos que se importan y prueban en la misma: pedir_email(), validar_email() y validar_telefono()

"""

import os
import pathlib
from os import path

# Constantes globales
RUTA = pathlib.Path(__file__).parent.absolute() 

NOMBRE_FICHERO = 'contactos.csv'

RUTA_FICHERO = path.join(RUTA, NOMBRE_FICHERO)

#TODO: Crear un conjunto con las posibles opciones del menú de la agenda
OPCIONES_MENU = {1, 2, 3, 4, 5, 6, 7, 8}
#TODO: Utiliza este conjunto en las funciones agenda() y pedir_opcion()

def borrar_consola():
    """ Limpia la consola
    """
    if os.name == "posix":
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system ("cls")


def pulse_tecla_para_continuar():
    """ Muestra un mensaje y realiza una pausa hasta que se pulse una tecla
    """
    print("\n")
    os.system("pause")


def mostrar_menu():
    print("\nMenú:")
    print("1. Nuevo contacto")
    print("2. Modificar contacto")
    print("3. Eliminar contacto")
    print("4. Vaciar agenda")
    print("5. Cargar agenda inicial")
    print("6. Mostrar contactos por criterio")
    print("7. Mostrar la agenda completa")
    print("8. Salir")


def pedir_opcion():
    opc_ok = False
    while not opc_ok:
        try:
            opcion = int(input("Elije una opcion: "))
            if opcion in OPCIONES_MENU:
                return opcion 
            else:
                print("Elije opcion correcta (1-8)")

        except ValueError:
            print("Debes ingresar valor numerico (1-8))")


def agregar_contacto(contactos):
    nombre = input("\nIngrese el nombre del contacto: ").title()
    apellido = input("Ingrese el apellido del contacto: ").title()
    
    email = pedir_email(contactos)
    
    telefonos = pedir_telefono()

    # Crear un diccionario con la información del contacto
    nuevo_contacto = {"nombre": nombre, "apellido": apellido, "email": email, "telefonos": telefonos}

    # Añadir el contacto a la lista
    contactos.append(nuevo_contacto)

    print(f"Contacto {nombre} {apellido} añadido correctamente.")


def pedir_email(contactos):
    email = ""
    while not email or not validar_email(contactos, email):
        email = input("Ingrese el correo del contacto: ")
        if not email:
            print("El email no puede estar vacío.")
    return email


def validar_email(contactos, email):
    if "@gmail.com" not in email:
        return False

    for contacto in contactos:
        if email.lower() == contacto["email"].lower():
            return False

    return True


def pedir_telefono():
    lista_tel = []
    input_tel = input("Ingrese el teléfono del contacto (deje en blanco para terminar): ")
    input_tel = input_tel.replace(" ", "").replace("-", "").upper()
    while input_tel:
        if validar_telefono(input_tel):
            lista_tel.append(input_tel)
        else:
            print("Teléfono no válido.")
        input_tel = input("Ingrese otro teléfono del contacto (deje en blanco para terminar): ")

    return lista_tel


def validar_telefono(input_tel):
    try:
        if input_tel[0] == "+":
            return len(input_tel) == 12  
        else:
            return len(input_tel) == 9
    except IndexError:
        return False



def buscar_contacto(contactos : list, email : str):
    """ Busca la posición de un contacto en la lista por su email
    ...
    """
    email = input("Ingrese el correo del contacto: ")

    for i, contacto in enumerate(contactos):
        if contacto.get("email") == email:
            return i
    return None


def modificar_contacto():
    print()


def eliminar_contacto(contactos: list, email: str):
    """ Elimina un contacto de la agenda
    ...
    """
    try:
        pos = buscar_contacto(contactos, email)

        if pos != None:
            del contactos[pos]
            print("Se eliminó 1 contacto")
        else:
            print("No se encontró el contacto para eliminar")
    except Exception as e:
        print(f"**Error** {e}")
        print("No se eliminó ningún contacto")


def agenda(contactos: list):
    """ Ejecuta el menú de la agenda con varias opciones
    ...
    """
    #TODO: Crear un bucle para mostrar el menú y ejecutar las funciones necesarias según la opción seleccionada...

    while opcion != 7:
        mostrar_menu()
        opcion = pedir_opcion()

        #TODO: Se valorará que utilices la diferencia simétrica de conjuntos para comprobar que la opción es un número entero del 1 al 6
        if opcion in "?":
        
            print()


def cargar_contactos(contactos: list):
    """ Carga los contactos iniciales de la agenda desde un fichero
    ...
    """
    #TODO: Controlar los posibles problemas derivados del uso de ficheros...

    with open(RUTA_FICHERO, 'r') as fichero:
        for linea in fichero:
            print(linea)

def mostrar_contactos(contactos : list):
    # Clonar la lista de contactos para no modificar la original
    contactos_ordenados = sorted(contactos, key=lambda x: x['nombre'])

    print("AGENDA ({}):".format(len(contactos)))
    print("------")
    
    for contacto in contactos_ordenados:
        print(f"Nombre: {contacto['nombre']} ({contacto.get('email')})")
        telefonos = contacto.get('telefonos')
        print("Teléfonos: {}".format(" / ".join(telefonos)))
        print("......")


def main():
    """ Función principal del programa
    """
    borrar_consola()

    contactos = []

    #TODO: Modificar la función cargar_contactos para que almacene todos los contactos del fichero en una lista con un diccionario por contacto (claves: nombre, apellido, email y telefonos)


    cargar_contactos(contactos)

    #TODO: Crear función para agregar un contacto. Debes tener en cuenta lo siguiente:
    # - El nombre y apellido no pueden ser una cadena vacía o solo espacios y se guardarán con la primera letra mayúscula y el resto minúsculas (ojo a los nombre compuestos)
    # - El email debe ser único en la lista de contactos, no puede ser una cadena vacía y debe contener el carácter @.
    # - El email se guardará tal cuál el usuario lo introduzca, con las mayúsculas y minúsculas que escriba. 
    #  (CORREO@gmail.com se considera el mismo email que correo@gmail.com)
    # - Pedir teléfonos hasta que el usuario introduzca una cadena vacía, es decir, que pulse la tecla <ENTER> sin introducir nada.
    # - Un teléfono debe estar compuesto solo por 9 números, aunque debe permitirse que se introduzcan espacios entre los números.
    # - Además, un número de teléfono puede incluir de manera opcional un prefijo +34.
    # - De igual manera, aunque existan espacios entre el prefijo y los 9 números al introducirlo, debe almacenarse sin espacios.
    # - Por ejemplo, será posible introducir el número +34 600 100 100, pero guardará +34600100100 y cuando se muestren los contactos, el telófono se mostrará como +34-600100100. 

    #TODO: Realizar una llamada a la función agregar_contacto con todo lo necesario para que funcione correctamente.
    agregar_contacto(contactos )

    pulse_tecla_para_continuar()
    borrar_consola()


    eliminar_contacto(contactos )


    pulse_tecla_para_continuar()
    borrar_consola()


    mostrar_contactos(contactos)


    pulse_tecla_para_continuar()
    borrar_consola()

    #TODO: Crear un menú para gestionar la agenda con las funciones previamente desarrolladas y las nuevas que necesitéis:
    # AGENDA
    # ------
    # 1. Nuevo contacto
    # 2. Modificar contacto
    # 3. Eliminar contacto
    # 4. Vaciar agenda
    # 5. Cargar agenda inicial
    # 6. Mostrar contactos por criterio
    # 7. Mostrar la agenda completa
    # 8. Salir
    #
    # >> Seleccione una opción: 
    #
    #TODO: Para la opción 3, modificar un contacto, deberás desarrollar las funciones necesarias para actualizar la información de un contacto.
    #TODO: También deberás desarrollar la opción 6 que deberá preguntar por el criterio de búsqueda (nombre, apellido, email o telefono) y el valor a buscar para mostrar los contactos que encuentre en la agenda.
    agenda("?")


if __name__ == "__main__":
    main()
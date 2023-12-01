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

OPCIONES_CRITERIO = {1: "nombre", 2: "apellido", 3: "email", 4: "telefono"}
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
    print("AGENDA")
    print("-------")
    print("1. Nuevo contacto")
    print("2. Modificar contacto")
    print("3. Eliminar contacto")
    print("4. Vaciar agenda")
    print("5. Cargar agenda inicial")
    print("6. Mostrar contactos por criterio")
    print("7. Mostrar la agenda completa")
    print("8. Salir\n")


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

# NUEVO CONTACTO 
def agregar_contacto(contactos : list):
    nombre = input("\nIngrese el nombre del contacto: ").title()
    apellido = input("Ingrese el apellido del contacto: ").title()
    
    email = pedir_email(contactos)
    
    telefonos = pedir_telefono()

    # Crear un diccionario con la información del contacto
    nuevo_contacto = {"nombre": nombre, "apellido": apellido, "email": email, "telefonos": telefonos}

    # Añadir el contacto a la lista
    contactos.append(nuevo_contacto)

    print(f"Contacto {nombre} {apellido} añadido correctamente.")


def pedir_email(contactos : list):
    email = ""
    email = input("Ingrese el correo del contacto: ")
    while not email or not validar_email(contactos, email):
        email = input("Ingrese el correo del contacto válido: ")
        if not email:
            print("El email no puede estar vacío.")
    return email


def validar_email(contactos  : list, email : str):
    if "@gmail.com" not in email:
        return False

    for contacto in contactos:
        if email.lower() == contacto["email"].lower():
            return False

    return True


def pedir_telefono():
    lista_tel = []
    input_tel = input("Ingrese el teléfono del contacto (deje en blanco para terminar): ")
    while input_tel:
        if validar_telefono(input_tel):
            lista_tel.append(input_tel)
        else:
            print("Teléfono no válido.")
        input_tel = input("Ingrese otro teléfono del contacto (deje en blanco para terminar): ")

    return lista_tel


def validar_telefono(input_tel : str):
    input_tel.replace(" ", "").replace("-", "")
    try:
        if input_tel[0] == "+":
            return len(input_tel) == 12  
        else:
            return len(input_tel) == 9
    except ValueError:
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

# ELIMINAR CONTACTO

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


def cargar_contactos():
    """ Carga los contactos iniciales de la agenda desde un fichero
    ...
    """
    #TODO: Controlar los posibles problemas derivados del uso de ficheros...

    with open(RUTA_FICHERO, 'r') as fichero:
        for linea in fichero:
            print(linea)


def vaciar_agenda(contactos : list):
    contactos.clear()


def pedir_criterio():
    criterio = False
    while not criterio:
        try:
            criterio = int(input("Elije un criterio: "))
            if criterio in OPCIONES_CRITERIO:
                return criterio 
            else:
                print("Elije un criterio correcto (1-4)")

        except ValueError:
            print("Debes ingresar valor numerico (1-4)")


def mostrar_contactos_params(contactos : list, criterio : int):
    contactos_ordenados = sorted(contactos, key=lambda x: x[criterio])

    print(f"AGENDA ({len(contactos)}):")
    print("------")
    
    for contacto in contactos_ordenados:
        print(f"Nombre: {contacto['nombre']} ({contacto.get('email')})")
        telefonos = contacto.get('telefonos')
        print("Teléfonos: {}".format(" / ".join(telefonos)))
        print("......")


def mostrar_contactos(contactos : list):
    # Clonar la lista de contactos para no modificar la original
    contactos_ordenados = sorted(contactos, key=lambda x: x['nombre'])

    print(f"AGENDA ({len(contactos)}):")
    print("------")
    
    for contacto in contactos_ordenados:
        print(f"Nombre: {contacto['nombre']} ({contacto.get('email')})")
        telefonos = contacto.get('telefonos')
        print("Teléfonos: {}".format(" / ".join(telefonos)))
        print("......")


def agenda(contactos: list):
    """ Ejecuta el menú de la agenda con varias opciones
    ...
    """
    opcion = None
    while opcion != 8 :
        mostrar_menu()
        opcion = pedir_opcion()

        if opcion == 1:
            agregar_contacto(contactos)
            
        elif opcion == 2:
            modificar_contacto(contactos)
            
        elif opcion == 3:
            eliminar_contacto(contactos)
            
        elif opcion == 4: 
            vaciar_agenda(contactos)
            
        elif opcion == 5:
            cargar_contactos()
            
        elif opcion == 6:
            mostrar_contactos_params()
            
        elif opcion == 7:
            mostrar_contactos(contactos)
            
        pulse_tecla_para_continuar()
        borrar_consola()


def main():
    """ Función principal del programa
    """
    borrar_consola()

    contactos = []

    #TODO: Modificar la función cargar_contactos para que almacene todos los contactos del fichero en una lista con un diccionario por contacto (claves: nombre, apellido, email y telefonos)

    mostrar_menu()

    agenda(contactos)

    #TODO: Para la opción 3, modificar un contacto, deberás desarrollar las funciones necesarias para actualizar la información de un contacto.
    #TODO: También deberás desarrollar la opción 6 que deberá preguntar por el criterio de búsqueda (nombre, apellido, email o telefono) y el valor a buscar para mostrar los contactos que encuentre en la agenda.
    


if __name__ == "__main__":
    main()
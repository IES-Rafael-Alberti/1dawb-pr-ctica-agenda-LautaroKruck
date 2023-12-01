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

# CONSTANTES GLOBALES

RUTA = pathlib.Path(__file__).parent.absolute() 

NOMBRE_FICHERO = 'contactos.csv'

RUTA_FICHERO = path.join(RUTA, NOMBRE_FICHERO)

OPCIONES_MENU = {1, 2, 3, 4, 5, 6, 7, 8}

OPCIONES_CRITERIO = {1: "nombre", 2: "apellido", 3: "email", 4: "telefono"}

def borrar_consola():
    """ Limpia la consola.
    ...
    """
    if os.name == "posix":
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system ("cls")


def pulse_tecla_para_continuar():
    """ Muestra un mensaje y pausa hasta que se pulse una tecla.
    ...
    """
    print("\n")
    os.system("pause")


def mostrar_menu():
    """ Imprime el menú principal por pantalla.
    ...
    """
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
    """Solicita al usuario elegir una opción del menú.
    ...
    """
    opcion = None
    while opcion not in OPCIONES_MENU:

        try:
            opcion = int(input("Elije una opción: "))
            if opcion not in OPCIONES_MENU:
                print("Elije una opción correcta (1-8)")
        except ValueError:
            print("Debes ingresar un valor numérico (1-8)")
            
    return opcion

# NUEVO CONTACTO 

def agregar_contacto(contactos : list):
    """Añade un nuevo contacto a la lista de contactos.
    ...
    """
    nombre = input("\nIngrese el nombre del contacto: ").title()
    apellido = input("Ingrese el apellido del contacto: ").title()
    
    email = pedir_email(contactos)
    
    telefonos = pedir_telefono()

    nuevo_contacto = {"nombre": nombre, "apellido": apellido, "email": email, "telefonos": telefonos}

    contactos.append(nuevo_contacto)

    print(f"Contacto {nombre} {apellido} añadido correctamente.")


def pedir_email(contactos: list):
    """Solicita y valida la entrada del correo electrónico del contacto.
    ...
    """
    email = input("Ingrese el correo del contacto: ")
    
    while not email or not validar_email(contactos, email):
        if not email:
            raise ValueError("el email no puede ser una cadena vacía")

        if not validar_email(contactos, email):
            raise ValueError("el email no es un correo válido")

        if email.lower() in [contacto["email"].lower() for contacto in contactos]:
            raise ValueError("el email ya existe en la agenda")

        email = input("Ingrese el correo del contacto válido: ")

    return email


def validar_email(contactos  : list, email : str):
    """Valida si el correo electrónico ya existe en la lista de contactos.
    ...
    """
    if "@gmail.com" not in email:
        return False

    for contacto in contactos:
        if email.lower() == contacto["email"].lower():
            return False

    return True


def pedir_telefono():
    """Solicita y valida la entrada de teléfonos del contacto.
    ...
    """
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
    """Valida el formato del número de teléfono.
    ...
    """
    input_tel = input_tel.replace(" ", "").replace("-", "")
    try:
        if input_tel[0] == "+":
            return len(input_tel) == 12  
        else:
            return len(input_tel) == 9
    except ValueError:
        return False

# BUSCAR CONTACTO

def buscar_contacto(contactos : list, email : str):
    """ Busca la posición de un contacto en la lista por su email.
    ...
    """
    email = input("Ingrese el correo del contacto: ")

    for pos, contacto in enumerate(contactos):
        if contacto.get("email") == email:
            return pos
    return None

# MODIFICAR CONTACTO

def modificar_contacto(contactos:list, email):
    """Modifica los datos de un contacto existente.
    ...
    """
    try:
        pos = buscar_contacto(contactos, email)
        if pos != None:
            print("Introduce nuevos datos para el contacto ")
            nuevos_datos(contactos, pos)
            print("Se modificó 1 contacto")
        else:
            print("No se encontró el contacto para modificar")
    except ValueError as e:
        print(f"**Error** {e}")
        print("No se modificó ningún contacto")
    except Exception as e:
            print(f"**Error** {e}")
            print("No se modificó ningún contacto")


def nuevos_datos(contactos, pos):
    """Introduce nuevos datos para un contacto existente.
    ...
    """
    nombre = input("\nIngrese el nombre del contacto: ").title()
    apellido = input("Ingrese el apellido del contacto: ").title()
    email = pedir_email(contactos)
    telefonos = pedir_telefono()

    contactos[pos] = dict([ ("nombre", nombre), ("apellido", apellido), ("email", email), ("telefonos", telefonos) ])

# ELIMINAR CONTACTO

def eliminar_contacto(contactos: list, email: str):
    """ Elimina un contacto de la agenda.
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


def cargar_contactos(contactos: list):
    """ Carga los contactos iniciales de la agenda desde un fichero.
    ...
    """
    with open(RUTA_FICHERO, 'r') as fichero:
        for linea in fichero:
            # Procesar la línea y agregar el contacto a la lista
            # Supongo que la línea está en formato CSV, puedes ajustar esto según el formato real del archivo
            datos_contacto = linea.strip().split(',')
            nuevo_contacto = {
                "nombre": datos_contacto[0],
                "apellido": datos_contacto[1],
                "email": datos_contacto[2],
                "telefonos": datos_contacto[3:]
            }
            contactos.append(nuevo_contacto)


def vaciar_agenda(contactos : list):
    """ Elimina todos los contactos de la agenda.
    ...
    """
    contactos.clear()


def pedir_criterio():
    """Solicita al usuario elegir un criterio para ordenar la lista de contactos.
    ...
    """
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


def ordenar_contacto_criterio(contacto, criterio):
    return contacto[OPCIONES_CRITERIO.get(criterio)]

def mostrar_contactos_params(contactos: list):
    """Muestra la lista de contactos ordenada por el criterio especificado.
    ...
    """
    criterio = pedir_criterio()
    if criterio not in OPCIONES_CRITERIO:
        print("Criterio no válido. Mostrando contactos ordenados por nombre.")
        criterio = 1 

    contactos_ordenados = sorted(contactos, key=lambda x: ordenar_contacto_criterio(x, criterio))

    print(f"AGENDA ({len(contactos)}):")
    print("------")
    
    for contacto in contactos_ordenados:
        print(f"Nombre: {contacto['nombre']} ({contacto.get('email')})")
        telefonos = contacto.get('telefonos')
        print(f"Teléfonos: {" / ".join(telefonos)}")
        print("......")


def ordenar_contacto(contacto):
    return contacto['nombre']

def mostrar_contactos(contactos: list):
    """Muestra la lista de contactos ordenada por nombre.
    ...
    """
    contactos_ordenados = sorted(contactos, key=ordenar_contacto)

    print(f"AGENDA ({len(contactos)}):")
    print("------")
    
    for contacto in contactos_ordenados:
        print(f"Nombre: {contacto['nombre']} ({contacto.get('email')})")
        telefonos = contacto.get('telefonos')
        print(f"Teléfonos: {" / ".join(telefonos)}")
        print("......")


def agenda(contactos: list):
    """ Función principal que ejecuta el bucle del menú y gestiona las opciones.
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
    
    print ("Programa terminado")


def main():
    """ Función principal del programa que inicializa la agenda y llama a las funciones relevantes.
    ...
    """
    borrar_consola()

    contactos = []
    
    cargar_contactos(contactos)

    agregar_contacto(contactos)

    pulse_tecla_para_continuar()
    borrar_consola()

    eliminar_contacto(contactos)

    pulse_tecla_para_continuar()
    borrar_consola()


    mostrar_contactos(contactos)

    pulse_tecla_para_continuar()
    borrar_consola()

    agenda(contactos)


if __name__ == "__main__":
    main()
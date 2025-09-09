import pyfiglet
import pandas as pd
import os

# ---------------------------------------------
datos = pd.read_excel("datos.xlsx")
# ---------------------------------------------
# Configuramos el tamaño de letra de la consola
os.console.font = 'Lucida Console'

# Guardamos en la variable ascii_banner el mensaje que queremos mostrar
os.system("cls")
ascii_banner = pyfiglet.figlet_format("ContAgro")
# Imprimimos la variable ascii_banner
print(ascii_banner)

# La función print es una función de salida

print("")
print("Bienvenido a CONTAGRO 🌱")

# mientras la función input es una función de entrada
nombre = input("\nIngrese su nombre: ")

# ---------------------------------------------------

# Construimos la función menú (declaración de la función)


def menu(nombre):
    # Mostramos el menú con las opciones disponibles
    print(f"Hola {nombre}, seleccione una opción de nuestro menú:")
    print("\n1.Ingresar una nueva transacción")
    print("\n2.Resumir por transacción")
    print("\n3.Visualizar las últimas cinco (5) transacciones")
    print("\n4.Salir")
    # en la variable opción almacenamos la selección del usuario
    opcion = int(input("\nDigite una opción: "))
    # retornamos la variable opcion
    return opcion

# Construimos la función de la nueva transacción


def nueva_transaccion(nombre, datos):
    # solicita la fecha de la transacción
    fecha = input("\nIngrese la fecha de la transacción (DD/MM/YY): ")
    # solicita ingresar la descripción de la transacción (concepto)
    concepto = input("\nIngrese la descripción de la transacción:")
    # En cuenta se ingresa 1 para ingreso o 2 para egreso
    cuenta = input("\nIngrese 1 para Ingreso o 2 para Egreso:")
    # Si es un ingreso, en complemento se pregunta si es una venta o un aporte
    if cuenta == "1":
        complemento = input("\nIngrese 1 para Ventas o 2 para Aportes: ")
        if complemento == "1":
            # Genera el nombre completo de la cuenta, ya sea venta o aporte
            cuenta = "Ingreso - Venta"
        elif complemento == "2":
            cuenta = "Ingreso - Aporte"
        else:
            print(
                "\nLa opción seleccionada no es correcta, ingrese nuevamente la transacción")
            nueva_transaccion(nombre, datos)
    # Si es un egreso, pregunta si es operacional o es otro tipo de gasto
    elif cuenta == "2":
        # Genera el nombre completo de la cuenta
        complemento = input(
            "\nIngrese 1 para Gastos Operacionales o 2 para Otros Gastos: ")
        if complemento == "1":
            cuenta = "Egreso - Operacional"
        elif complemento == "2":
            cuenta = "Egreso - Otros"
        else:
            print(
                "\nLa opción seleccionada no es correcta, ingrese nuevamente la transacción")
            nueva_transaccion(nombre, datos)
    else:
        print("\nLa opción seleccionada no es correcta, ingrese nuevamente la transacción")
        nueva_transaccion(nombre, datos)
    # solicita el valor de la transacción
    valor = float(input("\nIngrese el valor de la transacción $COP: "))
    # Genera una lista con los datos de la transacción
    transaccion = [fecha, concepto, cuenta, valor, nombre]
    # ubica la última fila + 1 y agrega la nueva información
    datos.loc[len(datos)] = transaccion
    # guarda el archivo modificado
    datos.to_excel("datos.xlsx", index=False)
    input("\nLa transacción fue registrada, presione una tecla para continuar...")
    app(nombre, datos)

# Definimos la función ultimas_transacciones para visualizar las últimas 5
# transacciones almacenadas en el archivo de datos


def ultimas_transacciones(datos):
    # Imprimimos las últimas 5 transacciones almacenadas en datos
    print(datos.tail(5))

# Definimos la función menu_2 para que el usuario elija entre las
# siguientes opciones: promedio, total


def menu_2():
    # Mostramos el menú con las opciones disponibles
    print("Seleccione una opción de nuestro menú:")
    print("\n1.Promedio")
    print("\n2 Total por usuario")
    print("\n3.Total")
    print("\n4.Regresar al menú anterior")
    # en la variable opción almacenamos la selección del usuario
    opcion = int(input("\nDigite una opción: "))
    # retornamos la variable opcion
    return opcion


def revisar_opcion(opcion, nombre, datos):
    # Establecemos las condiciones para cada opción del menú
    # Inicializamos la lista de transacciones
    flag = True

    if opcion == 1:
        # En caso de que el usuario elija la opción 1, llama a la función
        # nueva_transaccion
        os.system("cls")
        nueva_transaccion(nombre, datos)
    elif opcion == 2:
        # En caso de que el usuario elija la opción 2, llama a la función
        # menú 2
        os.system("cls")
        opcion_2 = menu_2()
        # Revisamos los condicionales para la opción elegida por el usuario
        # en el menu_2 almacenada en opcion_2
        if opcion_2 == 1:
            # Imprimimos el promedio
            print("\nEl valor promedio por tipo de transacción es:")
            print(datos.groupby("Ingreso/Egreso")["Valor ($COP)"].mean())
            input("\nPresione una tecla para continuar...")
            app(nombre, datos)
        elif opcion_2 == 2:
            # Imprimimos el total por usuario
            print("\nEl total por usuario es:")
            print(datos.groupby("Nombre del editor")["Valor ($COP)"].sum())
            input("\nPresione una tecla para continuar...")
            app(nombre, datos)
        elif opcion_2 == 3:
            # Imprimimos la suma
            print("\nEl total por tipo de transacción es:")
            print(datos.groupby("Ingreso/Egreso")["Valor ($COP)"].sum())
            input("\nPresione una tecla para continuar...")
            app(nombre, datos)
        elif opcion_2 == 4:
            # En caso de que el usuario elija la opción 3, llama a la función
            # menu
            os.system("cls")
            app(nombre, datos)
        else:
            print("\nLa opción seleccionada no es correcta")
            print("\nVuelva a intentarlo")
            print("\n")
            app(nombre, datos)
    elif opcion == 3:
        # En caso de que el usuario elija la opcón 3, llama a  la función
        # ultimas_transacciones
        os.system("cls")
        ultimas_transacciones(datos)
        input("\nPresione una tecla para continuar...")
        app(nombre, datos)

    elif opcion == 4:
        # Salimos de la aplicación
        print("\nGracias por usar ContAgro")
        flag = False
    else:
        print("\nEsa opción no está dentro de nuestro menú")
        print("\nVuelva a intentarlo")
        print("\n")
        app(nombre, datos)
    return flag


def app(nombre, datos):
    os.system("cls")
    opcion = menu(nombre)
    revisar_opcion(opcion, nombre, datos)


# -------------------------------------------------
# hacemos uso de la función que acabamos de declarar. La salida
# de la función la almacenamos en la variable opcion
flag = True
while True:
    if flag:
        flag = app(nombre, datos)
    else:
        break

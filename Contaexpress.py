#!pip install pyfiglet

# Cargamos la libería del sistema
import os

# Cargamos la librería pyfiglet
import pyfiglet

os.system('cls')

# Guardamos en la variable ascii_banner el mensaje que queremos mostrar
ascii_banner = pyfiglet.figlet_format("ContaExpress")
# Imprimimos la variable ascii_banner
print(ascii_banner)

# Importamos la librería para gestión de Dataframes (tablas)
import pandas as pd

# La función print es una función de salida

print("")
print("Bienvenido a CONTAEXPRESS🔢")

# mientras la función input es una función de entrada
nombre = input("\n Ingrese su nombre: ")

os.system('cls')
# Construimos la función menú (declaración de la función)
def menu(nombre):
    # Mostramos el menú con las opciones disponibles
    print(f" Hola {nombre}, seleccione una opción de nuestro menú:")
    print("\n1.Ingresar una nueva transacción")
    print("\n2.Resumir por transacción")
    print("\n3.Visualizar las últimas cinco (5) transacciones")   
    # en la variable opción almacenamos la selección del usuario
    opcion = int(input("\n Digite una opción: "))
    # retornamos la variable opcion
    return opcion

# Construimos la función de la nueva transacción
def nueva_transaccion():
    fecha = input("\nIngrese la fecha de la transacción (DD/MM/YY): ")
    concepto = input("\nIngrese la descripción de la transacción:")
    cuenta = input("\nIngrese el tipo de cuenta (ingreso o egreso):")
    valor = float(input("\nIngrese el valor de la transacción USD$: "))
    transaccion = [fecha, concepto, cuenta, valor, nombre]
    # Abrimos el archivo de datos.xlsx para agregar la transacción
    # leemos el archivo con las transacciones
    datos = pd.read_excel("datos.xlsx")
    # ubica la última fila + 1 y agrega la nueva información
    datos.loc[len(datos)] = transaccion
    # guarda el archivo modificado
    datos.to_excel("datos.xlsx", index=False)

# Definimos la función ultimas_transacciones para visualizar las últimas 5
# transacciones almacenadas en el archivo de datos
def ultimas_transacciones():
    # Cargamos los datos del archivo datos.xlsx
    datos = pd.read_excel("datos.xlsx")
    print(datos.tail(5))  

# Definimos la función menu_2 para que el usuario elija entre las 
# siguientes opciones: promedio, total
def menu_2():
    # Mostramos el menú con las opciones disponibles
    print(f" Seleccione una opción de nuestro menú:")
    print("\n1.Promedio")
    print("\n2.Total") 
    print("\n3.Regresar al menú anterior")
    # en la variable opción almacenamos la selección del usuario
    opcion = int(input("\nDigite una opción: "))
    # retornamos la variable opcion
    return opcion    



# hacemos uso de la función que acabamos de declarar. La salida
# de la función la almacenamos en la variable opcion
opcion = menu(nombre)
os.system('cls')


# Establecemos las condiciones para cada opción del menú
# Inicializamos la lista de transacciones

if opcion == 1:
    # En caso de que el usuario elija la opción 1, llama a la función
    # nueva_transaccion
    nueva_transaccion()
elif opcion == 2:
    # En caso de que el usuario elija la opción 2, llama a la función
    # menú 2
    opcion_2 = menu_2()
    # Revisamos los condicionales para la opción elegida por el usuario
    # en el menu_2 almacenada en opcion_2
    if opcion_2 == 1:
        # primero cargamos los datos
        datos = pd.read_excel("datos.xlsx")
        # después calculamos la media o promedio
        datos[["Valor (USD$)"]].mean()
        # imprimimos el mensaje con el resultado
        print("\nEl promedio de las transacciones es: $", datos[["Valor (USD$)"]].mean())
    elif opcion_2 == 2:
        # primero cargamos los datos
        datos = pd.read_excel("datos.xlsx")
        # después calculamos la suma o total
        datos[["Valor (USD$)"]].sum()
        # imprimimos el mensaje con resultado
        print("\nEl total de las transacciones es: $", datos[["Valor (USD$)"]].sum())
    elif opcion_2 == 3:
        os.system('cls')
        menu(nombre)
    else:
        print("\nLa opción seleccionada no es correcta")
elif opcion == 3:
    # En caso de que el usuario elija la opcón 3, llama a  la función
    # ultimas_transacciones
    ultimas_transacciones()
else:
    print("\nEsa opción no está dentro de nuestro menú")
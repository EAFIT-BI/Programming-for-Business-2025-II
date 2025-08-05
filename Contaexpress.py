# Importamos la librería para gestión de Dataframes (tablas)
import pandas as pd

# La función print es una función de salida
print("Bienvenido a CONTAEXPRESS🔢")

# mientras la función input es una función de entrada
nombre = input("\n Ingrese su nombre: ")

# Mostramos el menú con las opciones disponibles
print(f" Hola {nombre}, seleccione una opción de nuestro menú:")
print("\n1. Ingresar una nueva transacción")
print("\n2. Resumir por transacción")
print("\n3. Visualizar las últimas cinco (5) transacciones")

# en la variable opción almacenamos la selección del usuario
opcion = int(input("\n Digite el número de la operación deseada: "))


# Establecemos las condiciones para cada opción del menú
# Inicializamos la lista de transacciones

if opcion == 1:
    print("\nIngresó la opción 1")
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
elif opcion == 2:
    print("\nIngresó la opción 2")
elif opcion == 3:
    # Cargamos los datos del archivo datos.xlsx
    datos = pd.read_excel("datos.xlsx")
    print(datos.tail(5))
else:
    print("\nEsa opción no está dentro de nuestro menú")
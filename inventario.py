"""El proyecto consiste en desarrollar un sistema en Python para la gestión de inventario de productos, permitiendo controlar existencias, registrar movimientos (entradas y salidas), generar reportes y almacenar la información de manera persistente.
El sistema debe simular un entorno real de control de inventario, aplicando lógica de programación, estructuras de datos, validaciones y manejo de errores.
"""
import json 

productos = {}

import os 

def registrar_producto():
    print("\n--- REGISTRAR NUEVO PRODUCTO ---")
   
    while True: 
        id_producto = input("Ingrese el ID único del producto: ").strip() 
        if not id_producto: 
            print("Error: El ID del producto no puede estar vacío.")
            continue
        elif not id_producto.isnumeric(): 
            print("Error: El ID del producto debe ser un número.") 
            continue    
        elif id_producto in productos:
            print("Error: El ID del producto ya existe. Por favor, ingrese un ID único.")
            continue
        else: break    
   
    while True: 
        nombre = input("Ingrese el nombre del producto: ").strip()
        
        if not nombre:
            print("Error: El nombre del producto no puede estar vacío.")
            continue
        else: 
            break

    while True:
        try:
            precio = float(input("Ingrese el precio del producto: "))  
            if precio < 0:
                print("Error: El precio no puede ser negativo.")
                continue
            break
        except ValueError:
            print("Error: El precio debe ser un número válido.")

    while True:
        try:
            stock = int(input("Ingrese el stock inicial: "))
            if stock < 0:
                print("Error: El stock no puede ser negativo.")
                continue
            break
        except ValueError:
            print("Error: El stock debe ser un número válido.")
    
    productos[id_producto] = { 
        "nombre": nombre,
        "precio": precio,
        "stock": stock
    }
    print(f"¡Producto '{nombre}' registrado con éxito!")
    guardar_datos()


def mostrar_productos(): 
    print("\n--- LISTA DE PRODUCTOS ---")
    if not productos:
        print("No hay productos registrados.")
        return
    
    for id_producto, info in productos.items():  
        print(f"ID: {id_producto} | Nombre: {info['nombre']} | Precio: ${info['precio']:.2f} | Stock: {info['stock']} | Valor Total: ${info['precio'] * info['stock']:.2f}")  
        if info['stock'] <= 5:
            print(f"¡Atención! El producto '{info['nombre']}' está por agotarse, hay {info['stock']} unidades restantes.")

def entrada_producto(): 
    print("\n--- ENTRADA DE PRODUCTO ---")
    while True:
        id_producto = input("Ingrese el ID del producto a ingresar: ").strip()
        if not id_producto.isnumeric():
            print("Error: El ID del producto debe ser un número.")
            continue
        elif  id_producto not in productos:
            print("Error: El producto no existe.")
            continue
        else: break
        
    while True:
        try:
            cantidad = int(input("Ingrese la cantidad a ingresar: "))
            if cantidad <= 0:
                print("Error: La cantidad debe ser un número positivo.")
                continue
            else:
                productos[id_producto]['stock'] += cantidad
                print(f"¡Entrada registrada! Nuevo stock de '{productos[id_producto]['nombre']}': {productos[id_producto]['stock']}")
                guardar_datos()
                break
        except ValueError:
            print("Error: Por favor, ingrese un número entero válido.")
        
def salida_producto(): 
    print("\n--- SALIDA DE PRODUCTO ---")
    while True:
        id_producto = input("Ingrese el ID del producto a retirar: ").strip()
        if not id_producto.isnumeric():
            print("Error: El ID del producto debe ser un número.")
            continue
        elif  id_producto not in productos:
            print("Error: El producto no existe.")
            continue
        else: break
    while True:
        try:
            cantidad = int(input("Ingrese la cantidad a retirar: "))
            if cantidad <= 0:
                print("Error: La cantidad debe ser un número positivo.")
                continue
            elif productos[id_producto]['stock'] < cantidad:
                print(f"Error: Stock insuficiente. Stock actual de '{productos[id_producto]['nombre']}': {productos[id_producto]['stock']}")
                continue
            else:
                productos[id_producto]['stock'] -= cantidad
                print(f"¡Salida registrada! Nuevo stock de '{productos[id_producto]['nombre']}': {productos[id_producto]['stock']}")
                guardar_datos()
                break
        except ValueError:
            print("Error: Por favor, ingrese un número entero válido.")
            
def generar_reporte():
    print("\n--- REPORTE DE INVENTARIO ---")
    if not productos:
        print("No hay productos registrados.")
        return
    
    print(f"{'ID':<10} {'Nombre':<20} {'Precio':<10} {'Stock':<10} {'Valor Total':<15}")
    print("-" * 50)
    for id_producto, info in productos.items():
        print(f"{id_producto:<10} {info['nombre']:<20} ${info['precio']:<10.2f} {info['stock']:<10} ${info['precio'] * info['stock']:<15.2f}")

    total_valor = sum(info['precio'] * info['stock'] for info in productos.values())
    print("-" * 70)
    print(f"Valor total del inventario: ${total_valor:.2f}")

def guardar_datos():
    try:
        directorio_actual = os.path.dirname(os.path.abspath(__file__))
        ruta = os.path.join(directorio_actual, "inventario.json")
        
        with open(ruta, "w", encoding="utf-8") as archivo:
            json.dump(productos, archivo, indent=4, ensure_ascii=False) 
        print(f"Datos guardados exitosamente en:\n{ruta}")   
    except NameError:
        print("Error: La variable 'productos' o el módulo 'json' no están definidos.") 
    except TypeError:
        print("Error: 'productos' contiene datos que JSON no puede leer (ej. Clases u Objetos).") 
    except Exception as e:
        print(f"Error inesperado: {e}")
        
def cargar_datos():
    try:
        directorio_actual = os.path.dirname(os.path.abspath(__file__))
        ruta = os.path.join(directorio_actual, "inventario.json")
        
        if os.path.exists(ruta):
            with open(ruta, "r", encoding="utf-8") as archivo:
                return json.load(archivo)
        else:
            print("No se encontró el archivo de datos. Se iniciará con un inventario vacío.")
            return {}
    except json.JSONDecodeError:
        print("Error: El archivo de datos está corrupto o no es un JSON válido. Se iniciará con un inventario vacío.")
        return {}
    except Exception as e:
        print(f"Error inesperado al cargar datos: {e}")
        return {}

def eliminar_datos():
    confirmacion = input("¿Está seguro de que desea eliminar todos los datos? Esta acción no se puede deshacer. (si/no): ").strip().lower()
    if confirmacion == 'si':
        productos.clear()
        guardar_datos()
        print("¡Todos los datos han sido eliminados!")
    elif confirmacion == 'no':
        print("Eliminación cancelada.")
    else:
        print("Opción no válida. Eliminación cancelada.")
        
productos = cargar_datos()

def mostrar_menu() -> None:  
    """Tenemos menu principal con opciones numeradas para el usuario."""
    print("\n  |-------------------------------------------------|")
    print("    |   SISTEMA DE GESTIÓN DE INVENTARIO           |")
    print("    |----------------------------------------------|")
    print("    |  1. Registrar producto                       |")
    print("    |  2. Mostrar productos                        |")
    print("    |  3. Entrada de producto (incrementar stock)  |")
    print("    |  4. Salida de producto (reducir stock)       |")
    print("    |  5. Generar reporte                          |")
    print("    |  6. Guardar datos                            |")
    print("    |  7. Eliminar datos                           |")
    print("    |  8. Salir                                    |")
    print("    |----------------------------------------------|")


while True: 
    mostrar_menu() 
    opcion = input("Seleccione una opción (1-8): ").strip()
    match opcion:
        case '1':
            print("Registrar producto")
            registrar_producto()
        case '2':
            print("Mostrar productos")
            mostrar_productos()
        case '3':
            print("Entrada de producto")
            entrada_producto()
        case '4':
            print("Salida de producto")
            salida_producto()
        case '5':
            generar_reporte()
            print("Generar reporte")
        case '6':
            guardar_datos()
            print("Guardando datos")
        case '7':
            print("Eliminando datos")
            eliminar_datos()
        case '8':
            print("Saliendo del sistema. ¡Hasta luego!")
            break
        case _:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 8.")

    input("\nPresione ENTER para continuar al menú principal...")
"""
Sistema de gestión de inventario conectado a SQL Server.
Permite controlar existencias, registrar movimientos (entradas y salidas), 
generar reportes y almacenar la información de manera persistente en BD.
"""
import pyodbc
import sys

# --- CONEXIÓN A LA BASE DE DATOS ---
try:
    conexion = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=localhost\\SQLEXPRESS;' 
        'DATABASE=InventarioEmprendedores;'
        'Trusted_Connection=yes;'
    )
    cursor = conexion.cursor()
    print("¡Conexión exitosa a SQL Server!")
except Exception as e:
    print(f"Error crítico al conectar a la base de datos: {e}")
    print("Asegúrate de que SQL Server esté ejecutándose y la base de datos exista.")
    sys.exit() 

# --- FUNCIONES DEL SISTEMA ---

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
        
        # Verificar en la base de datos si el ID ya existe
        cursor.execute("SELECT id_producto FROM Productos WHERE id_producto = ?", (id_producto,))
        if cursor.fetchone():
            print("Error: El ID del producto ya existe. Por favor, ingrese un ID único.")
            continue
        else: 
            break    
    
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
    
    # Insertar el nuevo producto en la base de datos
    try:
        cursor.execute(
            "INSERT INTO Productos (id_producto, nombre, precio, stock) VALUES (?, ?, ?, ?)",
            (int(id_producto), nombre, precio, stock)
        )
        conexion.commit() # Confirma el guardado
        print(f"¡Producto '{nombre}' registrado con éxito en la base de datos!")
    except Exception as e:
        print(f"Error al guardar el producto: {e}")


def mostrar_productos(): 
    print("\n--- LISTA DE PRODUCTOS ---")
    cursor.execute("SELECT id_producto, nombre, precio, stock FROM Productos")
    productos = cursor.fetchall()

    if not productos:
        print("No hay productos registrados en la base de datos.")
        return
    
    for prod in productos:  
        valor_total = prod.precio * prod.stock
        print(f"ID: {prod.id_producto} | Nombre: {prod.nombre} | Precio: ${prod.precio:.2f} | Stock: {prod.stock} | Valor Total: ${valor_total:.2f}")  
        if prod.stock <= 5:
            print(f"  -> ¡Atención! El producto '{prod.nombre}' está por agotarse, hay {prod.stock} unidades restantes.")

def entrada_producto(): 
    print("\n--- ENTRADA DE PRODUCTO ---")
    while True:
        id_producto = input("Ingrese el ID del producto a ingresar: ").strip()
        if not id_producto.isnumeric():
            print("Error: El ID del producto debe ser un número.")
            continue
        
        # Buscar el producto en la BD
        cursor.execute("SELECT nombre, stock FROM Productos WHERE id_producto = ?", (id_producto,))
        producto = cursor.fetchone()
        
        if not producto:
            print("Error: El producto no existe en la base de datos.")
            continue
        else: 
            break
        
    while True:
        try:
            cantidad = int(input("Ingrese la cantidad a ingresar: "))
            if cantidad <= 0:
                print("Error: La cantidad debe ser un número positivo.")
                continue
            else:
                nuevo_stock = producto.stock + cantidad
                cursor.execute("UPDATE Productos SET stock = ? WHERE id_producto = ?", (nuevo_stock, id_producto))
                conexion.commit()
                print(f"¡Entrada registrada! Nuevo stock de '{producto.nombre}': {nuevo_stock}")
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
        
        cursor.execute("SELECT nombre, stock FROM Productos WHERE id_producto = ?", (id_producto,))
        producto = cursor.fetchone()

        if not producto:
            print("Error: El producto no existe en la base de datos.")
            continue
        else: 
            break

    while True:
        try:
            cantidad = int(input("Ingrese la cantidad a retirar: "))
            if cantidad <= 0:
                print("Error: La cantidad debe ser un número positivo.")
                continue
            elif producto.stock < cantidad:
                print(f"Error: Stock insuficiente. Stock actual de '{producto.nombre}': {producto.stock}")
                continue
            else:
                nuevo_stock = producto.stock - cantidad
                cursor.execute("UPDATE Productos SET stock = ? WHERE id_producto = ?", (nuevo_stock, id_producto))
                conexion.commit()
                print(f"¡Salida registrada! Nuevo stock de '{producto.nombre}': {nuevo_stock}")
                break
        except ValueError:
            print("Error: Por favor, ingrese un número entero válido.")
            
def generar_reporte():
    print("\n--- REPORTE DE INVENTARIO ---")
    cursor.execute("SELECT id_producto, nombre, precio, stock FROM Productos")
    productos = cursor.fetchall()

    if not productos:
        print("No hay productos registrados.")
        return
    
    print(f"{'ID':<10} {'Nombre':<20} {'Precio':<10} {'Stock':<10} {'Valor Total':<15}")
    print("-" * 70)
    
    total_valor_inventario = 0
    for prod in productos:
        valor_total_producto = prod.precio * prod.stock
        total_valor_inventario += valor_total_producto
        print(f"{prod.id_producto:<10} {prod.nombre:<20} ${prod.precio:<10.2f} {prod.stock:<10} ${valor_total_producto:<15.2f}")

    print("-" * 70)
    print(f"Valor total del inventario: ${total_valor_inventario:.2f}")

def guardar_datos():
    # En SQL, los datos se guardan al instante con conexion.commit()
    # Esta función se mantiene para no romper el menú, pero solo informa al usuario.
    print("Nota: El sistema está conectado a SQL Server.")
    print("Los datos se guardan automáticamente en la base de datos en tiempo real.")

def eliminar_datos():
    confirmacion = input("¿Está seguro de que desea eliminar TODOS los productos de la base de datos? (si/no): ").strip().lower()
    if confirmacion == 'si':
        try:
            cursor.execute("DELETE FROM Productos")
            conexion.commit()
            print("¡Todos los datos han sido eliminados de la base de datos!")
        except Exception as e:
            print(f"Error al eliminar los datos: {e}")
    elif confirmacion == 'no':
        print("Eliminación cancelada.")
    else:
        print("Opción no válida. Eliminación cancelada.")

def mostrar_menu() -> None:  
    """Tenemos menu principal con opciones numeradas para el usuario."""
    print("\n  |-------------------------------------------------|")
    print("    |   SISTEMA DE GESTIÓN DE INVENTARIO (SQL)         |")
    print("    |----------------------------------------------|")
    print("    |  1. Registrar producto                       |")
    print("    |  2. Mostrar productos                        |")
    print("    |  3. Entrada de producto (incrementar stock)  |")
    print("    |  4. Salida de producto (reducir stock)       |")
    print("    |  5. Generar reporte                          |")
    print("    |  6. Guardar datos (Automático en SQL)        |")
    print("    |  7. Eliminar todos los datos                 |")
    print("    |  8. Salir                                    |")
    print("    |----------------------------------------------|")

# --- BUCLE PRINCIPAL ---
while True: 
    mostrar_menu() 
    opcion = input("Seleccione una opción (1-8): ").strip()
    match opcion:
        case '1':
            registrar_producto()
        case '2':
            mostrar_productos()
        case '3':
            entrada_producto()
        case '4':
            salida_producto()
        case '5':
            generar_reporte()
        case '6':
            guardar_datos()
        case '7':
            eliminar_datos()
        case '8':
            print("Saliendo del sistema. ¡Hasta luego!")
            # Cerrar conexión limpiamente al salir
            cursor.close()
            conexion.close()
            break
        case _:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 8.")

    input("\nPresione ENTER para continuar al menú principal...")
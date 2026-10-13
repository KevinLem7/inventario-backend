# Sistema de Gestión de Inventario

## Descripción del Proyecto

Sistema integral de gestión de inventario desarrollado en Python que permite controlar existencias de productos, registrar movimientos (entradas y salidas), generar reportes y almacenar la información de manera persistente. El sistema simula un entorno real de control de inventario, aplicando lógica de programación, estructuras de datos, validaciones y manejo de errores.

---

## Características Principales

- **Registrar Productos**: Agregar nuevos productos con ID único, nombre, precio y stock inicial
- **Mostrar Productos**: Visualizar lista completa de productos con detalles actualizados
- **Entrada de Productos**: Incrementar el stock de productos existentes
- **Salida de Productos**: Reducir el stock con validaciones de disponibilidad
- **Generar Reportes**: Crear reportes detallados del inventario con valor total
- **Guardar Datos**: Persistencia de información en formato JSON
- **Eliminar Datos**: Limpiar completamente el inventario (con confirmación)
- **Alertas de Stock**: Notificaciones cuando el stock está bajo (≤5 unidades)
- **Menú Interactivo**: Interfaz de usuario intuitiva y fácil de usar

---

## Requisitos del Sistema

### Software Requerido
- **Python**: 3.10 o superior (para soporte de `match-case`)
- **Sistema Operativo**: Windows, macOS o Linux
- **Terminal**: CMD, PowerShell, Bash o similar

### Dependencias
- Librerías estándar de Python (sin instalación adicional necesaria):
  - `json` - Para manejo de archivos JSON
  - `os` - Para operaciones del sistema de archivos

---

## Instalación y Configuración

### Paso 1: Descargar o Clonar el Proyecto
```bash
# Si está en un repositorio Git
git clone <url-del-repositorio>
cd inventario
```

### Paso 2: Verificar la Instalación de Python
```bash
python --version
```
**Resultado esperado**: Python 3.10 o superior

### Paso 3: Ejecutar la Aplicación
```bash
python inventario.py
```

---

## Instrucciones de Uso

### Menú Principal
Al ejecutar el programa, se mostrará el siguiente menú:

```
  |-------------------------------------------------|
    |   SISTEMA DE GESTIÓN DE INVENTARIO           |
    |----------------------------------------------|
    |  1. Registrar producto                       |
    |  2. Mostrar productos                        |
    |  3. Entrada de producto (incrementar stock)  |
    |  4. Salida de producto (reducir stock)       |
    |  5. Generar reporte                          |
    |  6. Guardar datos                            |
    |  7. Eliminar datos                           |
    |  8. Salir                                    |
    |----------------------------------------------|
```

### Descripción de Funciones

#### 1. Registrar Producto
- Solicita ID único del producto (debe ser numérico)
- Solicita nombre del producto (no puede estar vacío)
- Solicita precio (número positivo)
- Solicita stock inicial (número no negativo)
- Guarda automáticamente los datos

**Validaciones:**
- ID debe ser número y único
- Nombre no puede estar vacío
- Precio no puede ser negativo
- Stock no puede ser negativo

#### 2. Mostrar Productos
- Visualiza lista completa de productos con:
  - ID del producto
  - Nombre
  - Precio unitario
  - Stock disponible
  - Valor total (precio × stock)
- Muestra alertas si el stock está bajo (≤5 unidades)

#### 3. Entrada de Producto
- Incrementa el stock de un producto existente
- Solicita ID del producto a ingresar
- Solicita cantidad a agregar (debe ser positiva)
- Muestra nuevo stock actualizado

**Validaciones:**
- El producto debe existir
- La cantidad debe ser positiva

#### 4. Salida de Producto
- Reduce el stock de un producto existente
- Solicita ID del producto a retirar
- Solicita cantidad a retirar (debe ser positiva y disponible)
- Muestra nuevo stock actualizado

**Validaciones:**
- El producto debe existir
- La cantidad debe ser positiva
- No puede haber stock insuficiente

#### 5. Generar Reporte
- Crea un reporte formatado en tabla con:
  - ID
  - Nombre
  - Precio
  - Stock
  - Valor Total
- Calcula y muestra el valor total del inventario

#### 6. Guardar Datos
- Guarda toda la información en archivo `inventario.json`
- Se ejecuta automáticamente al registrar, entrada y salida de productos
- Permite guardar manualmente en cualquier momento

#### 7. Eliminar Datos
- Solicita confirmación antes de eliminar (escribe "si" o "no")
- Elimina todos los productos del inventario
- Guarda los cambios en `inventario.json`

#### 8. Salir
- Cierra la aplicación de forma segura
- Los datos permanecen guardados

---

## Estructura del Proyecto

```
inventario/
├── inventario.py          # Archivo principal de la aplicación
├── inventario.json        # Base de datos (se genera automáticamente)
└── README.md              # Este archivo de documentación
```

### Archivo `inventario.json`
Almacena los productos en formato JSON. Ejemplo:

```json
{
    "101": {
        "nombre": "Laptop",
        "precio": 999.99,
        "stock": 10
    },
    "102": {
        "nombre": "Mouse",
        "precio": 25.50,
        "stock": 50
    }
}
```

---

## Estructura de Datos

### Diccionario de Productos
Cada producto se almacena como:

```python
{
    "id_producto": {
        "nombre": str,      # Nombre del producto
        "precio": float,    # Precio unitario
        "stock": int        # Cantidad disponible
    }
}
```

---

## Manejo de Errores

El sistema incluye validaciones exhaustivas:

| Error | Descripción | Solución |
|-------|-------------|----------|
| ID vacío | El ID no puede estar vacío | Ingrese un ID numérico válido |
| ID no numérico | El ID debe ser número | Use solo dígitos (0-9) |
| ID duplicado | El ID ya existe en el sistema | Ingrese un ID único diferente |
| Nombre vacío | El nombre no puede estar vacío | Ingrese el nombre del producto |
| Precio inválido | El precio no es un número válido | Ingrese un número (ej: 99.99) |
| Precio negativo | El precio no puede ser negativo | Ingrese un valor positivo |
| Stock inválido | El stock no es un número entero válido | Ingrese un número entero |
| Stock negativo | El stock no puede ser negativo | Ingrese un valor no negativo |
| Producto no existe | El ID del producto no existe | Verifique el ID e intente de nuevo |
| Stock insuficiente | No hay suficiente stock para la salida | Reduzca la cantidad requerida |
| JSON corrupto | El archivo de datos está dañado | Se inicia con inventario vacío |

---

## Ejemplos de Uso

### Ejemplo 1: Registrar un Producto
```
Seleccione una opción (1-8): 1
--- REGISTRAR NUEVO PRODUCTO ---
Ingrese el ID único del producto: 101
Ingrese el nombre del producto: Laptop Dell
Ingrese el precio del producto: 899.99
Ingrese el stock inicial: 15
¡Producto 'Laptop Dell' registrado con éxito!
```

### Ejemplo 2: Entrada de Producto
```
Seleccione una opción (1-8): 3
--- ENTRADA DE PRODUCTO ---
Ingrese el ID del producto a ingresar: 101
Ingrese la cantidad a ingresar: 5
¡Entrada registrada! Nuevo stock de 'Laptop Dell': 20
```

### Ejemplo 3: Ver Reporte
```
Seleccione una opción (1-8): 5
--- REPORTE DE INVENTARIO ---
ID         Nombre               Precio     Stock      Valor Total    
--------------------------------------------------
101        Laptop Dell          $899.99    20         $17,999.80     
--------------------------------------------------
Valor total del inventario: $17,999.80
```

---

## Consideraciones de Seguridad

- Los datos se guardan automáticamente
- Confirmación requerida para eliminar datos
- Validación exhaustiva de entrada de usuario
- Manejo seguro de excepciones
- Codificación UTF-8 para caracteres especiales

---

## Tecnologías Utilizadas

- **Lenguaje**: Python 3.10+
- **Paradigma**: Programación Estructurada/Imperativa
- **Almacenamiento**: JSON (formato de texto)
- **Control de Flujo**: Match-Case (Python 3.10+)
- **Manejo de Archivos**: módulo `os` y `json`

---

## Conceptos de Programación Aplicados

- Estructuras de datos (diccionarios, listas)
- Funciones y modularización
- Bucles (`while`, `for`)
- Sentencias condicionales (`match-case`, `if-elif`)
- Validación de entrada de usuario
- Manejo de excepciones (`try-except`)
- Persistencia de datos (JSON)
- Operaciones con archivos
- Interfaces de usuario en consola
- Cálculos matemáticos (suma, multiplicación)

---

## Notas Importantes

1. **Python 3.10+**: El proyecto utiliza `match-case` que requiere Python 3.10 o superior
2. **Primero ejecute**: Si es la primera vez, el sistema creará el archivo `inventario.json` automáticamente
3. **Datos persistentes**: Los datos se guardan en `inventario.json` y se cargan al iniciar
4. **Validaciones**: Todas las entradas de usuario son validadas
5. **Caracteres especiales**: El sistema soporta caracteres acentuados (UTF-8)

---

## Resolución de Problemas

### Problema: "No module named json"
**Solución**: `json` es una librería estándar. Verifica que Python esté instalado correctamente.

### Problema: Archivo `inventario.json` no se crea
**Solución**: Asegúrate de tener permisos de escritura en la carpeta del proyecto.

### Problema: Error "invalid syntax" con `match-case`
**Solución**: Verifica que estés usando Python 3.10 o superior con `python --version`.

### Problema: Datos no se guardan
**Solución**: Verifica que el archivo `inventario.json` no esté abierto en otro programa.

---

## Información del Proyecto

- **Tipo**: Sistema de Gestión de Inventario
- **Versión**: 1.0
- **Estado**: Completo y Funcional
- **Última Actualización**: Junio 2026
- **Autor**: [Tu Nombre Aquí]
- **Institución**: DLP-ITCA

---

## Licencia

Este proyecto es de código abierto y está disponible para propósitos educativos.

---

## Contribuciones

Las sugerencias y mejoras son bienvenidas. Siéntete libre de hacer fork del proyecto y enviar pull requests.

---

Para más información o soporte, consulte la documentación técnica incluida en el proyecto.

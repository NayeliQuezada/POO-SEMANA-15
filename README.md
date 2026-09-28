# SABORES DE MI TIERRA - Sistema de Gestión de Restaurante

## 👩‍💻 Autora

**Nayeli Quezada**

Estudiante de Tecnologías de la Información  
Universidad Estatal Amazónica (UEA)

---

## 📌 Descripción del proyecto

**SABORES DE MI TIERRA** es una aplicación de escritorio desarrollada en Python para la gestión básica de un restaurante.

El sistema permite administrar usuarios, productos y ventas mediante una interfaz gráfica desarrollada con Tkinter.

El proyecto fue desarrollado aplicando conceptos de Programación Orientada a Objetos (POO), manejo de archivos JSON, eventos y separación de responsabilidades entre modelos, servicios e interfaz gráfica.

---

## 🎯 Objetivo

Desarrollar una aplicación de escritorio que permita gestionar información de un restaurante utilizando Programación Orientada a Objetos, persistencia de datos mediante archivos JSON e interacción gráfica con Tkinter.

---

## 🛠️ Tecnologías utilizadas

- Python
- Tkinter
- Programación Orientada a Objetos (POO)
- Archivos JSON
- Visual Studio Code
- Git
- GitHub

---

## 📂 Estructura del proyecto

```text
restaurante_app15/
│
├── assets/
│   ├── icono.png
│   └── logo.png
│
├── datos/
│   ├── productos.json
│   ├── usuarios.json
│   └── ventas.json
│
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   ├── usuario.py
│   └── venta.py
│
├── servicios/
│   ├── __init__.py
│   ├── archivo_servicio.py
│   └── restaurante_servicio.py
│
├── ui/
│   ├── __init__.py
│   ├── login_view.py
│   └── main_view.py
│
├── main.py
└── README.md
⚙️ Funcionalidades
🔐 Inicio de sesión

El sistema cuenta con una pantalla de inicio de sesión que permite validar las credenciales de los usuarios registrados.

👤 Gestión de usuarios

El sistema permite:

Registrar usuarios.
Consultar usuarios.
Actualizar usuarios.
Eliminar usuarios.
Visualizar identificación, nombre y usuario.
Guardar los cambios en usuarios.json.
🍔 Gestión de productos

El sistema permite:

Registrar productos.
Consultar productos.
Actualizar productos.
Eliminar productos.
Manejar código, nombre, precio, categoría y stock.
Guardar los cambios en productos.json.
🧾 Gestión de ventas

El sistema permite:

Seleccionar un usuario.
Seleccionar un producto.
Registrar una venta.
Mostrar la identificación del usuario.
Mostrar el producto seleccionado.
Registrar la fecha de la venta.
Guardar las ventas en ventas.json.
🔄 Flujo de funcionamiento

El proyecto aplica el siguiente flujo:

Acción del usuario
       ↓
    command=
       ↓
Método de la interfaz
       ↓
RestauranteServicio
       ↓
ArchivoServicio
       ↓
   Archivo JSON
       ↓
Respuesta visual al usuario

Este flujo permite separar la interfaz gráfica de la lógica del sistema y del almacenamiento de los datos.

🧩 Programación Orientada a Objetos

El proyecto utiliza diferentes clases para representar y organizar la información.

Clase Producto

Representa los productos del restaurante.

Sus principales atributos son:

Código
Nombre
Precio
Categoría
Stock
Clase Usuario

Representa a los usuarios del sistema.

Sus principales atributos son:

Identificación
Nombre
Usuario
Contraseña
Clase Venta

Representa una venta realizada.

Sus principales datos son:

Identificación del usuario
Código del producto
Fecha
Clase ArchivoServicio

Se encarga de leer y escribir información utilizando archivos JSON.

Clase RestauranteServicio

Contiene la lógica principal para:

Usuarios
Productos
Ventas
Validación de acceso
Persistencia de información
Clases de interfaz

La interfaz gráfica se divide principalmente en:

LoginView
MainView

Estas clases permiten interactuar con el sistema mediante Tkinter.

💾 Persistencia de datos

La información se almacena localmente mediante archivos JSON.

usuarios.json

Almacena los usuarios registrados.

productos.json

Almacena los productos disponibles.

ventas.json

Almacena las ventas realizadas.

Esto permite conservar la información aunque la aplicación sea cerrada.

▶️ Ejecución del proyecto

Para ejecutar la aplicación se necesita tener instalado Python.

Desde la terminal de Visual Studio Code, ubicándose dentro de la carpeta del proyecto, ejecutar:

python main.py

También puede utilizarse:

py main.py
🔑 Inicio de sesión

Para ingresar al sistema se deben utilizar las credenciales registradas en:

datos/usuarios.json
🖥️ Interfaz

La aplicación cuenta con:

Pantalla de inicio de sesión.
Logo del restaurante.
Menú lateral.
Panel de inicio.
Gestión de usuarios.
Gestión de productos.
Gestión de ventas.
Barra de estado.
Mensajes de confirmación y error.
📚 Actividad académica

Proyecto desarrollado como parte de la actividad de Programación Orientada a Objetos - Semana 15.

El proyecto integra los conocimientos adquiridos sobre:

Clases y objetos.
Encapsulamiento.
Métodos.
Manejo de archivos.
JSON.
Interfaces gráficas.
Eventos.
Persistencia de datos.
Git y GitHub.
👩‍💻 Autora

Nayeli Quezada

Tecnologías de la Información
Universidad Estatal Amazónica

Proyecto: SABORES DE MI TIERRA
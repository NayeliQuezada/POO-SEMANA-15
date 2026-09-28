import tkinter as tk
from tkinter import ttk, messagebox
from pathlib import Path
from datetime import datetime


class MainView(tk.Frame):

    def __init__(
        self,
        master,
        restaurante_servicio,
        usuario_actual,
        al_cerrar_sesion
    ):

        super().__init__(
            master,
            bg="#f7fafc"
        )

        self.restaurante_servicio = restaurante_servicio
        self.usuario_actual = usuario_actual
        self.al_cerrar_sesion = al_cerrar_sesion

        # =====================================================
        # COLORES
        # =====================================================

        self.color_fondo = "#f7fafc"
        self.color_panel = "#d59e9e"

        # PANEL LATERAL CLARO
        self.color_encabezado = "#a0c0e7"

        self.color_texto = "#4E647E"

        self.color_registrar = "#16a34a"
        self.color_consultar = "#2563eb"
        self.color_actualizar = "#f59e0b"
        self.color_eliminar = "#dc2626"
        self.color_limpiar = "#64748b"
        self.color_venta = "#7c3aed"

        # =====================================================
        # VARIABLES
        # =====================================================

        self.contenido = None
        self.barra_estado = None

        # =====================================================
        # PRODUCTOS
        # =====================================================

        self.producto_codigo_entry = None
        self.producto_nombre_entry = None
        self.producto_precio_entry = None
        self.producto_categoria_entry = None
        self.producto_stock_entry = None
        self.tabla_productos = None

        # =====================================================
        # USUARIOS
        # =====================================================

        self.usuario_identificacion_entry = None
        self.usuario_nombre_entry = None
        self.usuario_usuario_entry = None
        self.usuario_contrasena_entry = None
        self.tabla_usuarios = None

        # =====================================================
        # VENTAS
        # =====================================================

        self.venta_usuario_combo = None
        self.venta_producto_combo = None
        self.tabla_ventas = None
        self.mensaje_venta = None

        self.usuarios_venta = {}
        self.productos_venta = {}

        # =====================================================
        # LOGO
        # =====================================================

        self.logo = None

        self.definir_estilos()
        self.construir_interfaz()

    # =========================================================
    # ESTILOS
    # =========================================================

    def definir_estilos(self):

        estilo = ttk.Style()

        try:
            estilo.theme_use("clam")
        except tk.TclError:
            pass

        estilo.configure(
            "Tabla.Treeview",
            background="#ffffff",
            foreground="#243447",
            rowheight=30,
            fieldbackground="#ffffff",
            font=("Arial", 9)
        )

        estilo.configure(
            "Tabla.Treeview.Heading",
            background="#1f2a44",
            foreground="#ffffff",
            font=("Arial", 9, "bold"),
            padding=8
        )

        estilo.map(
            "Tabla.Treeview",
            background=[
                ("selected", "#dbeafe")
            ],
            foreground=[
                ("selected", "#1f2a44")
            ]
        )

    # =========================================================
    # CARGAR LOGO
    # =========================================================

    def cargar_logo(self):

        ruta_base = Path(__file__).resolve().parent.parent

        rutas_posibles = [
            ruta_base / "assets" / "logo.png",
            ruta_base / "assets" / "logo" / "logo.png"
        ]

        for ruta_logo in rutas_posibles:

            if ruta_logo.exists():

                try:

                    logo_original = tk.PhotoImage(
                        file=str(ruta_logo)
                    )

                    ancho = logo_original.width()
                    alto = logo_original.height()

                    if ancho > 170 or alto > 90:

                        factor = max(
                            ancho // 170,
                            alto // 90,
                            1
                        )

                        self.logo = logo_original.subsample(
                            factor,
                            factor
                        )

                    else:

                        self.logo = logo_original

                    return self.logo

                except Exception:

                    return None

        return None

    # =========================================================
    # INTERFAZ PRINCIPAL
    # =========================================================

    def construir_interfaz(self):

        # =====================================================
        # SIDEBAR
        # =====================================================

        self.sidebar = tk.Frame(
            self,
            bg=self.color_encabezado,
            width=210
        )

        self.sidebar.pack(
            side="left",
            fill="y"
        )

        self.sidebar.pack_propagate(False)

        # =====================================================
        # LOGO
        # =====================================================

        logo = self.cargar_logo()

        if logo is not None:

            tk.Label(
                self.sidebar,
                image=logo,
                bg=self.color_encabezado
            ).pack(
                pady=(18, 5)
            )

        # =====================================================
        # NOMBRE DEL RESTAURANTE
        # =====================================================

        tk.Label(
            self.sidebar,
            text="SABORES",
            bg=self.color_encabezado,
            fg="#243447",
            font=("Arial", 21, "bold")
        ).pack(
            pady=(5, 0)
        )

        tk.Label(
            self.sidebar,
            text="DE MI TIERRA",
            bg=self.color_encabezado,
            fg="#243447",
            font=("Arial", 13, "bold")
        ).pack(
            pady=(0, 5)
        )

        tk.Label(
            self.sidebar,
            text="RESTAURANTE",
            bg=self.color_encabezado,
            fg="#516173",
            font=("Arial", 9)
        ).pack(
            pady=(0, 25)
        )

        # =====================================================
        # MENÚ
        # =====================================================

        self.crear_boton_menu(
            "Inicio",
            self.mostrar_inicio
        )

        self.crear_boton_menu(
            "Usuarios",
            self.mostrar_usuarios
        )

        self.crear_boton_menu(
            "Productos",
            self.mostrar_productos
        )

        self.crear_boton_menu(
            "Ventas",
            self.mostrar_ventas
        )

        # ESPACIO

        tk.Frame(
            self.sidebar,
            bg=self.color_encabezado
        ).pack(
            fill="both",
            expand=True
        )

        # CERRAR SESIÓN

        self.crear_boton_menu(
            "Cerrar sesion",
            self.cerrar_sesion,
            color="#dc2626"
        )

        # =====================================================
        # ÁREA PRINCIPAL
        # =====================================================

        self.contenido = tk.Frame(
            self,
            bg=self.color_fondo
        )

        self.contenido.pack(
            side="left",
            fill="both",
            expand=True
        )

        # =====================================================
        # BARRA DE ESTADO
        # =====================================================

        self.barra_estado = tk.Label(
            self.contenido,
            text="",
            bg="#eef3f8",
            fg="#516173",
            font=("Arial", 9),
            anchor="w",
            padx=15,
            pady=7
        )

        self.barra_estado.pack(
            side="bottom",
            fill="x"
        )

        self.mostrar_inicio()

    # =========================================================
    # BOTÓN MENÚ
    # =========================================================

    def crear_boton_menu(
        self,
        texto,
        comando,
        color=None
    ):

        color_boton = (
            color
            if color is not None
            else self.color_encabezado
        )

        color_texto = (
            "#ffffff"
            if color is not None
            else "#243447"
        )

        boton = tk.Button(
            self.sidebar,
            text=texto,
            command=comando,
            bg=color_boton,
            fg=color_texto,
            activebackground="#c5d3e3",
            activeforeground="#243447",
            relief="flat",
            borderwidth=0,
            anchor="w",
            padx=25,
            pady=12,
            font=("Arial", 10, "bold"),
            cursor="hand2"
        )

        boton.pack(
            fill="x",
            padx=8,
            pady=2
        )

    # =========================================================
    # BOTÓN DE ACCIÓN
    # =========================================================

    def crear_boton_accion(
        self,
        padre,
        texto,
        comando,
        color,
        ancho=12
    ):

        boton = tk.Button(
            padre,
            text=texto,
            command=comando,
            bg=color,
            fg="#ffffff",
            activebackground=color,
            activeforeground="#ffffff",
            relief="flat",
            borderwidth=0,
            font=("Arial", 9, "bold"),
            padx=10,
            pady=7,
            width=ancho,
            cursor="hand2"
        )

        return boton

    # =========================================================
    # LIMPIAR CONTENIDO
    # =========================================================

    def limpiar_contenido(self):

        for widget in self.contenido.winfo_children():

            if widget != self.barra_estado:

                widget.destroy()

    # =========================================================
    # TÍTULO
    # =========================================================

    def crear_titulo_seccion(
        self,
        titulo,
        descripcion
    ):

        encabezado = tk.Frame(
            self.contenido,
            bg=self.color_panel
        )

        encabezado.pack(
            fill="x",
            padx=25,
            pady=(25, 10)
        )

        tk.Label(
            encabezado,
            text=titulo,
            bg=self.color_panel,
            fg=self.color_encabezado,
            font=("Arial", 20, "bold")
        ).pack(
            anchor="w",
            padx=20,
            pady=(15, 3)
        )

        tk.Label(
            encabezado,
            text=descripcion,
            bg=self.color_panel,
            fg="#516173",
            font=("Arial", 10)
        ).pack(
            anchor="w",
            padx=20,
            pady=(0, 15)
        )

    # =========================================================
    # INICIO
    # =========================================================

    def mostrar_inicio(self):

        self.limpiar_contenido()

        self.crear_titulo_seccion(
            "Bienvenida",
            "Panel principal del sistema de restaurante."
        )

        bienvenida = tk.Frame(
            self.contenido,
            bg=self.color_panel
        )

        bienvenida.pack(
            fill="x",
            padx=25,
            pady=10
        )

        tk.Label(
            bienvenida,
            text=f"Bienvenida, {self.usuario_actual.nombre}",
            bg=self.color_panel,
            fg=self.color_encabezado,
            font=("Arial", 17, "bold")
        ).pack(
            anchor="w",
            padx=20,
            pady=(20, 5)
        )

        tk.Label(
            bienvenida,
            text="Seleccione una opción del menú lateral para continuar.",
            bg=self.color_panel,
            fg="#516173",
            font=("Arial", 10)
        ).pack(
            anchor="w",
            padx=20,
            pady=(0, 20)
        )

        tarjetas = tk.Frame(
            self.contenido,
            bg=self.color_fondo
        )

        tarjetas.pack(
            fill="x",
            padx=25,
            pady=10
        )

        self.crear_tarjeta(
            tarjetas,
            "USUARIOS",
            self.restaurante_servicio.cantidad_usuarios(),
            "#e0f2fe",
            0
        )

        self.crear_tarjeta(
            tarjetas,
            "PRODUCTOS",
            self.restaurante_servicio.cantidad_productos(),
            "#dcfce7",
            1
        )

        self.crear_tarjeta(
            tarjetas,
            "VENTAS",
            self.restaurante_servicio.cantidad_ventas(),
            "#fef3c7",
            2
        )

        self.actualizar_barra_estado()

    # =========================================================
    # TARJETAS
    # =========================================================

    def crear_tarjeta(
        self,
        padre,
        titulo,
        cantidad,
        color,
        columna
    ):

        tarjeta = tk.Frame(
            padre,
            bg=color,
            padx=20,
            pady=18
        )

        tarjeta.grid(
            row=0,
            column=columna,
            padx=7,
            sticky="nsew"
        )

        padre.grid_columnconfigure(
            columna,
            weight=1
        )

        tk.Label(
            tarjeta,
            text=titulo,
            bg=color,
            fg=self.color_encabezado,
            font=("Arial", 10, "bold")
        ).pack()

        tk.Label(
            tarjeta,
            text=str(cantidad),
            bg=color,
            fg=self.color_encabezado,
            font=("Arial", 24, "bold")
        ).pack(
            pady=(5, 0)
        )

    # =========================================================
    # USUARIOS
    # =========================================================

    def mostrar_usuarios(self):

        self.limpiar_contenido()

        self.crear_titulo_seccion(
            "Usuarios",
            "Gestion de usuarios registrados en el sistema."
        )

        # =====================================================
        # FORMULARIO
        # =====================================================

        formulario = tk.Frame(
            self.contenido,
            bg=self.color_panel
        )

        formulario.pack(
            fill="x",
            padx=25,
            pady=10
        )

        # IDENTIFICACION

        tk.Label(
            formulario,
            text="Identificacion",
            bg=self.color_panel,
            fg=self.color_texto,
            font=("Arial", 9, "bold")
        ).grid(
            row=0,
            column=0,
            padx=10,
            pady=(15, 3),
            sticky="w"
        )

        self.usuario_identificacion_entry = tk.Entry(
            formulario,
            width=18,
            font=("Arial", 10)
        )

        self.usuario_identificacion_entry.grid(
            row=1,
            column=0,
            padx=10,
            pady=(0, 12)
        )

        # NOMBRE

        tk.Label(
            formulario,
            text="Nombre",
            bg=self.color_panel,
            fg=self.color_texto,
            font=("Arial", 9, "bold")
        ).grid(
            row=0,
            column=1,
            padx=10,
            pady=(15, 3),
            sticky="w"
        )

        self.usuario_nombre_entry = tk.Entry(
            formulario,
            width=25,
            font=("Arial", 10)
        )

        self.usuario_nombre_entry.grid(
            row=1,
            column=1,
            padx=10,
            pady=(0, 12)
        )

        # USUARIO

        tk.Label(
            formulario,
            text="Usuario",
            bg=self.color_panel,
            fg=self.color_texto,
            font=("Arial", 9, "bold")
        ).grid(
            row=0,
            column=2,
            padx=10,
            pady=(15, 3),
            sticky="w"
        )

        self.usuario_usuario_entry = tk.Entry(
            formulario,
            width=18,
            font=("Arial", 10)
        )

        self.usuario_usuario_entry.grid(
            row=1,
            column=2,
            padx=10,
            pady=(0, 12)
        )

        # CONTRASEÑA

        tk.Label(
            formulario,
            text="Contraseña",
            bg=self.color_panel,
            fg=self.color_texto,
            font=("Arial", 9, "bold")
        ).grid(
            row=0,
            column=3,
            padx=10,
            pady=(15, 3),
            sticky="w"
        )

        self.usuario_contrasena_entry = tk.Entry(
            formulario,
            width=18,
            font=("Arial", 10),
            show="*"
        )

        self.usuario_contrasena_entry.grid(
            row=1,
            column=3,
            padx=10,
            pady=(0, 12)
        )

        # =====================================================
        # BOTONES
        # =====================================================

        botones = tk.Frame(
            formulario,
            bg=self.color_panel
        )

        botones.grid(
            row=2,
            column=0,
            columnspan=4,
            padx=10,
            pady=(0, 15),
            sticky="w"
        )

        self.crear_boton_accion(
            botones,
            "Registrar",
            self.registrar_usuario,
            self.color_registrar
        ).pack(
            side="left",
            padx=3
        )

        self.crear_boton_accion(
            botones,
            "Consultar",
            self.cargar_usuario,
            self.color_consultar
        ).pack(
            side="left",
            padx=3
        )

        self.crear_boton_accion(
            botones,
            "Actualizar",
            self.actualizar_usuario,
            self.color_actualizar
        ).pack(
            side="left",
            padx=3
        )

        self.crear_boton_accion(
            botones,
            "Eliminar",
            self.eliminar_usuario,
            self.color_eliminar
        ).pack(
            side="left",
            padx=3
        )

        self.crear_boton_accion(
            botones,
            "Limpiar",
            self.limpiar_formulario_usuario,
            self.color_limpiar
        ).pack(
            side="left",
            padx=3
        )

        # =====================================================
        # TABLA
        # =====================================================

        self.tabla_usuarios = self.crear_tabla(
            (
                "identificacion",
                "nombre",
                "usuario"
            )
        )

        self.tabla_usuarios.heading(
            "identificacion",
            text="Identificacion"
        )

        self.tabla_usuarios.heading(
            "nombre",
            text="Nombre"
        )

        self.tabla_usuarios.heading(
            "usuario",
            text="Usuario"
        )

        self.tabla_usuarios.column(
            "identificacion",
            width=150
        )

        self.tabla_usuarios.column(
            "nombre",
            width=250
        )

        self.tabla_usuarios.column(
            "usuario",
            width=200
        )

        self.cargar_tabla_usuarios()

        self.actualizar_barra_estado()

    # =========================================================
    # CARGAR TABLA DE USUARIOS
    # =========================================================

    def cargar_tabla_usuarios(self):

        if self.tabla_usuarios is None:
            return

        self.limpiar_tabla(
            self.tabla_usuarios
        )

        for usuario in (
            self.restaurante_servicio.listar_usuarios()
        ):

            self.tabla_usuarios.insert(
                "",
                "end",
                values=(
                    usuario.identificacion,
                    usuario.nombre,
                    usuario.usuario
                )
            )

    # =========================================================
    # REGISTRAR USUARIO
    # =========================================================

    def registrar_usuario(self):

        try:

            identificacion = (
                self.usuario_identificacion_entry
                .get()
                .strip()
            )

            nombre = (
                self.usuario_nombre_entry
                .get()
                .strip()
            )

            usuario = (
                self.usuario_usuario_entry
                .get()
                .strip()
            )

            contrasena = (
                self.usuario_contrasena_entry
                .get()
                .strip()
            )

            self.restaurante_servicio.registrar_usuario(
                identificacion,
                nombre,
                usuario,
                contrasena
            )

            messagebox.showinfo(
                "Usuario",
                "Usuario registrado correctamente."
            )

            self.cargar_tabla_usuarios()

            self.limpiar_formulario_usuario()

            self.actualizar_barra_estado()

        except ValueError as error:

            messagebox.showerror(
                "Error",
                str(error)
            )

    # =========================================================
    # CONSULTAR USUARIO
    # =========================================================

    def cargar_usuario(self):

        if self.tabla_usuarios is None:
            return

        seleccion = self.tabla_usuarios.selection()

        if not seleccion:

            messagebox.showwarning(
                "Usuario",
                "Seleccione un usuario de la tabla."
            )

            return

        valores = self.tabla_usuarios.item(
            seleccion[0],
            "values"
        )

        self.limpiar_formulario_usuario()

        self.usuario_identificacion_entry.insert(
            0,
            valores[0]
        )

        self.usuario_nombre_entry.insert(
            0,
            valores[1]
        )

        self.usuario_usuario_entry.insert(
            0,
            valores[2]
        )

        usuario = (
            self.restaurante_servicio
            .buscar_usuario_por_identificacion(
                valores[0]
            )
        )

        if usuario is not None:

            self.usuario_contrasena_entry.insert(
                0,
                usuario.contrasena
            )

    # =========================================================
    # ACTUALIZAR USUARIO
    # =========================================================

    def actualizar_usuario(self):

        try:

            identificacion = (
                self.usuario_identificacion_entry
                .get()
                .strip()
            )

            nombre = (
                self.usuario_nombre_entry
                .get()
                .strip()
            )

            usuario = (
                self.usuario_usuario_entry
                .get()
                .strip()
            )

            contrasena = (
                self.usuario_contrasena_entry
                .get()
                .strip()
            )

            self.restaurante_servicio.actualizar_usuario(
                identificacion,
                nombre,
                usuario,
                contrasena
            )

            messagebox.showinfo(
                "Usuario",
                "Usuario actualizado correctamente."
            )

            self.cargar_tabla_usuarios()

            self.limpiar_formulario_usuario()

            self.actualizar_barra_estado()

        except ValueError as error:

            messagebox.showerror(
                "Error",
                str(error)
            )

    # =========================================================
    # ELIMINAR USUARIO
    # =========================================================

    def eliminar_usuario(self):

        try:

            identificacion = (
                self.usuario_identificacion_entry
                .get()
                .strip()
            )

            if not identificacion:

                messagebox.showwarning(
                    "Usuario",
                    "Ingrese o seleccione una identificacion."
                )

                return

            usuario = (
                self.restaurante_servicio
                .buscar_usuario_por_identificacion(
                    identificacion
                )
            )

            if usuario is None:

                raise ValueError(
                    "No existe un usuario con esa identificacion."
                )

            confirmar = messagebox.askyesno(
                "Eliminar usuario",
                f"¿Desea eliminar al usuario {usuario.nombre}?"
            )

            if not confirmar:
                return

            self.restaurante_servicio.eliminar_usuario(
                identificacion
            )

            messagebox.showinfo(
                "Usuario",
                "Usuario eliminado correctamente."
            )

            self.cargar_tabla_usuarios()

            self.limpiar_formulario_usuario()

            self.actualizar_barra_estado()

        except ValueError as error:

            messagebox.showerror(
                "Error",
                str(error)
            )

    # =========================================================
    # LIMPIAR FORMULARIO USUARIO
    # =========================================================

    def limpiar_formulario_usuario(self):

        entradas = [
            self.usuario_identificacion_entry,
            self.usuario_nombre_entry,
            self.usuario_usuario_entry,
            self.usuario_contrasena_entry
        ]

        for entrada in entradas:

            if entrada is not None:

                entrada.delete(
                    0,
                    tk.END
                )

    # =========================================================
    # PRODUCTOS
    # =========================================================

    def mostrar_productos(self):

        self.limpiar_contenido()

        self.crear_titulo_seccion(
            "Productos",
            "Gestion de productos disponibles en el restaurante."
        )

        formulario = tk.Frame(
            self.contenido,
            bg=self.color_panel
        )

        formulario.pack(
            fill="x",
            padx=25,
            pady=10
        )

        # CÓDIGO

        tk.Label(
            formulario,
            text="Código",
            bg=self.color_panel,
            fg=self.color_texto,
            font=("Arial", 9, "bold")
        ).grid(
            row=0,
            column=0,
            padx=10,
            pady=(15, 3),
            sticky="w"
        )

        self.producto_codigo_entry = tk.Entry(
            formulario,
            width=18,
            font=("Arial", 10)
        )

        self.producto_codigo_entry.grid(
            row=1,
            column=0,
            padx=10,
            pady=(0, 10)
        )

        # NOMBRE

        tk.Label(
            formulario,
            text="Nombre",
            bg=self.color_panel,
            fg=self.color_texto,
            font=("Arial", 9, "bold")
        ).grid(
            row=0,
            column=1,
            padx=10,
            pady=(15, 3),
            sticky="w"
        )

        self.producto_nombre_entry = tk.Entry(
            formulario,
            width=25,
            font=("Arial", 10)
        )

        self.producto_nombre_entry.grid(
            row=1,
            column=1,
            padx=10,
            pady=(0, 10)
        )

        # PRECIO

        tk.Label(
            formulario,
            text="Precio",
            bg=self.color_panel,
            fg=self.color_texto,
            font=("Arial", 9, "bold")
        ).grid(
            row=0,
            column=2,
            padx=10,
            pady=(15, 3),
            sticky="w"
        )

        self.producto_precio_entry = tk.Entry(
            formulario,
            width=15,
            font=("Arial", 10)
        )

        self.producto_precio_entry.grid(
            row=1,
            column=2,
            padx=10,
            pady=(0, 10)
        )

        # CATEGORÍA

        tk.Label(
            formulario,
            text="Categoría",
            bg=self.color_panel,
            fg=self.color_texto,
            font=("Arial", 9, "bold")
        ).grid(
            row=2,
            column=0,
            padx=10,
            pady=(5, 3),
            sticky="w"
        )

        self.producto_categoria_entry = tk.Entry(
            formulario,
            width=18,
            font=("Arial", 10)
        )

        self.producto_categoria_entry.grid(
            row=3,
            column=0,
            padx=10,
            pady=(0, 15)
        )

        # STOCK

        tk.Label(
            formulario,
            text="Stock",
            bg=self.color_panel,
            fg=self.color_texto,
            font=("Arial", 9, "bold")
        ).grid(
            row=2,
            column=1,
            padx=10,
            pady=(5, 3),
            sticky="w"
        )

        self.producto_stock_entry = tk.Entry(
            formulario,
            width=15,
            font=("Arial", 10)
        )

        self.producto_stock_entry.grid(
            row=3,
            column=1,
            padx=10,
            pady=(0, 15)
        )

        # =====================================================
        # BOTONES PRODUCTOS
        # =====================================================

        botones = tk.Frame(
            formulario,
            bg=self.color_panel
        )

        botones.grid(
            row=3,
            column=2,
            padx=10,
            pady=(0, 15)
        )

        self.crear_boton_accion(
            botones,
            "Registrar",
            self.registrar_producto,
            self.color_registrar
        ).pack(
            side="left",
            padx=3
        )

        self.crear_boton_accion(
            botones,
            "Consultar",
            self.cargar_producto,
            self.color_consultar
        ).pack(
            side="left",
            padx=3
        )

        self.crear_boton_accion(
            botones,
            "Actualizar",
            self.actualizar_producto,
            self.color_actualizar
        ).pack(
            side="left",
            padx=3
        )

        self.crear_boton_accion(
            botones,
            "Eliminar",
            self.eliminar_producto,
            self.color_eliminar
        ).pack(
            side="left",
            padx=3
        )

        self.crear_boton_accion(
            botones,
            "Limpiar",
            self.limpiar_formulario_producto,
            self.color_limpiar
        ).pack(
            side="left",
            padx=3
        )

        # =====================================================
        # TABLA PRODUCTOS
        # =====================================================

        self.tabla_productos = self.crear_tabla(
            (
                "codigo",
                "nombre",
                "precio",
                "categoria",
                "stock"
            )
        )

        encabezados = {
            "codigo": "Código",
            "nombre": "Nombre",
            "precio": "Precio",
            "categoria": "Categoría",
            "stock": "Stock"
        }

        for columna in encabezados:

            self.tabla_productos.heading(
                columna,
                text=encabezados[columna]
            )

        self.tabla_productos.column(
            "codigo",
            width=100
        )

        self.tabla_productos.column(
            "nombre",
            width=200
        )

        self.tabla_productos.column(
            "precio",
            width=100
        )

        self.tabla_productos.column(
            "categoria",
            width=150
        )

        self.tabla_productos.column(
            "stock",
            width=100
        )

        self.cargar_tabla_productos()

        self.actualizar_barra_estado()

    # =========================================================
    # TABLA GENÉRICA
    # =========================================================

    def crear_tabla(
        self,
        columnas
    ):

        contenedor = tk.Frame(
            self.contenido,
            bg=self.color_panel
        )

        contenedor.pack(
            fill="both",
            expand=True,
            padx=25,
            pady=10
        )

        tabla = ttk.Treeview(
            contenedor,
            columns=columnas,
            show="headings",
            style="Tabla.Treeview"
        )

        scrollbar = ttk.Scrollbar(
            contenedor,
            orient="vertical",
            command=tabla.yview
        )

        tabla.configure(
            yscrollcommand=scrollbar.set
        )

        tabla.pack(
            side="left",
            fill="both",
            expand=True,
            padx=(10, 0),
            pady=10
        )

        scrollbar.pack(
            side="right",
            fill="y",
            padx=(0, 10),
            pady=10
        )

        return tabla

    # =========================================================
    # LIMPIAR TABLA
    # =========================================================

    def limpiar_tabla(
        self,
        tabla
    ):

        for item in tabla.get_children():

            tabla.delete(item)

    # =========================================================
    # CARGAR PRODUCTOS
    # =========================================================

    def cargar_tabla_productos(self):

        if self.tabla_productos is None:
            return

        self.limpiar_tabla(
            self.tabla_productos
        )

        for producto in (
            self.restaurante_servicio.listar_productos()
        ):

            self.tabla_productos.insert(
                "",
                "end",
                values=(
                    producto.codigo,
                    producto.nombre,
                    producto.precio,
                    producto.categoria,
                    producto.stock
                )
            )

    # =========================================================
    # REGISTRAR PRODUCTO
    # =========================================================

    def registrar_producto(self):

        try:

            codigo = (
                self.producto_codigo_entry
                .get()
                .strip()
            )

            nombre = (
                self.producto_nombre_entry
                .get()
                .strip()
            )

            precio = float(
                self.producto_precio_entry
                .get()
                .strip()
            )

            categoria = (
                self.producto_categoria_entry
                .get()
                .strip()
            )

            stock = int(
                self.producto_stock_entry
                .get()
                .strip()
            )

            self.restaurante_servicio.registrar_producto(
                codigo,
                nombre,
                precio,
                categoria,
                stock
            )

            messagebox.showinfo(
                "Producto",
                "Producto registrado correctamente."
            )

            self.cargar_tabla_productos()
            self.limpiar_formulario_producto()
            self.actualizar_barra_estado()

        except ValueError as error:

            messagebox.showerror(
                "Error",
                str(error)
            )

    # =========================================================
    # CONSULTAR PRODUCTO
    # =========================================================

    def cargar_producto(self):

        if self.tabla_productos is None:
            return

        seleccion = self.tabla_productos.selection()

        if not seleccion:

            messagebox.showwarning(
                "Producto",
                "Seleccione un producto de la tabla."
            )

            return

        valores = self.tabla_productos.item(
            seleccion[0],
            "values"
        )

        self.limpiar_formulario_producto()

        self.producto_codigo_entry.insert(
            0,
            valores[0]
        )

        self.producto_nombre_entry.insert(
            0,
            valores[1]
        )

        self.producto_precio_entry.insert(
            0,
            valores[2]
        )

        self.producto_categoria_entry.insert(
            0,
            valores[3]
        )

        self.producto_stock_entry.insert(
            0,
            valores[4]
        )

    # =========================================================
    # ACTUALIZAR PRODUCTO
    # =========================================================

    def actualizar_producto(self):

        try:

            codigo = (
                self.producto_codigo_entry
                .get()
                .strip()
            )

            nombre = (
                self.producto_nombre_entry
                .get()
                .strip()
            )

            precio = float(
                self.producto_precio_entry
                .get()
                .strip()
            )

            categoria = (
                self.producto_categoria_entry
                .get()
                .strip()
            )

            stock = int(
                self.producto_stock_entry
                .get()
                .strip()
            )

            self.restaurante_servicio.actualizar_producto(
                codigo,
                nombre,
                precio,
                categoria,
                stock
            )

            messagebox.showinfo(
                "Producto",
                "Producto actualizado correctamente."
            )

            self.cargar_tabla_productos()
            self.limpiar_formulario_producto()
            self.actualizar_barra_estado()

        except ValueError as error:

            messagebox.showerror(
                "Error",
                str(error)
            )

    # =========================================================
    # ELIMINAR PRODUCTO
    # =========================================================

    def eliminar_producto(self):

        try:

            codigo = (
                self.producto_codigo_entry
                .get()
                .strip()
            )

            if not codigo:

                messagebox.showwarning(
                    "Producto",
                    "Ingrese o seleccione un código."
                )

                return

            producto = (
                self.restaurante_servicio
                .buscar_producto_por_codigo(
                    codigo
                )
            )

            if producto is None:

                raise ValueError(
                    "No existe un producto con ese codigo."
                )

            confirmar = messagebox.askyesno(
                "Eliminar producto",
                f"¿Desea eliminar {producto.nombre}?"
            )

            if not confirmar:
                return

            self.restaurante_servicio.eliminar_producto(
                codigo
            )

            messagebox.showinfo(
                "Producto",
                "Producto eliminado correctamente."
            )

            self.cargar_tabla_productos()
            self.limpiar_formulario_producto()
            self.actualizar_barra_estado()

        except ValueError as error:

            messagebox.showerror(
                "Error",
                str(error)
            )

    # =========================================================
    # LIMPIAR PRODUCTO
    # =========================================================

    def limpiar_formulario_producto(self):

        entradas = [
            self.producto_codigo_entry,
            self.producto_nombre_entry,
            self.producto_precio_entry,
            self.producto_categoria_entry,
            self.producto_stock_entry
        ]

        for entrada in entradas:

            if entrada is not None:

                entrada.delete(
                    0,
                    tk.END
                )

    # =========================================================
    # VENTAS
    # =========================================================

    def mostrar_ventas(self):

        self.limpiar_contenido()

        self.crear_titulo_seccion(
            "Ventas",
            "Registre una venta relacionando un usuario con un producto."
        )

        # =====================================================
        # FORMULARIO
        # =====================================================

        formulario = tk.Frame(
            self.contenido,
            bg=self.color_panel
        )

        formulario.pack(
            fill="x",
            padx=25,
            pady=10
        )

        # =====================================================
        # USUARIO / CLIENTE
        # =====================================================

        tk.Label(
            formulario,
            text="Usuario / Cliente",
            bg=self.color_panel,
            fg=self.color_texto,
            font=("Arial", 10, "bold")
        ).grid(
            row=0,
            column=0,
            padx=10,
            pady=(15, 5),
            sticky="w"
        )

        self.venta_usuario_combo = ttk.Combobox(
            formulario,
            state="readonly",
            width=30,
            font=("Arial", 10)
        )

        self.venta_usuario_combo.grid(
            row=1,
            column=0,
            padx=10,
            pady=(0, 15)
        )

        # =====================================================
        # PRODUCTO
        # =====================================================

        tk.Label(
            formulario,
            text="Producto",
            bg=self.color_panel,
            fg=self.color_texto,
            font=("Arial", 10, "bold")
        ).grid(
            row=0,
            column=1,
            padx=10,
            pady=(15, 5),
            sticky="w"
        )

        self.venta_producto_combo = ttk.Combobox(
            formulario,
            state="readonly",
            width=30,
            font=("Arial", 10)
        )

        self.venta_producto_combo.grid(
            row=1,
            column=1,
            padx=10,
            pady=(0, 15)
        )

        # =====================================================
        # REGISTRAR VENTA
        # =====================================================

        boton_venta = tk.Button(
            formulario,
            text="Registrar venta",
            command=self.registrar_venta,
            bg=self.color_venta,
            fg="#ffffff",
            activebackground="#6d28d9",
            activeforeground="#ffffff",
            relief="flat",
            borderwidth=0,
            font=("Arial", 9, "bold"),
            padx=12,
            pady=8,
            width=16,
            cursor="hand2"
        )

        boton_venta.grid(
            row=1,
            column=2,
            padx=15,
            pady=(0, 15)
        )

        # =====================================================
        # MENSAJE
        # =====================================================

        self.mensaje_venta = tk.Label(
            formulario,
            text="",
            bg=self.color_panel,
            fg="#16803c",
            font=("Arial", 10, "bold")
        )

        self.mensaje_venta.grid(
            row=2,
            column=0,
            columnspan=3,
            padx=10,
            pady=(0, 15)
        )

        # =====================================================
        # CARGAR USUARIOS
        # =====================================================

        self.usuarios_venta = {}

        valores_usuarios = []

        for usuario in (
            self.restaurante_servicio.listar_usuarios()
        ):

            texto = (
                f"{usuario.identificacion} - "
                f"{usuario.nombre}"
            )

            valores_usuarios.append(
                texto
            )

            self.usuarios_venta[texto] = usuario

        self.venta_usuario_combo["values"] = (
            valores_usuarios
        )

        if valores_usuarios:

            self.venta_usuario_combo.current(0)

        # =====================================================
        # CARGAR PRODUCTOS
        # =====================================================

        self.productos_venta = {}

        valores_productos = []

        for producto in (
            self.restaurante_servicio.listar_productos()
        ):

            texto = (
                f"{producto.codigo} - "
                f"{producto.nombre}"
            )

            valores_productos.append(
                texto
            )

            self.productos_venta[texto] = producto

        self.venta_producto_combo["values"] = (
            valores_productos
        )

        if valores_productos:

            self.venta_producto_combo.current(0)

        # =====================================================
        # TABLA DE VENTAS
        # =====================================================

        contenedor_tabla = tk.Frame(
            self.contenido,
            bg=self.color_panel
        )

        contenedor_tabla.pack(
            fill="both",
            expand=True,
            padx=25,
            pady=10
        )

        columnas = (
            "usuario_id",
            "usuario",
            "producto_codigo",
            "producto",
            "fecha"
        )

        self.tabla_ventas = ttk.Treeview(
            contenedor_tabla,
            columns=columnas,
            show="headings",
            style="Tabla.Treeview"
        )

        encabezados = {
            "usuario_id": "Identificacion",
            "usuario": "Usuario",
            "producto_codigo": "Codigo",
            "producto": "Producto",
            "fecha": "Fecha"
        }

        for columna in columnas:

            self.tabla_ventas.heading(
                columna,
                text=encabezados[columna]
            )

        self.tabla_ventas.column(
            "usuario_id",
            width=120
        )

        self.tabla_ventas.column(
            "usuario",
            width=180
        )

        self.tabla_ventas.column(
            "producto_codigo",
            width=100
        )

        self.tabla_ventas.column(
            "producto",
            width=180
        )

        self.tabla_ventas.column(
            "fecha",
            width=120
        )

        scrollbar = ttk.Scrollbar(
            contenedor_tabla,
            orient="vertical",
            command=self.tabla_ventas.yview
        )

        self.tabla_ventas.configure(
            yscrollcommand=scrollbar.set
        )

        self.tabla_ventas.pack(
            side="left",
            fill="both",
            expand=True,
            padx=(10, 0),
            pady=10
        )

        scrollbar.pack(
            side="right",
            fill="y",
            padx=(0, 10),
            pady=10
        )

        self.cargar_tabla_ventas()

        self.actualizar_barra_estado()

    # =========================================================
    # REGISTRAR VENTA
    # =========================================================

    def registrar_venta(self):

        if self.venta_usuario_combo is None:
            return

        if self.venta_producto_combo is None:
            return

        if self.mensaje_venta is None:
            return

        usuario_seleccionado = (
            self.venta_usuario_combo.get()
        )

        producto_seleccionado = (
            self.venta_producto_combo.get()
        )

        if not usuario_seleccionado:

            self.mensaje_venta.config(
                text="Seleccione un usuario.",
                fg="#b42318"
            )

            return

        if not producto_seleccionado:

            self.mensaje_venta.config(
                text="Seleccione un producto.",
                fg="#b42318"
            )

            return

        usuario = self.usuarios_venta.get(
            usuario_seleccionado
        )

        producto = self.productos_venta.get(
            producto_seleccionado
        )

        if usuario is None:

            self.mensaje_venta.config(
                text="No se pudo obtener el usuario seleccionado.",
                fg="#b42318"
            )

            return

        if producto is None:

            self.mensaje_venta.config(
                text="No se pudo obtener el producto seleccionado.",
                fg="#b42318"
            )

            return

        fecha = datetime.now().strftime(
            "%Y-%m-%d"
        )

        try:

            self.restaurante_servicio.registrar_venta(
                usuario.identificacion,
                producto.codigo,
                fecha
            )

            self.mensaje_venta.config(
                text="Venta registrada correctamente.",
                fg="#16803c"
            )

            self.cargar_tabla_ventas()

            self.actualizar_barra_estado()

        except ValueError as error:

            self.mensaje_venta.config(
                text=str(error),
                fg="#b42318"
            )

    # =========================================================
    # CARGAR TABLA DE VENTAS
    # =========================================================

    def cargar_tabla_ventas(self):

        if self.tabla_ventas is None:
            return

        self.limpiar_tabla(
            self.tabla_ventas
        )

        for venta in (
            self.restaurante_servicio.listar_ventas()
        ):

            usuario = (
                self.restaurante_servicio
                .buscar_usuario_por_identificacion(
                    venta.usuario_id
                )
            )

            producto = (
                self.restaurante_servicio
                .buscar_producto_por_codigo(
                    venta.producto_codigo
                )
            )

            nombre_usuario = (
                usuario.nombre
                if usuario is not None
                else "No encontrado"
            )

            nombre_producto = (
                producto.nombre
                if producto is not None
                else "No encontrado"
            )

            self.tabla_ventas.insert(
                "",
                "end",
                values=(
                    venta.usuario_id,
                    nombre_usuario,
                    venta.producto_codigo,
                    nombre_producto,
                    venta.fecha
                )
            )

    # =========================================================
    # BARRA DE ESTADO
    # =========================================================

    def actualizar_barra_estado(self):

        if self.barra_estado is None:
            return

        texto = (
            f"Productos: "
            f"{self.restaurante_servicio.cantidad_productos()}"
            f"  |  "
            f"Usuarios: "
            f"{self.restaurante_servicio.cantidad_usuarios()}"
            f"  |  "
            f"Ventas: "
            f"{self.restaurante_servicio.cantidad_ventas()}"
            f"  |  "
            "Datos JSON locales"
        )

        self.barra_estado.config(
            text=texto
        )

    # =========================================================
    # CERRAR SESIÓN
    # =========================================================

    def cerrar_sesion(self):

        confirmar = messagebox.askyesno(
            "Cerrar sesión",
            "¿Desea cerrar la sesión?"
        )

        if confirmar:

            self.al_cerrar_sesion()
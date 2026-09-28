import tkinter as tk
from pathlib import Path

from servicios.archivo_servicio import ArchivoServicio
from servicios.restaurante_servicio import RestauranteServicio

from ui.login_view import LoginView
from ui.main_view import MainView


class AplicacionRestaurante:

    def __init__(self):

        self.root = tk.Tk()

        ruta_base = Path(__file__).resolve().parent

        self.root.title("SABORES DE MI TIERRA")
        self.root.geometry("920x560")
        self.root.minsize(780, 500)

        # =====================================================
        # ICONO
        # =====================================================

        ruta_icono = (
            ruta_base
            / "assets"
            / "icono.png"
        )

        self.icono = None

        if ruta_icono.exists():

            try:

                self.icono = tk.PhotoImage(
                    file=str(ruta_icono)
                )

                self.root.iconphoto(
                    True,
                    self.icono
                )

            except Exception:
                self.icono = None

        # =====================================================
        # SERVICIOS
        # =====================================================

        archivo_servicio = ArchivoServicio(
            ruta_base / "datos"
        )

        self.restaurante_servicio = RestauranteServicio(
            archivo_servicio
        )

        # =====================================================
        # INFORMACION EN CONSOLA
        # =====================================================

        self.mostrar_informacion_consola(ruta_base)

        # =====================================================
        # VISTA ACTUAL
        # =====================================================

        self.vista_actual = None

        self.mostrar_login()

    # =========================================================
    # INFORMACION EN CONSOLA
    # =========================================================

    def mostrar_informacion_consola(self, ruta_base):

        print("=" * 45)
        print("SABORES DE MI TIERRA")
        print("RESTAURANTE")
        print("=" * 45)

        print("RUTA DE PRODUCTOS:")

        print(
            ruta_base
            / "datos"
            / "productos.json"
        )

        print()

        print(
            "PRODUCTOS CARGADOS:",
            self.restaurante_servicio.cantidad_productos()
        )

        for producto in self.restaurante_servicio.listar_productos():

            print(
                producto.codigo,
                producto.nombre,
                producto.precio,
                producto.categoria,
                producto.stock
            )

        print()

        print(
            "USUARIOS CARGADOS:",
            self.restaurante_servicio.cantidad_usuarios()
        )

        print(
            "VENTAS CARGADAS:",
            self.restaurante_servicio.cantidad_ventas()
        )

        print("=" * 45)

    # =========================================================
    # CAMBIAR VISTA
    # =========================================================

    def cambiar_vista(self, nueva_vista):

        if self.vista_actual is not None:
            self.vista_actual.destroy()

        self.vista_actual = nueva_vista

        self.vista_actual.pack(
            fill="both",
            expand=True
        )

    # =========================================================
    # LOGIN
    # =========================================================

    def mostrar_login(self):

        vista = LoginView(
            self.root,
            self.restaurante_servicio,
            self.mostrar_interfaz_principal
        )

        self.cambiar_vista(vista)

    # =========================================================
    # INTERFAZ PRINCIPAL
    # =========================================================

    def mostrar_interfaz_principal(self, usuario_actual):

        vista = MainView(
            self.root,
            self.restaurante_servicio,
            usuario_actual,
            self.mostrar_login
        )

        self.cambiar_vista(vista)

    # =========================================================
    # EJECUTAR
    # =========================================================

    def ejecutar(self):

        self.root.mainloop()


# =============================================================
# PROGRAMA PRINCIPAL
# =============================================================

if __name__ == "__main__":

    app = AplicacionRestaurante()

    app.ejecutar()
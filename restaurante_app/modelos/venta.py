class Venta:
    def __init__(self, usuario_id, producto_codigo, fecha):
        self.usuario_id = usuario_id
        self.producto_codigo = producto_codigo
        self.fecha = fecha

    def to_dict(self):
        return {
            "usuario_id": self.usuario_id,
            "producto_codigo": self.producto_codigo,
            "fecha": self.fecha
        }

    @classmethod
    def from_dict(cls, datos):
        return cls(
            datos["usuario_id"],
            datos["producto_codigo"],
            datos["fecha"]
        )
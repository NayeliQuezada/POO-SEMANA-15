class Producto:
    def __init__(self, codigo, nombre, precio, categoria, stock):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria
        self.stock = stock

    def actualizar(self, nombre, precio, categoria, stock):
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria
        self.stock = stock

    def to_dict(self):
        return {
            "codigo": self.codigo,
            "nombre": self.nombre,
            "precio": self.precio,
            "categoria": self.categoria,
            "stock": self.stock
        }

    @classmethod
    def from_dict(cls, datos):
        return cls(
            datos["codigo"],
            datos["nombre"],
            datos["precio"],
            datos["categoria"],
            datos["stock"]
        )
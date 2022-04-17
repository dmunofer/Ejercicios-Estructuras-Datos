
class Naturaleza():

    ALIMENTARIA = 0.055
    SERVICIO = 0.2

class Producto(Naturaleza):

    def __init__(self,naturaleza):
        self.naturaleza=naturaleza
        self.precio =100

    def facturar(self):
        return (100*self.naturaleza)+self.precio

class FactoryFactura(Producto):

    def crear(self,producto):
        self.producto = producto
        return self.producto



producto = Producto(Naturaleza.ALIMENTARIA)
factura = FactoryFactura(Producto)
precio_neto = factura.crear(producto).facturar()
print(precio_neto)

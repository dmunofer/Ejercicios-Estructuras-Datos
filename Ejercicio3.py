
class Naturaleza():

    ALIMENTARIA = 0.055
    SERVICIO = 0.2

class Producto(Naturaleza):

    def __init__(self,naturaleza):
        self.naturaleza=naturaleza
        self.precio =100
    
    def facturar(self):
        return (100*self.naturaleza)+self.precio


        















'''
producto = Producto(Naturaleza.ALIMENTARIA) # IVA 5,5% 
precio_neto = FactoryFactura.crear(producto).facturar() 
print(precio_neto) 
# 105.5 
 
producto = Producto(Naturaleza.SERVICIO) # IVA 20% 
precio_neto = FactoryFactura.crear(producto).facturar() 
print(precio_neto) 
# 120 
'''
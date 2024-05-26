
class Menu(object):
    def __init__(self):
        self.nombre = ""
        self.establecimiento = None
        self.producto = []
        self.descripcion = ""
    
    def __str__(self):
        return self.nombre


class Producto(object):
    def __init__(self):
        self.nombre = ""
        self.precio = 0.
        self.menu = None
        self.pedido = None
        self.descripcion = ""

    def __str__(self):
        return self.nombre
        
    # Start of user code -> properties/constructors for Producto class

    # End of user code
    def getNombre(self):
        # Start of user code protected zone for getNombre function body
        raise NotImplementedError
        # End of user code	
    def setNombre(self):
        # Start of user code protected zone for setNombre function body
        raise NotImplementedError
        # End of user code	
    # Start of user code -> methods for Producto class

    # End of user code


producto1 = Producto()
producto1.nombre = "Papas"
producto1.precio = 20.0
producto1.descripcion = "Papas fritas"


producto2 = Producto()
producto2.nombre = "Hamburguesa"
producto2.precio = 50.0
producto2.descripcion = "Hamburguesa con queso"
    

menu = Menu()
menu.nombre = "Comida"
menu.producto.append(producto1)
menu.producto.append(producto2)

print("-----Menu: %s ------- "  %menu)
for producto in menu.producto:
    print("* %s"  %producto)
        
    # Start of user code -> properties/constructors for Menu class

    # End of user code
    # Start of user code -> methods for Menu class

    # End of user code


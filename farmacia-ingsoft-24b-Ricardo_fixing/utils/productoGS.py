class Producto:
    def __init__(self, id_producto=None, nombre_producto="", descripcion="", precio=0, cantidad_stock=0, id_proveedor=0):
        self.id_producto = id_producto
        self.nombre_producto = nombre_producto
        self.descripcion = descripcion
        self.precio = precio
        self.cantidad_stock = cantidad_stock
        self.id_proveedor = id_proveedor

    def getId_producto(self):
        return self.id_producto

    def setId_producto(self, id_producto):
        self.id_producto = id_producto

    def getNombre_producto(self):
        return self.nombre_producto

    def setNombre_producto(self, nombre_producto):
        self.nombre_producto = nombre_producto

    def getDescripcion(self):
        return self.descripcion

    def setDescripcion(self, descripcion):
        self.descripcion = descripcion

    def getPrecio(self):
        return self.precio

    def setPrecio(self, precio):
        self.precio = precio

    def getCantidad_stock(self):
        return self.cantidad_stock

    def setCantidad_stock(self, cantidad_stock):
        self.cantidad_stock = cantidad_stock

    def getId_proveedor(self):
        return self.id_proveedor

    def setId_proveedor(self, id_proveedor):
        self.id_proveedor = id_proveedor

class DetalleVenta:
    def __init__(self, id_detalle=None, id_venta=None, id_producto=None, cantidad=None, precio_unitario=None, subtotal=None):
        self.id_detalle = id_detalle
        self.id_venta = id_venta
        self.id_producto = id_producto
        self.cantidad = cantidad
        self.precio_unitario = precio_unitario
        self.subtotal = subtotal

    def getId_detalle(self):
        return self.id_detalle

    def setId_detalle(self, id_detalle):
        self.id_detalle = id_detalle

    def getId_venta(self):
        return self.id_venta

    def setId_venta(self, id_venta):
        self.id_venta = id_venta

    def getId_producto(self):
        return self.id_producto

    def setId_producto(self, id_producto):
        self.id_producto = id_producto

    def getCantidad(self):
        return self.cantidad

    def setCantidad(self, cantidad):
        self.cantidad = cantidad

    def getPrecio_unitario(self):
        return self.precio_unitario

    def setPrecio_unitario(self, precio_unitario):
        self.precio_unitario = precio_unitario

    def getSubtotal(self):
        return self.subtotal

    def setSubtotal(self, subtotal):
        self.subtotal = subtotal

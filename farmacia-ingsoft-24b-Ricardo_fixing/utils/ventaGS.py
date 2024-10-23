class Ventas:
    def __init__(self, id_venta=None, id_cliente=None, id_usuario=None, fecha_venta="", total=None):
        self.id_venta = id_venta
        self.id_cliente = id_cliente
        self.id_usuario = id_usuario
        self.fecha_venta = fecha_venta
        self.total = total

    def getId_venta(self):
        return self.id_venta

    def setId_venta(self, id_venta):
        self.id_venta = id_venta

    def getId_cliente(self):
        return self.id_cliente

    def setId_cliente(self, id_cliente):
        self.id_cliente = id_cliente

    def getId_usuario(self):
        return self.id_usuario

    def setId_usuario(self, id_usuario):
        self.id_usuario = id_usuario

    def getFecha_venta(self):
        return self.fecha_venta

    def setFecha_venta(self, fecha_venta):
        self.fecha_venta = fecha_venta

    def getTotal(self):
        return self.total

    def setTotal(self, total):
        self.total = total

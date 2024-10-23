class Cliente:
    def __init__(self, id_cliente=None, nombre="", rfc="", puntos_acumulados=""):
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.rfc = rfc
        self.puntos_acumulados = puntos_acumulados

        def getIdCliente(self):
            return self.id_cliente

        def setIdCliente(self, id_cliente):
            self.id_cliente = id_cliente

        def getNombre(self):
            return self.nombre

        def setNombre(self, nombre):
            self.nombre = nombre

        def getRfc(self):
            return self.rfc

        def setRfc(self, rfc):
            self.rfc = rfc

        def getPuntosAcumulados(self):
            return self.puntos_acumulados

        def setPuntosAcumulados(self, puntos_acumulados):
            self.puntos_acumulados = puntos_acumulados

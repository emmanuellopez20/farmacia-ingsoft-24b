class Proveedor:
    def __init__(self, id_proveedor=None, nombre_empresa="", telefono="", direccion="", email=""):
        self.id_proveedor = id_proveedor
        self.nombre_empresa = nombre_empresa
        self.telefono = telefono
        self.direccion = direccion
        self.email = email

        def getId_proveedor(self):
            return self.usuario_id
        
        def setId_proveedor(self, id_proveedor):
            self.id_proveedor = id_proveedor

        def getNombre_empresa(self):
            return self.nombre_empresa
        
        def setNombre_empresa(self, nombre_empresa):
            self.nombre_empresa = nombre_empresa

        def getTelefono(self):
            return self.telefono
        
        def setTelefono(self, telefono):
            self.Telefono = telefono

        def getDireccion(self):
            return self.direccion
        
        def setDireccion(self, direccion):
            self.direccion = direccion

        def getEmail(self):
            return self.email
        
        def setEmail(self, email):
            self.email = email
        

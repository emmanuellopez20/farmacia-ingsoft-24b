class Usuario:
    def __init__(self, id_usuario=None, nombre="", correo="", contraseña="",rol=""):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.correo = correo
        self.contraseña = contraseña
        self.rol = rol

    def getId_usuario(self):
        return self.usuario_id
    
    def setId_usuario(self, usuario_id):
        self.usuario_id = usuario_id

    def getNombre(self):
        return self.nombre
    
    def setNombre(self, nombre):
        self.nombre = nombre

    def getCorreo(self):
        return self.correo
    
    def setCorreo(self, correo):
        self.correo = correo

    def getContraseña(self):
        return self.contraseña
    
    def setContraseña(self, contraseña):
        self.contraseña = contraseña

    def getRol(self):
        return self.rol
    
    def setRol(self, rol):
        self.rol = rol
        

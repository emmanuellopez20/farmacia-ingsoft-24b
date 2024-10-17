import mysql.connector
from mysql.connector import Error
import conexion as con
from utils.usuariosGS import Usuario

class dbUsuario:
    def save(self, usuario):
        try:
            self.con = con.conexion()
            self.conn = self.con.open()
            if self.conn is None:
                raise Exception("No se pudo conectar a la base de datos")
            self.cursor = self.conn.cursor()
            self.sql = "INSERT INTO usuarios (nombre, correo, contraseña, rol) VALUES (%s, %s, %s, %s)"
            self.datos = (usuario.getNombre(), usuario.getCorreo(), usuario.getContraseña(), usuario.getRol())
            self.cursor.execute(self.sql, self.datos)
            self.conn.commit()
            print("Datos insertados correctamente")
            self.con.close()
        except mysql.connector.Error as err:
            print(f"Error al guardar el usuario: {err}")
        except Exception as e:
            print(f"Error: {e}")

    def search(self, usuario_id):
        try:
            self.con = con.conexion()
            self.conn = self.con.open()
            self.cursor = self.conn.cursor(buffered=True)
            self.sql = "SELECT * FROM usuarios WHERE id_usuario = %s"
            self.cursor.execute(self.sql, (usuario_id,))
            row = self.cursor.fetchone()
            self.con.close()
            if row:
                usuario = Usuario(row[0], row[1], row[2], row[3], row[4])
                return usuario
            return None
        except mysql.connector.Error as err:
            print(f"Error al buscar el usuario: {err}")
            return None

    def edit(self, usuario):
        try:
            self.con = con.conexion()
            self.conn = self.con.open()
            self.cursor = self.conn.cursor()
            self.sql = "UPDATE usuarios SET nombre=%s, correo=%s, contraseña=%s, rol=%s WHERE id_usuario=%s"
            self.datos = (usuario.getNombre(), usuario.getCorreo(), usuario.getContraseña(), usuario.getRol(), usuario.getUsuario_id())
            self.cursor.execute(self.sql, self.datos)
            self.conn.commit()
            self.con.close()
        except mysql.connector.Error as err:
            print(f"Error al editar el usuario: {err}")

    def remov(self, usuario_id):
        try:
            self.con = con.conexion()
            self.conn = self.con.open()
            self.cursor = self.conn.cursor()
            self.sql = "DELETE FROM usuarios WHERE id_usuario=%s"
            self.cursor.execute(self.sql, (usuario_id,))
            self.conn.commit()
            self.con.close()
        except mysql.connector.Error as err:
            print(f"Error al eliminar el usuario: {err}")

    def getMaxId(self):
        try:
            self.con = con.conexion()
            self.conn = self.con.open()
            self.cursor = self.conn.cursor()
            self.sql = "SELECT MAX(id_usuario) FROM usuarios"
            self.cursor.execute(self.sql)
            row = self.cursor.fetchone()
            self.con.close()
            return row[0] if row[0] is not None else 0
        except mysql.connector.Error as err:
            print(f"Error al obtener el máximo ID: {err}")
            return 0

    def autenticar(self, username, contraseña):
        try:
            self.con = con.conexion()
            self.conn = self.con.open()
            self.cursor = self.conn.cursor(buffered=True)
            self.sql = "SELECT * FROM usuarios WHERE correo = %s AND contraseña = %s"
            self.cursor.execute(self.sql, (username, contraseña))
            row = self.cursor.fetchone()
            self.con.close()
            if row:
                usuario = Usuario(row[0], row[1], row[2], row[3], row[4])
                return usuario
            return None
        except mysql.connector.Error as err:
            print(f"Error al autenticar el usuario: {err}")
            return None

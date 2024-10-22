import mysql.connector
from mysql.connector import Error
import conexion as con
from utils.proveedorGS import Proveedor

class dbProveedor:
    def save(self, proveedor):
        try:
            self.con = con.conexion()
            self.conn = self.con.open()
            if self.conn is None:
                raise Exception("No se puede conectar a la base de datos")
            self.cursor = self.conn.cursor()
            self.sql = "INSERT INTO proveedores (nombre_empresa, telefono, direccion, email) VALUES (%s, %s, %s, %s)"
            self.datos = (proveedor.getNombre(), proveedor.getTelefono(), proveedor.getDireccion(), proveedor.getEmail())
            self.cursor.execute(self.sql, self.datos)
            self.conn.commit()
            print("Datos insertados correctamente")
            self.con.close()
        except mysql.connector.Error as err:
            print(f"Error al guardar el proveedor: {err}")
        except Exception as e:
            print(f"Error: {e}")

    def search(self, id_proveedor):
        try:
            self.con = con.conexion()
            self.conn = self.con.open()
            self.cursor = self.conn.cursor(buffered=True)
            self.sql = "SELECT * FROM proveedores WHERE id_proveedor = %s"
            self.cursor.execute(self.sql, (id_proveedor,))
            row = self.cursor.fetchone()
            self.con.close()
            if row:
                proveedor = Proveedor(row[0], row[1], row[2], row[3], row[4])
                return proveedor
            return None
        except mysql.connector.Error as err:
            print(f"Error al buscar el proveedor: {err}")
            return None

    def edit(self, proveedor):
        try:
            self.con = con.conexion()
            self.conn = self.con.open()
            self.cursor = self.conn.cursor()
            self.sql = "UPDATE proveedores SET nombre_empresa=%s, telefono=%s, direccion=%s, email=%s WHERE id_proveedor=%s"
            self.datos = (proveedor.getNombre(), proveedor.getTelefono(), proveedor.getDireccion(), proveedor.getEmail(), proveedor.getId_proveedor())
            self.cursor.execute(self.sql, self.datos)
            self.conn.commit()
            self.con.close()
        except mysql.connector.Error as err:
            print(f"Error al editar el proveedor: {err}")

    def remov(self, id_proveedor):
        try:
            self.con = con.conexion()
            self.conn = self.con.open()
            self.cursor = self.conn.cursor()
            self.sql = "DELETE FROM proveedores WHERE id_proveedor=%s"
            self.cursor.execute(self.sql, (id_proveedor,))
            self.conn.commit()
            self.con.close()
        except mysql.connector.Error as err:
            print(f"Error al eliminar el proveedor: {err}")

    def getMaxId(self):
        try:
            self.con = con.conexion()
            self.conn = self.con.open()
            self.cursor = self.conn.cursor()
            self.sql = "SELECT MAX(id_proveedor) FROM proveedores"
            self.cursor.execute(self.sql)
            row = self.cursor.fetchone()
            self.con.close()
            return row[0] if row[0] is not None else 0
        except mysql.connector.Error as err:
            print(f"Error al obtener el maximo ID: {err}")
            return 0
    
    def get_all_proveedores(self):
        try:
            self.con = con.conexion()
            self.conn = self.con.open()
            self.cursor = self.conn.cursor()
            self.sql = "SELECT * FROM proveedores"
            self.cursor.execute(self.sql)
            rows = self.cursor.fetchall()
            self.con.close()
            proveedores = []
            for row in rows:
                proveedor = Proveedor(row[0], row[1], row[2], row[3], row[4])
                proveedores.append(proveedor)
            return proveedores
        except mysql.connector.Error as err:
            print(f"Error al obtener proveedores: {err}")
            return []

        
    def search_by_name(self, nombre_empresa):
        try:
            self.con = con.conexion()
            self.conn = self.con.open()
            self.cursor = self.conn.cursor(buffered=True)
            self.sql = "SELECT * FROM proveedores WHERE nombre_empresa = %s"
            self.cursor.execute(self.sql, (nombre_empresa,))
            row = self.cursor.fetchone()
            self.con.close()
            if row:
                return Proveedor(row[0], row[1], row[2], row[3], row[4])
            return None
        except mysql.connector.Error as err:
            print(f"Error al buscar proveedor: {err}")
            return None

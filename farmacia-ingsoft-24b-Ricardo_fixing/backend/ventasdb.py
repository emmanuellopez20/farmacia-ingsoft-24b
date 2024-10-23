import mysql.connector
from mysql.connector import Error
import conexion as con
from utils.ventaGS import Ventas


class dbVentas:
    def save(self, venta):
        try:
            self.con = con.conexion()
            self.conn = self.con.open()
            if self.conn is None:
                raise Exception("No se puede conectar a la base de datos")
            self.cursor = self.conn.cursor()
            self.sql = "INSERT INTO ventas (id_cliente, id_usuario, fecha_venta, total) VALUES (%s, %s, %s, %s)"
            self.datos = (venta.getId_cliente(), venta.getId_usuario(), venta.getFecha_venta(), venta.getTotal())
            self.cursor.execute(self.sql, self.datos)
            self.conn.commit()
            print("Venta insertada correctamente")
            last_id = self.cursor.lastrowid
            self.con.close()
            return last_id
        except mysql.connector.Error as err:
            print(f"Error al guardar la venta: {err}")
        except Exception as e:
            print(f"Error: {e}")

    def get_all_ventas(self):
        try:
            self.con = con.conexion()
            self.conn = self.con.open()
            self.cursor = self.conn.cursor()
            self.sql = "SELECT * FROM ventas"
            self.cursor.execute(self.sql)
            rows = self.cursor.fetchall()
            self.con.close()
            ventas = []
            for row in rows:
                venta = Ventas(row[0], row[1], row[2], row[3], row[4])
                ventas.append(venta)
            return ventas
        except mysql.connector.Error as err:
            print(f"Error al obtener ventas: {err}")
            return []
        
    def delete_by_id(self, id_venta):
        try:
            self.con = con.conexion()
            self.conn = self.con.open()
            self.cursor = self.conn.cursor()
            self.sql = "DELETE FROM ventas WHERE id_venta = %s"
            print(f"Ejecutando consulta: {self.sql} con id_venta: {id_venta}")
            self.cursor.execute(self.sql, (id_venta,))
            self.conn.commit()
            print("Eliminación exitosa")
            self.con.close()
        except mysql.connector.Error as err:
            print(f"Error al eliminar la venta: {err}")



    def get_max_id(self):
        try:
            self.con = con.conexion()
            self.conn = self.con.open()
            self.cursor = self.conn.cursor()
            self.sql = "SELECT MAX(id_venta) FROM ventas"
            self.cursor.execute(self.sql)
            row = self.cursor.fetchone()
            self.con.close()
            return row[0] if row[0] is not None else 0
        except mysql.connector.Error as err:
            print(f"Error al obtener el ID máximo: {err}")
            return 0


    def search(self, folio):
        try:
            self.con = con.conexion()
            self.conn = self.con.open()
            self.cursor = self.conn.cursor()
            self.sql = "SELECT * FROM ventas WHERE id_venta = %s"
            self.cursor.execute(self.sql, (folio,))
            row = self.cursor.fetchone()
            self.con.close()
            if row:
                venta = Ventas(row[0], row[1], row[2], row[3], row[4])
                return venta
            return None
        except mysql.connector.Error as err:
            print(f"Error al buscar la venta: {err}")
            return 

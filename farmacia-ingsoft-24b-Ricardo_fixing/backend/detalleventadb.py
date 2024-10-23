import mysql.connector
from mysql.connector import Error
import conexion as con
from utils.detalleventaGS import DetalleVenta

class dbDetalleVenta:
    def save(self, detalle_venta):
        try:
            self.con = con.conexion()
            self.conn = self.con.open()
            if self.conn is None:
                raise Exception("No se puede conectar a la base de datos")
            self.cursor = self.conn.cursor()
            self.sql = "INSERT INTO detalle_venta (id_venta, id_producto, cantidad, precio_unitario, subtotal) VALUES (%s, %s, %s, %s, %s)"
            self.datos = (detalle_venta.getId_venta(), detalle_venta.getId_producto(), detalle_venta.getCantidad(), detalle_venta.getPrecio_unitario(), detalle_venta.getSubtotal())
            self.cursor.execute(self.sql, self.datos)
            self.conn.commit()
            print("Detalle de venta insertado correctamente")
            self.con.close()
        except mysql.connector.Error as err:
            print(f"Error al guardar el detalle de venta: {err}")
        except Exception as e:
            print(f"Error: {e}")

    def get_all(self):
            try:
                self.con = con.conexion()
                self.conn = self.con.open()
                self.cursor = self.conn.cursor()
                self.sql = "SELECT * FROM detalle_venta"
                self.cursor.execute(self.sql)
                rows = self.cursor.fetchall()
                self.con.close()
                detalles = []
                for row in rows:
                    detalle = DetalleVenta(row[0], row[1], row[2], row[3], row[4], row[5])
                    detalles.append(detalle)
                return detalles
            except mysql.connector.Error as err:
                print(f"Error al obtener los detalles de venta: {err}")
                return 
    
    def delete_by_venta_id(self, id_venta):
            try:
                self.con = con.conexion()
                self.conn = self.con.open()
                self.cursor = self.conn.cursor()
                self.sql = "DELETE FROM detalle_venta WHERE id_venta = %s"
                self.cursor.execute(self.sql, (id_venta,))
                self.conn.commit()
                self.con.close()
            except mysql.connector.Error as err:
                print(f"Error al eliminar el detalle de venta: {err}")

    def get_all_by_venta_id(self, id_venta):
        try:
            self.con = con.conexion()
            self.conn = self.con.open()
            self.cursor = self.conn.cursor()
            self.sql = "SELECT * FROM detalle_venta WHERE id_venta = %s"
            self.cursor.execute(self.sql, (id_venta,))
            rows = self.cursor.fetchall()
            self.con.close()
            detalles = []
            for row in rows:
                detalle = DetalleVenta(row[0], row[1], row[2], row[3], row[4], row[5])
                detalles.append(detalle)
            return detalles
        except mysql.connector.Error as err:
            print(f"Error al obtener los detalles de venta: {err}")
            return []
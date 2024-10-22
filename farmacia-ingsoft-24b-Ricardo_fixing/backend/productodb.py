import mysql.connector
from mysql.connector import Error
import conexion as con
from utils.productoGS import Producto

class dbProductos:
    def save(self, producto):
        try:
            self.con = con.conexion()
            self.conn = self.con.open()
            if self.conn is None:
                raise Exception("No se puede conectar a la base de datos")
            self.cursor = self.conn.cursor()
            self.sql = "INSERT INTO productos (nombre_producto, descripcion, precio, cantidad_stock, id_proveedor) VALUES (%s, %s, %s, %s, %s)"
            self.datos = (producto.getNombre_producto(), producto.getDescripcion(), producto.getPrecio(), producto.getCantidad_stock(), producto.getId_proveedor())
            self.cursor.execute(self.sql, self.datos)
            self.conn.commit()
            print("Datos insertados correctamente")
            self.con.close()
        except mysql.connector.Error as err:
            print(f"Error al guardar el producto: {err}")
        except Exception as e:
            print(f"Error: {e}")

    def search(self, id_producto):
        try:
            self.con = con.conexion()
            self.conn = self.con.open()
            self.cursor = self.conn.cursor(buffered=True)
            self.sql = "SELECT * FROM productos WHERE id_producto = %s"
            self.cursor.execute(self.sql, (id_producto,))
            row = self.cursor.fetchone()
            self.con.close()
            if row:
                producto = Producto(row[0], row[1], row[2], row[3], row[4], row[5])
                return producto
            return None
        except mysql.connector.Error as err:
            print(f"Error al buscar el producto: {err}")
            return None

    def edit(self, producto):
        try:
            self.con = con.conexion()
            self.conn = self.con.open()
            self.cursor = self.conn.cursor()
            self.sql = "UPDATE productos SET nombre_producto=%s, descripcion=%s, precio=%s, cantidad_stock=%s, id_proveedor=%s WHERE id_producto=%s"
            self.datos = (producto.getNombre_producto(), producto.getDescripcion(), producto.getPrecio(), producto.getCantidad_stock(), producto.getId_proveedor(), producto.getId_producto())
            self.cursor.execute(self.sql, self.datos)
            self.conn.commit()
            self.con.close()
        except mysql.connector.Error as err:
            print(f"Error al editar el producto: {err}")

    def remov(self, id_producto):
        try:
            self.con = con.conexion()
            self.conn = self.con.open()
            self.cursor = self.conn.cursor()
            self.sql = "DELETE FROM productos WHERE id_producto=%s"
            self.cursor.execute(self.sql, (id_producto,))
            self.conn.commit()
            self.con.close()
        except mysql.connector.Error as err:
            print(f"Error al eliminar el producto: {err}")

    def getMaxId(self):
        try:
            self.con = con.conexion()
            self.conn = self.con.open()
            self.cursor = self.conn.cursor()
            self.sql = "SELECT MAX(id_producto) FROM productos"
            self.cursor.execute(self.sql)
            row = self.cursor.fetchone()
            self.con.close()
            return row[0] if row[0] is not None else 0
        except mysql.connector.Error as err:
            print(f"Error al obtener el maximo ID: {err}")
            return 0

    

    """     def search_by_name(self, nombre_producto):
            try:
                self.con = con.conexion()
                self.conn = self.con.open()
                self.cursor = self.conn.cursor(buffered=True)
                self.sql = "SELECT * FROM productos WHERE nombre_producto LIKE %s"
                self.cursor.execute(self.sql, ('%' + nombre_producto + '%',))
                rows = self.cursor.fetchall()
                self.con.close()
                productos = []
                for row in rows:
                    producto = Producto(row[0], row[1], row[2], row[3], row[4], row[5])
                    productos.append(producto)
                return productos
            except mysql.connector.Error as err:
                print(f"Error al buscar productos: {err}")
                return [] """
    def search_by_name(self, nombre_producto):
        try:
            self.con = con.conexion()
            self.conn = self.con.open()
            self.cursor = self.conn.cursor(buffered=True)
            self.sql = "SELECT * FROM productos WHERE nombre_producto LIKE %s"
            self.cursor.execute(self.sql, ('%' + nombre_producto + '%',))
            rows = self.cursor.fetchall()
            self.con.close()
            productos = []
            for row in rows:
                producto = Producto(row[0], row[1], row[2], row[3], row[4], row[5])
                productos.append(producto)
            return productos
        except mysql.connector.Error as err:
            print(f"Error al buscar productos: {err}")
            return []

                    
    def get_all_productos(self):
        try:
            self.con = con.conexion()
            self.conn = self.con.open()
            self.cursor = self.conn.cursor()
            self.sql = "SELECT * FROM productos"
            self.cursor.execute(self.sql)
            rows = self.cursor.fetchall()
            self.con.close()
            productos = []
            for row in rows:
                producto = Producto(row[0], row[1], row[2], row[3], row[4], row[5])
                productos.append(producto)
            return productos
        except mysql.connector.Error as err:
            print(f"Error al obtener productos: {err}")
            return []

    def aumentar_stock(self, nombre_producto, cantidad):
        try:
            self.con = con.conexion()
            self.conn = self.con.open()
            self.cursor = self.conn.cursor()
            self.sql = "UPDATE productos SET cantidad_stock = cantidad_stock + %s WHERE nombre_producto = %s"
            self.cursor.execute(self.sql, (cantidad, nombre_producto))
            self.conn.commit()
            self.con.close()
        except mysql.connector.Error as err:
            print(f"Error al aumentar el stock: {err}")

    def get_productos_by_proveedor(self, id_proveedor):
        try:
            self.con = con.conexion()
            self.conn = self.con.open()
            self.cursor = self.conn.cursor()
            self.sql = "SELECT * FROM productos WHERE id_proveedor = %s"
            self.cursor.execute(self.sql, (id_proveedor,))
            rows = self.cursor.fetchall()
            self.con.close()
            productos = []
            for row in rows:
                producto = Producto(row[0], row[1], row[2], row[3], row[4], row[5])
                productos.append(producto)
            return productos
        except mysql.connector.Error as err:
            print(f"Error al obtener productos: {err}")
            return []
        
    def disminuir_stock(self, id_producto, cantidad):
        try:
            self.con = con.conexion()
            self.conn = self.con.open()
            self.cursor = self.conn.cursor()
            self.sql = "UPDATE productos SET cantidad_stock = cantidad_stock - %s WHERE id_producto = %s"
            self.cursor.execute(self.sql, (cantidad, id_producto))
            self.conn.commit()
            self.con.close()
        except mysql.connector.Error as err:
            print(f"Error al disminuir stock: {err}")




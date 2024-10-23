import mysql.connector
from mysql.connector import Error
import conexion as con
from utils.clienteGS import Cliente


class dbClientes:
    def save(self, cliente):
        try:
            self.con = con.conexion()
            self.conn = self.con.open()
            if self.conn is None:
                raise Exception("No se puede conectar a la base de datos")
            self.cursor = self.conn.cursor()
            self.sql = "INSERT INTO clientes (nombre, rfc, puntos_acumulados) VALUES (%s, %s, %s)"
            self.datos = (cliente.getNombre(), cliente.getRfc(), cliente.getPuntosAcumulados())
            self.cursor.execute(self.sql, self.datos)
            self.conn.commit()
            print("Datos insertados correctamente")
        except mysql.connector.Error as err:
            print(f"Error al guardar el cliente: {err}")
        except Exception as e:
            print(f"Error: {e}")
        finally:
            if self.conn is not None and self.conn.is_connected():
                self.cursor.close()
                self.conn.close()

    def search(self, id_cliente):
        try:
            self.con = con.conexion()
            self.conn = self.con.open()
            self.cursor = self.conn.cursor(buffered=True)
            self.sql = "SELECT * FROM clientes WHERE id_cliente = %s"
            self.cursor.execute(self.sql, (id_cliente,))
            row = self.cursor.fetchone()
            self.con.close()
            if row:
                cliente = Cliente(row[0], row[1], row[2], row[3])
                return cliente
            return None
        except mysql.connector.Error as err:
            print(f"Error al buscar el cliente: {err}")
            return None

    def edit(self, cliente):
        try:
            self.con = con.conexion()
            self.conn = self.con.open()
            self.cursor = self.conn.cursor()
            self.sql = "UPDATE clientes SET nombre=%s, rfc=%s, puntos_acumulados=%s WHERE id_cliente=%s"
            self.datos = (cliente.getNombre(), cliente.getRfc(), cliente.getPuntosAcumulados(), cliente.getIdCliente())
            self.cursor.execute(self.sql, self.datos)
            self.conn.commit()
            self.con.close()
        except mysql.connector.Error as err:
            print(f"Error al editar el cliente: {err}")

    def remov(self, id_cliente):
        try:
            self.con = con.conexion()
            self.conn = self.con.open()
            self.cursor = self.conn.cursor()
            self.sql = "DELETE FROM clientes WHERE id_cliente=%s"
            self.cursor.execute(self.sql, (id_cliente,))
            self.conn.commit()
            self.con.close()
        except mysql.connector.Error as err:
            print(f"Error al eliminar el cliente: {err}")

    def getMaxId(self):
        try:
            self.con = con.conexion()
            self.conn = self.con.open()
            self.cursor = self.conn.cursor()
            self.sql = "SELECT MAX(id_cliente) FROM clientes"
            self.cursor.execute(self.sql)
            row = self.cursor.fetchone()
            self.con.close()
            return row[0] if row[0] is not None else 0
        except mysql.connector.Error as err:
            print(f"Error al obtener el maximo ID: {err}")
            return 0


    def get_all_clientes(self):
        try:
            self.con = con.conexion()
            self.conn = self.con.open()
            self.cursor = self.conn.cursor()
            self.sql = "SELECT * FROM clientes"
            self.cursor.execute(self.sql)
            rows = self.cursor.fetchall()
            self.con.close()
            clientes = []
            for row in rows:
                cliente = Cliente(row[0], row[1], row[2], row[3])
                clientes.append(cliente)
            return clientes
        except mysql.connector.Error as err:
            print(f"Error al obtener clientes: {err}")
            return []

    
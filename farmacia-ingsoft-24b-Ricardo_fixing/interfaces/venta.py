import tkinter as tk
from tkinter import ttk, messagebox
from backend.productodb import dbProductos
from backend.clientesdb import dbClientes
import datetime

class Venta(tk.Toplevel):
    
    def __init__(self, parent):
        
        super().__init__(parent)
        self.title('Venta de Productos')
        self.geometry('1200x600')
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(2, weight=1)

        # Frame para el entry
        self.frameEntradaDeDatos = tk.Frame(self)
        self.frameEntradaDeDatos.grid(row=1, column=1, padx=10, pady=10)

        # Primera fila
        tk.Label(self.frameEntradaDeDatos, text='Folio:').grid(row=0, column=0, padx=5, pady=5)
        self.folio_entry = tk.Entry(self.frameEntradaDeDatos)
        self.folio_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(self.frameEntradaDeDatos, text='Fecha:').grid(row=0, column=2, padx=5, pady=5)
        self.fecha_entry = tk.Entry(self.frameEntradaDeDatos)
        self.fecha_entry.grid(row=0, column=3, padx=5, pady=5)

        # Segunda fila
        tk.Label(self.frameEntradaDeDatos, text='Buscar Producto:').grid(row=1, column=0, padx=5, pady=5)
        self.producto_entry = tk.Entry(self.frameEntradaDeDatos)
        self.producto_entry.grid(row=1, column=1, padx=5, pady=5)
        self.buscar_button = tk.Button(self.frameEntradaDeDatos, text='Buscar', command=self.buscar_producto)
        self.buscar_button.grid(row=1, column=2, padx=5, pady=5)

        # Tercera fila
        tk.Label(self.frameEntradaDeDatos, text='Código:').grid(row=2, column=0, padx=5, pady=5)
        self.codigo_entry = tk.Entry(self.frameEntradaDeDatos)
        self.codigo_entry.grid(row=2, column=1, padx=5, pady=5)

        # Cuarta fila
        tk.Label(self.frameEntradaDeDatos, text='Nombre de Producto:').grid(row=3, column=0, padx=5, pady=5)
        self.nombre_entry = tk.Entry(self.frameEntradaDeDatos)
        self.nombre_entry.grid(row=3, column=1, padx=5, pady=5)

        # Quinta fila
        tk.Label(self.frameEntradaDeDatos, text='Descripción:').grid(row=4, column=0, padx=5, pady=5)
        self.descripcion_entry = tk.Entry(self.frameEntradaDeDatos)
        self.descripcion_entry.grid(row=4, column=1, padx=5, pady=5)

        # Sexta fila
        tk.Label(self.frameEntradaDeDatos, text='Precio:').grid(row=5, column=0, padx=5, pady=5)
        self.precio_entry = tk.Entry(self.frameEntradaDeDatos)
        self.precio_entry.grid(row=5, column=1, padx=5, pady=5)

        # Séptima fila
        tk.Label(self.frameEntradaDeDatos, text='Stock:').grid(row=6, column=0, padx=5, pady=5)
        self.stock_entry = tk.Entry(self.frameEntradaDeDatos)
        self.stock_entry.grid(row=6, column=1, padx=5, pady=5)

        # Octava fila
        tk.Label(self.frameEntradaDeDatos, text='Cantidad:').grid(row=7, column=0, padx=5, pady=5)
        self.cantidad_entry = tk.Entry(self.frameEntradaDeDatos)
        self.cantidad_entry.grid(row=7, column=1, padx=5, pady=5)

        # Frame para botones
        self.frameBotones = tk.Frame(self)
        self.frameBotones.grid(row=3, column=1, padx=10, pady=10, sticky='ew')

        self.agregar_button = tk.Button(self.frameBotones, text='Agregar', command=self.agregar_producto)
        self.agregar_button.grid(row=0, column=0, padx=5, pady=5)

        self.quitar_button = tk.Button(self.frameBotones, text='Quitar', command=self.quitar_producto)
        self.quitar_button.grid(row=0, column=1, padx=5, pady=5)

        self.cancelar_button = tk.Button(self.frameBotones, text='Cancelar Venta', command=self.cancelar_venta)
        self.cancelar_button.grid(row=0, column=2, padx=5, pady=5)

        self.frameBotones.grid_columnconfigure(0, weight=1)
        self.frameBotones.grid_columnconfigure(1, weight=1)
        self.frameBotones.grid_columnconfigure(2, weight=1)

        # Cuadro para Cliente
        self.cliente_frame = tk.LabelFrame(self, text='Cliente')
        self.cliente_frame.grid(row=0, column=6, rowspan=8, padx=10, pady=5, sticky='nsew')

        tk.Label(self.cliente_frame, text='Codigo del cliente:').grid(row=0, column=0, padx=5, pady=5)
        self.nombre_cliente_entry = tk.Entry(self.cliente_frame)
        self.nombre_cliente_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(self.cliente_frame, text='Seleccionar Cliente:').grid(row=1, column=0, padx=5, pady=5)
        self.clientes_combo = ttk.Combobox(self.cliente_frame)
        self.clientes_combo.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(self.cliente_frame, text='RFC:').grid(row=2, column=0, padx=5, pady=5)
        self.rfc_entry = tk.Entry(self.cliente_frame)
        self.rfc_entry.grid(row=2, column=1, padx=5, pady=5)

        # Frame para tabla
        self.frameTabla = tk.Frame(self)
        self.frameTabla.grid(row=2, column=1, padx=10, pady=10)
        columns = ('#1', '#2', '#3', '#4', '$5')
        self.tree = ttk.Treeview(self.frameTabla, columns=columns, show='headings')
        self.tree.heading('#1', text='Codigo')
        self.tree.heading('#2', text='Descripcion')
        self.tree.heading('#3', text='Precio Unitario')
        self.tree.heading('#4', text='Cantidad')
        self.tree.heading('#5', text='Precio Total')
        self.tree.column('#1', width=150)
        self.tree.column('#2', width=150)
        self.tree.column('#3', width=150)
        self.tree.column('#4', width=150)
        self.tree.column('#5', width=150)
        self.tree.grid(row=5, column=0, columnspan=5, padx=5, pady=5, sticky='nsew')

        self.cargar_clientes()
        self.buscar_button.config(command=self.buscar_producto)
        self.agregar_button.config(command=self.agregar_producto)
        self.quitar_button.config(command=self.quitar_producto)
        self.cancelar_button.config(command=self.cancelar_venta)
        self.productos_vendidos = []




    def inicializar(self):
        self.folio_entry.insert(0, "1")  # Inicializa el folio
        self.fecha_entry.insert(0, datetime.datetime.now().strftime("%Y-%m-%d"))
        self.cargar_clientes()


    def cargar_clientes(self):
        db_clientes = dbClientes()
        clientes = db_clientes.get_all_clientes()
        self.clientes_combo['values'] = [cliente.getNombre() for cliente in clientes]
        if not clientes:
            messagebox.showerror("Error", "No hay clientes registrados")

    """     def buscar_producto(self):
            producto_nombre = self.producto_entry.get()
            db_productos = dbProductos()
            producto = db_productos.search_by_name(producto_nombre)
            if producto:
                self.codigo_entry.delete(0, tk.END)
                self.codigo_entry.insert(0, producto.getId_producto())
                self.nombre_entry.delete(0, tk.END)
                self.nombre_entry.insert(0, producto.getNombre_producto())
                self.descripcion_entry.delete(0, tk.END)
                self.descripcion_entry.insert(0, producto.getDescripcion())
                self.precio_entry.delete(0, tk.END)
                self.precio_entry.insert(0, producto.getPrecio())
                self.stock_entry.delete(0, tk.END)
                self.stock_entry.insert(0, producto.getCantidad_stock())
            else:
                messagebox.showerror("Error", "Producto no encontrado") """

    def buscar_producto(self):
        producto_nombre = self.producto_entry.get()
        db_productos = dbProductos()
        productos = db_productos.search_by_name(producto_nombre)
        if productos:
            producto = productos[0]  # Asume el primer producto de la lista
            self.codigo_entry.delete(0, tk.END)
            self.codigo_entry.insert(0, producto.getId_producto())
            self.nombre_entry.delete(0, tk.END)
            self.nombre_entry.insert(0, producto.getNombre_producto())
            self.descripcion_entry.delete(0, tk.END)
            self.descripcion_entry.insert(0, producto.getDescripcion())
            self.precio_entry.delete(0, tk.END)
            self.precio_entry.insert(0, producto.getPrecio())
            self.stock_entry.delete(0, tk.END)
            self.stock_entry.insert(0, producto.getCantidad_stock())
        else:
            messagebox.showerror("Error", "Producto no encontrado")


    """     def agregar_producto(self):
            codigo = self.codigo_entry.get()
            nombre = self.nombre_entry.get()
            descripcion = self.descripcion_entry.get()
            precio = self.precio_entry.get()
            stock = self.stock_entry.get()
            cantidad = self.cantidad_entry.get()

            if not codigo or not nombre or not descripcion or not precio or not stock or not cantidad:
                messagebox.showerror("Error", "Todos los campos son obligatorios")
                return

            if int(cantidad) > int(stock):
                messagebox.showerror("Error", "La cantidad excede el stock disponible")
                return

            precio_total = float(precio) * int(cantidad)

            # Buscar si el producto ya está en el carrito
            for row in self.tree.get_children():
                item = self.tree.item(row)
                if item['values'][0] == codigo:
                    nueva_cantidad = int(item['values'][3]) + int(cantidad)
                    nuevo_precio_total = float(precio) * nueva_cantidad
                    self.tree.item(row, values=(codigo, descripcion, precio, nueva_cantidad, nuevo_precio_total))
                    return

            self.tree.insert('', 'end', values=(codigo, descripcion, precio, cantidad, precio_total))

            self.codigo_entry.delete(0, tk.END)
            self.nombre_entry.delete(0, tk.END)
            self.descripcion_entry.delete(0, tk.END)
            self.precio_entry.delete(0, tk.END)
            self.stock_entry.delete(0, tk.END)
            self.cantidad_entry.delete(0, tk.END) """
    def agregar_producto(self):
        codigo = self.codigo_entry.get()
        nombre = self.nombre_entry.get()
        descripcion = self.descripcion_entry.get()
        precio = self.precio_entry.get()
        stock = self.stock_entry.get()
        cantidad = self.cantidad_entry.get()

        if not codigo or not nombre or not descripcion or not precio or not stock or not cantidad:
            messagebox.showerror("Error", "Todos los campos son obligatorios")
            return

        if int(cantidad) > int(stock):
            messagebox.showerror("Error", "La cantidad excede el stock disponible")
            return

        precio_total = float(precio) * int(cantidad)

        # Actualizar el stock en la base de datos
        db_productos = dbProductos()
        db_productos.disminuir_stock(codigo, int(cantidad))

        # Buscar si el producto ya está en el carrito
        for row in self.tree.get_children():
            item = self.tree.item(row)
            if item['values'][0] == codigo:
                nueva_cantidad = int(item['values'][3]) + int(cantidad)
                nuevo_precio_total = float(precio) * nueva_cantidad
                self.tree.item(row, values=(codigo, descripcion, precio, nueva_cantidad, nuevo_precio_total))
                return

        self.tree.insert('', 'end', values=(codigo, descripcion, precio, cantidad, precio_total))

        self.codigo_entry.delete(0, tk.END)
        self.nombre_entry.delete(0, tk.END)
        self.descripcion_entry.delete(0, tk.END)
        self.precio_entry.delete(0, tk.END)
        self.stock_entry.delete(0, tk.END)
        self.cantidad_entry.delete(0, tk.END)
        self.productos_vendidos.append((codigo, cantidad))


    def quitar_producto(self):
        selected_item = self.tree.selection()
        if selected_item:
            self.tree.delete(selected_item)
    def cancelar_venta(self):
        db_productos = dbProductos()
        for producto in self.productos_vendidos:
            db_productos.aumentar_stock(producto[0], producto[1])  # Restaurar el stock en la base de datos

        for row in self.tree.get_children():
            self.tree.delete(row)

        self.codigo_entry.delete(0, tk.END)
        self.nombre_entry.delete(0, tk.END)
        self.descripcion_entry.delete(0, tk.END)
        self.precio_entry.delete(0, tk.END)
        self.stock_entry.delete(0, tk.END)
        self.cantidad_entry.delete(0, tk.END)

        self.productos_vendidos = []  # Vaciar la lista de productos vendidos
        messagebox.showinfo("Éxito", "Venta cancelada")




    # def open_carrito(self):
    #     carrito_window = Carrito(self)

import tkinter as tk
from tkinter import messagebox
from backend.productodb import dbProductos 
from utils.productoGS import Producto

class ProductoCRUD(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Gestión de Productos")
        self.geometry("800x600")
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.user_id = None  # Para manejar ID de usuario si es necesario

        # Frame para buscar
        self.frameBuscar = tk.Frame(self)
        self.frameBuscar.grid(row=0, column=1, padx=10, pady=10)
        # Campo de búsqueda
        self.buscar_label = tk.Label(self.frameBuscar, text="Buscar Producto")
        self.buscar_label.grid(row=0, column=0, padx=10, pady=10)
        self.txBuscarProducto = tk.Entry(self.frameBuscar)
        self.txBuscarProducto.grid(row=0, column=1, padx=10, pady=10)
        self.btBuscar = tk.Button(self.frameBuscar, text="Buscar", command=self.buscar_producto)
        self.btBuscar.grid(row=0, column=2, padx=10, pady=10)

        # Frame para entrada de datos
        self.frameEntradaDeDatos = tk.Frame(self)
        self.frameEntradaDeDatos.grid(row=1, column=1, padx=10, pady=10)
        # Campos de entrada
        self.id_label = tk.Label(self.frameEntradaDeDatos, text="ID")
        self.id_label.grid(row=0, column=0, padx=10, pady=10)
        self.txId = tk.Entry(self.frameEntradaDeDatos)
        self.txId.grid(row=0, column=1, padx=10, pady=10)
        self.nombre_label = tk.Label(self.frameEntradaDeDatos, text="Nombre del Producto")
        self.nombre_label.grid(row=1, column=0, padx=10, pady=10)
        self.txNombre = tk.Entry(self.frameEntradaDeDatos)
        self.txNombre.grid(row=1, column=1, padx=10, pady=10)
        self.descripcion_label = tk.Label(self.frameEntradaDeDatos, text="Descripción")
        self.descripcion_label.grid(row=2, column=0, padx=10, pady=10)
        self.txDescripcion = tk.Entry(self.frameEntradaDeDatos)
        self.txDescripcion.grid(row=2, column=1, padx=10, pady=10)
        self.precio_label = tk.Label(self.frameEntradaDeDatos, text="Precio")
        self.precio_label.grid(row=3, column=0, padx=10, pady=10)
        self.txPrecio = tk.Entry(self.frameEntradaDeDatos)
        self.txPrecio.grid(row=3, column=1, padx=10, pady=10)
        self.cantidad_label = tk.Label(self.frameEntradaDeDatos, text="Cantidad en Stock")
        self.cantidad_label.grid(row=4, column=0, padx=10, pady=10)
        self.txCantidad = tk.Entry(self.frameEntradaDeDatos)
        self.txCantidad.grid(row=4, column=1, padx=10, pady=10)
        self.proveedor_label = tk.Label(self.frameEntradaDeDatos, text="ID del Proveedor")
        self.proveedor_label.grid(row=5, column=0, padx=10, pady=10)
        self.txProveedor = tk.Entry(self.frameEntradaDeDatos)
        self.txProveedor.grid(row=5, column=1, padx=10, pady=10)

        # Frame para botones
        self.frameBotones = tk.Frame(self)
        self.frameBotones.grid(row=2, column=1, padx=10, pady=10)
        # Botones
        self.btNuevo = tk.Button(self.frameBotones, text="Nuevo", command=self.nuevo_producto)
        self.btNuevo.grid(row=0, column=0, padx=10, pady=10)
        self.btSalvar = tk.Button(self.frameBotones, text="Salvar", command=self.salvar_producto)
        self.btSalvar.grid(row=0, column=1, padx=10, pady=10)
        self.btSalvar.config(state=tk.DISABLED)
        self.btEditar = tk.Button(self.frameBotones, text="Editar", command=self.editar_producto)
        self.btEditar.grid(row=0, column=2, padx=10, pady=10)
        self.btEditar.config(state=tk.DISABLED)
        self.btCancelar = tk.Button(self.frameBotones, text="Cancelar", command=self.cancelar)
        self.btCancelar.grid(row=0, column=3, padx=10, pady=10)
        self.btCancelar.config(state=tk.DISABLED)
        self.btEliminar = tk.Button(self.frameBotones, text="Eliminar", command=self.eliminar_producto)
        self.btEliminar.grid(row=0, column=4, padx=10, pady=10)
        self.btEliminar.config(state=tk.DISABLED)

    def nuevo_producto(self):
        self.txId.delete(0, tk.END)
        self.txNombre.delete(0, tk.END)
        self.txDescripcion.delete(0, tk.END)
        self.txPrecio.delete(0, tk.END)
        self.txCantidad.delete(0, tk.END)
        self.txProveedor.delete(0, tk.END)
        db_productos = dbProductos()
        nuevo_id = db_productos.getMaxId() + 1
        self.txId.insert(0, nuevo_id)
        self.btSalvar.config(state=tk.NORMAL)
        self.btCancelar.config(state=tk.NORMAL)
        self.btEditar.config(state=tk.DISABLED)
        self.btEliminar.config(state=tk.DISABLED)

    def salvar_producto(self):
        id_producto = self.txId.get()
        nombre = self.txNombre.get()
        descripcion = self.txDescripcion.get()
        precio = self.txPrecio.get()
        cantidad_stock = self.txCantidad.get()
        id_proveedor = self.txProveedor.get()
        if not id_producto or not nombre or not descripcion or not precio or not cantidad_stock or not id_proveedor:
            messagebox.showerror("Error", "Todos los campos son obligatorios")
            return
        producto = Producto(id_producto, nombre, descripcion, precio, cantidad_stock, id_proveedor)
        db_productos = dbProductos()
        db_productos.save(producto)
        messagebox.showinfo("Éxito", "Producto guardado exitosamente")
        self.nuevo_producto()

    def cancelar(self):
        self.nuevo_producto()

    def editar_producto(self):
        id_producto = self.txId.get()
        nombre = self.txNombre.get()
        descripcion = self.txDescripcion.get()
        precio = self.txPrecio.get()
        cantidad_stock = self.txCantidad.get()
        id_proveedor = self.txProveedor.get()
        if not id_producto or not nombre or not descripcion or not precio or not cantidad_stock or not id_proveedor:
            messagebox.showerror("Error", "Todos los campos son obligatorios")
            return
        producto = Producto(id_producto, nombre, descripcion, precio, cantidad_stock, id_proveedor)
        db_productos = dbProductos()
        db_productos.edit(producto)
        messagebox.showinfo("Éxito", "Producto editado exitosamente")
        self.nuevo_producto()

    def eliminar_producto(self):
        id_producto = self.txId.get()
        if not id_producto:
            messagebox.showerror("Error", "ID del producto es necesario para eliminar")
            return
        db_productos = dbProductos()
        db_productos.remov(id_producto)
        messagebox.showinfo("Éxito", "Producto eliminado exitosamente")
        self.nuevo_producto()

    def buscar_producto(self):
        id_producto = self.txBuscarProducto.get()
        if not id_producto:
            messagebox.showerror("Error", "ID del producto es necesario para buscar")
            return
        db_productos = dbProductos()
        producto = db_productos.search(id_producto)
        if producto:
            self.txId.delete(0, tk.END)
            self.txId.insert(0, producto.getId_producto())
            self.txNombre.delete(0, tk.END)
            self.txNombre.insert(0, producto.getNombre_producto())
            self.txDescripcion.delete(0, tk.END)
            self.txDescripcion.insert(0, producto.getDescripcion())
            self.txPrecio.delete(0, tk.END)
            self.txPrecio.insert(0, producto.getPrecio())
            self.txCantidad.delete(0, tk.END)
            self.txCantidad.insert(0, producto.getCantidad_stock())
            self.txProveedor.delete(0, tk.END)
            self.txProveedor.insert(0, producto.getId_proveedor())
            self.btEditar.config(state=tk.NORMAL)
            self.btCancelar.config(state=tk.NORMAL)
            self.btEliminar.config(state=tk.NORMAL)
        else:
            messagebox.showerror("Error", "Producto no encontrado")

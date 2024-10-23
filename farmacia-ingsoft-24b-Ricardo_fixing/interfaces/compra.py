import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from backend.productodb import dbProductos
from backend.proveedordb import dbProveedor
import datetime

class Compra(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title('Compra de Productos')
        self.geometry('900x700')
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(2, weight=1)

        # Frame para el entry
        self.frameEntradaDeDatos = tk.Frame(self)
        self.frameEntradaDeDatos.grid(row=1, column=1, padx=10, pady=10)

        # Primera fila
        tk.Label(self.frameEntradaDeDatos, text='Folio:').grid(row=0, column=0, padx=5, pady=5)
        self.txFolio = tk.Entry(self.frameEntradaDeDatos)
        self.txFolio.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(self.frameEntradaDeDatos, text='Fecha:').grid(row=0, column=2, padx=5, pady=5)
        self.fecha_entry = tk.Entry(self.frameEntradaDeDatos, state='readonly')
        self.fecha_entry.grid(row=0, column=3, padx=5, pady=5)
        self.fecha_entry.insert(0, datetime.datetime.now().strftime("%Y-%m-%d"))

        # Segunda fila
        tk.Label(self.frameEntradaDeDatos, text='Proveedor:').grid(row=1, column=0, padx=5, pady=5)
        self.proveedor_combo = ttk.Combobox(self.frameEntradaDeDatos)
        self.proveedor_combo.grid(row=1, column=1, padx=5, pady=5)

        # Tercera fila
        tk.Label(self.frameEntradaDeDatos, text='Producto:').grid(row=2, column=0, padx=5, pady=5)
        self.producto_combo = ttk.Combobox(self.frameEntradaDeDatos)
        self.producto_combo.grid(row=2, column=1, padx=5, pady=5)

        self.agregar_button = tk.Button(self.frameEntradaDeDatos, text='Agregar', command=self.agregar_producto)
        self.agregar_button.grid(row=2, column=2, padx=5, pady=5)

        self.quitar_button = tk.Button(self.frameEntradaDeDatos, text='Quitar', command=self.quitar_producto)
        self.quitar_button.grid(row=2, column=3, padx=5, pady=5)

        # Cuarta fila
        tk.Label(self.frameEntradaDeDatos, text='Precio:').grid(row=3, column=0, padx=5, pady=5)
        self.precio_entry = tk.Entry(self.frameEntradaDeDatos)
        self.precio_entry.grid(row=3, column=1, padx=5, pady=5)

        # Quinta fila
        tk.Label(self.frameEntradaDeDatos, text='Cantidad:').grid(row=4, column=0, padx=5, pady=5)
        self.cantidad_entry = tk.Entry(self.frameEntradaDeDatos)
        self.cantidad_entry.grid(row=4, column=1, padx=5, pady=5)


        # Frame para tabla
        self.frameTabla = tk.Frame(self)
        self.frameTabla.grid(row=2, column=1, padx=10, pady=10)
        columns = ('#1', '#2', '#3', '#4', '#5')
        self.tree = ttk.Treeview(self.frameTabla, columns=columns, show='headings')
        self.tree.heading('#1', text='Código')
        self.tree.heading('#2', text='Nombre')
        self.tree.heading('#3', text='Precio Compra')
        self.tree.heading('#4', text='Cantidad')
        self.tree.heading('#5', text='Precio Total')
        self.tree.column('#1', width=150)
        self.tree.column('#2', width=150)
        self.tree.column('#3', width=150)
        self.tree.column('#4', width=150)
        self.tree.column('#5', width=150)
        self.tree.grid(row=5, column=0, columnspan=5, padx=5, pady=5, sticky='nsew')

        # Botones de acción
        self.frameBotones = tk.Frame(self)
        self.frameBotones.grid(row=3, column=1, padx=10, pady=10)
        self.btNuevo = tk.Button(self.frameBotones, text="Nuevo", command=self.nuevo)
        self.btNuevo.grid(row=0, column=0, padx=10, pady=10)
        self.btSalvar = tk.Button(self.frameBotones, text="Salvar", command=self.salvar)
        self.btSalvar.grid(row=0, column=1, padx=10, pady=10)
        self.btSalvar.config(state=tk.DISABLED)
        self.btCancelar = tk.Button(self.frameBotones, text="Cancelar", command=self.cancelar)
        self.btCancelar.grid(row=0, column=2, padx=10, pady=10)
        self.btCancelar.config(state=tk.DISABLED)
        self.btEliminar = tk.Button(self.frameBotones, text="Eliminar", command=self.eliminar)
        self.btEliminar.grid(row=0, column=3, padx=10, pady=10)
        self.btEliminar.config(state=tk.DISABLED)

        # Inicializar datos
        self.carrito = []
        self.folio_actual = 1
        self.cargar_proveedores()
        self.proveedor_combo.bind("<<ComboboxSelected>>", self.cargar_productos_por_proveedor)

        self.nuevo()
        

    def cargar_proveedores(self):
        db_proveedores = dbProveedor()
        proveedores = db_proveedores.get_all_proveedores()
        self.proveedor_combo['values'] = [proveedor.getNombre() for proveedor in proveedores]
    def cargar_productos_por_proveedor(self, event):
        proveedor_nombre = self.proveedor_combo.get()
        db_proveedores = dbProveedor()
        proveedor = db_proveedores.search_by_name(proveedor_nombre)
        if proveedor:
            db_productos = dbProductos()
            productos = db_productos.get_productos_by_proveedor(proveedor.getId_proveedor())
            self.producto_combo['values'] = [producto.getNombre_producto() for producto in productos]
    def agregar_producto(self):
        producto_nombre = self.producto_combo.get()
        precio_compra = self.precio_entry.get()
        cantidad = self.cantidad_entry.get()

        if not producto_nombre or not precio_compra or not cantidad:
            messagebox.showerror("Error", "Todos los campos son obligatorios")
            return

        precio_total = float(precio_compra) * int(cantidad)
        self.carrito.append((producto_nombre, precio_compra, cantidad, precio_total))

        self.tree.insert('', 'end', values=(len(self.carrito), producto_nombre, precio_compra, cantidad, precio_total))

        self.producto_combo.set('')
        self.precio_entry.delete(0, tk.END)
        self.cantidad_entry.delete(0, tk.END)

    def quitar_producto(self):
        selected_item = self.tree.selection()
        if selected_item:
            self.tree.delete(selected_item)
            del self.carrito[int(selected_item[0])]

    def mostrar_carrito(self):
        if not self.carrito:
            messagebox.showinfo("Carrito", "El carrito está vacío")
        else:
            detalles = "\n".join([f"{producto[0]} - {producto[2]} unidades - Total: ${producto[3]}" for producto in self.carrito])
            messagebox.showinfo("Carrito", f"Productos en el carrito:\n{detalles}")

    def confirmar_compra(self):
        db_productos = dbProductos()
        for producto in self.carrito:
            db_productos.aumentar_stock(producto[0], producto[2])
        messagebox.showinfo("Éxito", "Compra realizada exitosamente")
        self.carrito.clear()
        for row in self.tree.get_children():
            self.tree.delete(row)

    def nuevo(self):
        self.txFolio.delete(0, tk.END)
        self.txFolio.insert(0, self.folio_actual)
        self.folio_actual += 1
        self.fecha_entry.config(state=tk.NORMAL)
        self.fecha_entry.delete(0, tk.END)
        self.fecha_entry.insert(0, datetime.datetime.now().strftime("%Y-%m-%d"))
        self.fecha_entry.config(state='readonly')
        self.btSalvar.config(state=tk.NORMAL)
        self.btCancelar.config(state=tk.NORMAL)
        self.btEliminar.config(state=tk.DISABLED)

    def salvar(self):
        self.confirmar_compra()
        self.nuevo()

    def cancelar(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        self.carrito.clear()
        self.nuevo()

    def eliminar(self):
        selected_item = self.tree.selection()
        if selected_item:
            self.tree.delete(selected_item)
            del self.carrito[int(selected_item[0])]
        messagebox.showinfo("Éxito", "Producto eliminado del carrito")

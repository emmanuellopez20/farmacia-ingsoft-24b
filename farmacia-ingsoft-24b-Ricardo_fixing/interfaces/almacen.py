import tkinter as tk
from tkinter import messagebox, ttk
from backend.productodb import dbProductos


class Almacen(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title('Gestión de Almacén')
        self.geometry("900x700")
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(2, weight=1)

        # Primera fila
        tk.Label(self, text='Producto:').grid(row=0, column=0, padx=5, pady=5)
        self.producto_entry = tk.Entry(self)
        self.producto_entry.grid(row=0, column=1, padx=5, pady=5)

        self.buscar_button = tk.Button(self, text='Buscar', command=self.buscar_producto)
        self.buscar_button.grid(row=0, column=2, padx=5, pady=5)

        # Tabla de doble entrada
        self.tree = ttk.Treeview(self, columns=('Código', 'Nombre', 'Descripción', 'Proveedor', 'Stock', 'Precio Unitario'), show='headings')
        self.tree.heading('Código', text='Código')
        self.tree.heading('Nombre', text='Nombre')
        self.tree.heading('Descripción', text='Descripción')
        self.tree.heading('Proveedor', text='Proveedor')
        self.tree.heading('Stock', text='Stock')
        self.tree.heading('Precio Unitario', text='Precio Unitario')
        self.tree.grid(row=1, column=0, columnspan=6, padx=5, pady=5)

        # Botones en la última fila
        self.salir_button = tk.Button(self, text='Salir', command=self.destroy)
        self.salir_button.grid(row=2, column=4, padx=5, pady=5, sticky='e')

        self.borrar_busqueda_button = tk.Button(self, text='Borrar Búsqueda', command=self.borrar_busqueda)
        self.borrar_busqueda_button.grid(row=2, column=5, padx=5, pady=5, sticky='e')

    def buscar_producto(self):
        producto_nombre = self.producto_entry.get()
        if not producto_nombre:
            messagebox.showerror("Error", "Ingrese el nombre del producto para buscar")
            return
        db_productos = dbProductos()
        productos = db_productos.search_by_name(producto_nombre)
        for row in self.tree.get_children():
            self.tree.delete(row)
        for producto in productos:
            self.tree.insert('', 'end', values=(producto.getId_producto(), producto.getNombre_producto(), producto.getDescripcion(), producto.getId_proveedor(), producto.getCantidad_stock(), producto.getPrecio()))

    def borrar_busqueda(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        self.producto_entry.delete(0, tk.END)

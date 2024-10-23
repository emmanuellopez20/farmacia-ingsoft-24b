import tkinter as tk
from tkinter import ttk

class Compra(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title('Compra de Productos')
        self.geometry('900x700')

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(2, weight=1)

        #Frame para el entry
        self.frameEntradaDeDatos = tk.Frame(self)
        self.frameEntradaDeDatos.grid(row=1, column=1, padx=10, pady=10)
        
        # Primera fila
        tk.Label(self.frameEntradaDeDatos, text='Folio:').grid(row=0, column=0, padx=5, pady=5)
        self.txFolio = tk.Entry(self.frameEntradaDeDatos)
        self.txFolio.grid(row=0, column=1, padx=5, pady=5)
        
        tk.Label(self.frameEntradaDeDatos, text='Fecha:').grid(row=0, column=2, padx=5, pady=5)
        self.fecha_entry = tk.Entry(self.frameEntradaDeDatos)
        self.fecha_entry.grid(row=0, column=3, padx=5, pady=5)
        
        # Segunda fila
        tk.Label(self.frameEntradaDeDatos, text='Proveedor:').grid(row=1, column=0, padx=5, pady=5)
        self.proveedor_combo = ttk.Combobox(self.frameEntradaDeDatos)
        self.proveedor_combo.grid(row=1, column=1, padx=5, pady=5)
        
        # Tercera fila
        tk.Label(self.frameEntradaDeDatos, text='Producto:').grid(row=2, column=0, padx=5, pady=5)
        self.producto_combo = ttk.Combobox(self.frameEntradaDeDatos)
        self.producto_combo.grid(row=2, column=1, padx=5, pady=5)
        
        self.agregar_button = tk.Button(self.frameEntradaDeDatos, text='Agregar')
        self.agregar_button.grid(row=2, column=2, padx=5, pady=5)
        
        self.quitar_button = tk.Button(self.frameEntradaDeDatos, text='Quitar')
        self.quitar_button.grid(row=2, column=3, padx=5, pady=5)
        
        # Cuarta fila
        tk.Label(self.frameEntradaDeDatos, text='Precio:').grid(row=3, column=0, padx=5, pady=5)
        self.precio_entry = tk.Entry(self.frameEntradaDeDatos)
        self.precio_entry.grid(row=3, column=1, padx=5, pady=5)
        
        # Quinta fila
        tk.Label(self.frameEntradaDeDatos, text='Cantidad:').grid(row=4, column=0, padx=5, pady=5)
        self.cantidad_entry = tk.Entry(self.frameEntradaDeDatos)
        self.cantidad_entry.grid(row=4, column=1, padx=5, pady=5)

        # Botón Carrito
        self.carrito_button = tk.Button(self.frameEntradaDeDatos, text='Carrito')
        self.carrito_button.grid(row=0, column=4, padx=5, pady=5, sticky='e')
        # self.carrito_button.configure(command=self.open_carrito)

        #Frame para tabla
        self.frameTabla = tk.Frame(self)
        self.frameTabla.grid(row=2, column=1, padx=10, pady=10)


        columns = ('#1', '#2', '#3', '#4', '$5')

        self.tree = ttk.Treeview(self.frameTabla, columns=columns, show='headings')

        self.tree.heading('#1', text='Codigo')
        self.tree.heading('#2', text='Nombre')
        self.tree.heading('#3', text='Precio Unitario')
        self.tree.heading('#4', text='Cantidad')
        self.tree.heading('#5', text='Precio Total')

        self.tree.column('#1', width=150)
        self.tree.column('#2', width=150)
        self.tree.column('#3', width=150)
        self.tree.column('#4', width=150)
        self.tree.column('#5', width=150)

        self.tree.grid(row=5, column=0, columnspan=5, padx=5, pady=5, sticky='nsew')


    # def open_carrito(self):
    #     carrito_window = Carrito(self)


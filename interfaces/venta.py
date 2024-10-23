import tkinter as tk
from tkinter import ttk

class Venta(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title('Venta de Productos')
        self.geometry('1200x600')

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(2, weight=1)

        #Frame para el entry
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
        
        self.buscar_button = tk.Button(self.frameEntradaDeDatos, text='Buscar')
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

        #Frame para botones
        self.frameBotones = tk.Frame(self)
        self.frameBotones.grid(row=2, column=1, padx=10, pady=10)
        
        self.agregar_button = tk.Button(self.frameBotones, text='Agregar')
        self.agregar_button.grid(row=7, column=2, padx=5, pady=5)
        
        self.quitar_button = tk.Button(self.frameBotones, text='Quitar')
        self.quitar_button.grid(row=7, column=3, padx=5, pady=5)
        
        self.cancelar_button = tk.Button(self.frameBotones, text='Cancelar Venta')
        self.cancelar_button.grid(row=7, column=4, padx=5, pady=5)

        # # Botón Carrito
        # self.carrito_button = tk.Button(self.frameBotones, text='Carrito')
        # self.carrito_button.grid(row=0, column=5, padx=5, pady=5, sticky='e')
        # self.carrito_button.configure(command=self.open_carrito)


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

        #Frame para tabla
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



    # def open_carrito(self):
    #     carrito_window = Carrito(self)

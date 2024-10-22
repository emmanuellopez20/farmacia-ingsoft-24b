import tkinter as tk
from tkinter import ttk

class Carrito(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title('Carrito de Compras')

        # Crear tabla
        self.tree = ttk.Treeview(self, columns=('Código', 'Nombre', 'Precio Unitario', 'Cantidad', 'Precio Total'), show='headings')
        self.tree.heading('Código', text='Código')
        self.tree.heading('Nombre', text='Nombre')
        self.tree.heading('Precio Unitario', text='Precio Unitario')
        self.tree.heading('Cantidad', text='Cantidad')
        self.tree.heading('Precio Total', text='Precio Total')
        self.tree.grid(row=0, column=0, columnspan=5, padx=5, pady=5)
        
        # Campos de Subtotal, IVA y Total
        tk.Label(self, text='Subtotal:').grid(row=1, column=3, padx=5, pady=5)
        self.subtotal_entry = tk.Entry(self)
        self.subtotal_entry.grid(row=1, column=4, padx=5, pady=5)
        
        tk.Label(self, text='IVA:').grid(row=2, column=3, padx=5, pady=5)
        self.iva_entry = tk.Entry(self)
        self.iva_entry.grid(row=2, column=4, padx=5, pady=5)
        
        tk.Label(self, text='Total:').grid(row=3, column=3, padx=5, pady=5)
        self.total_entry = tk.Entry(self)
        self.total_entry.grid(row=3, column=4, padx=5, pady=5)

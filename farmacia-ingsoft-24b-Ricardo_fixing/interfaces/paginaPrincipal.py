import tkinter as tk
from tkinter import ttk
from interfaces.venta import Venta
from interfaces.compra import Compra
from interfaces.proveedor_crud import ProveedorCRUD
from interfaces.almacen import Almacen
from interfaces.cliente_crud import ClienteCRUD
from interfaces.producto_crud import ProductoCRUD

class PuntoDeVentaApp(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title('Punto de Venta')
        self.geometry('400x300')
        
        # Menú principal
        menubar = tk.Menu(self)
        self.config(menu=menubar)
        
        archivo_menu = tk.Menu(menubar, tearoff=0)
        archivo_menu.add_command(label="Venta", command=self.open_venta)
        archivo_menu.add_command(label="Compra", command=self.open_compra)
        archivo_menu.add_command(label="Gestión de Proveedores", command=self.open_proveedor_crud)
        archivo_menu.add_command(label="Almacén", command=self.open_almacen)
        archivo_menu.add_command(label="Gestión de Clientes", command=self.open_cliente_crud)
        # archivo_menu.add_command(label="Carrito", command=self.open_carrito)
        archivo_menu.add_command(label="Gestión de Productos", command=self.open_producto_crud)
        archivo_menu.add_separator()
        archivo_menu.add_command(label="Salir", command=self.quit)
        menubar.add_cascade(label="Archivo", menu=archivo_menu)

    def open_venta(self):
        venta_window = Venta(self)

    def open_compra(self):
        compra_window = Compra(self)

    def open_proveedor_crud(self):
        proveedor_crud_window = ProveedorCRUD(self)

    def open_almacen(self):
        almacen_window = Almacen(self)

    def open_cliente_crud(self):
        cliente_crud_window = ClienteCRUD(self)

    def open_producto_crud(self):
        producto_crud_window = ProductoCRUD(self)
     
    
    # def open_carrito(self):
    #     carrito_window = Carrito(self)

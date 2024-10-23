import tkinter as tk
from tkinter import ttk

class ProveedorCRUD(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Gestión de Proveedores")
        self.geometry("800x600")

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(2, weight=1)

        #Frame para buscar
        self.frameBuscar = tk.Frame(self)
        self.frameBuscar.grid(row=0, column=1, padx=10, pady=10)

        # Campo de búsqueda
        self.buscar_label = tk.Label(self.frameBuscar, text="Buscar Proveedor")
        self.buscar_label.grid(row=0, column=0, padx=10, pady=10)
        self.txBuscarProveedor = tk.Entry(self.frameBuscar)
        self.txBuscarProveedor.grid(row=0, column=1, padx=10, pady=10)
        self.btBuscar = tk.Button(self.frameBuscar, text="Buscar", command=self.buscar_proveedor)
        self.btBuscar.grid(row=0, column=2, padx=10, pady=10)

        #Frame para entrada de datos
        self.frameEntradaDeDatos = tk.Frame(self)
        self.frameEntradaDeDatos.grid(row=1, column=1, padx=10, pady=10)

        # Campos de entrada
        self.nombre_label = tk.Label( self.frameEntradaDeDatos, text="Nombre del Proveedor")
        self.nombre_label.grid(row=0, column=0, padx=10, pady=10)
        self.txNombre = tk.Entry( self.frameEntradaDeDatos)
        self.txNombre.grid(row=0, column=1, padx=10, pady=10)

        self.direccion_label = tk.Label( self.frameEntradaDeDatos, text="Dirección")
        self.direccion_label.grid(row=1, column=0, padx=10, pady=10)
        self.txDireccion = tk.Entry( self.frameEntradaDeDatos)
        self.txDireccion.grid(row=1, column=1, padx=10, pady=10)

        self.telefono_label = tk.Label( self.frameEntradaDeDatos, text="Teléfono")
        self.telefono_label.grid(row=2, column=0, padx=10, pady=10)
        self.txTelefono = tk.Entry( self.frameEntradaDeDatos)
        self.txTelefono.grid(row=2, column=1, padx=10, pady=10)

        self.email_label = tk.Label( self.frameEntradaDeDatos, text="Email")
        self.email_label.grid(row=3, column=0, padx=10, pady=10)
        self.txEmail = tk.Entry( self.frameEntradaDeDatos)
        self.txEmail.grid(row=3, column=1, padx=10, pady=10)

        #Frame para botones
        self.frameBotones = tk.Frame(self)
        self.frameBotones.grid(row=2, column=1, padx=10, pady=10)

        # Botones
        self.btNuevo = tk.Button(self.frameBotones, text="Nuevo", command=self.nuevo_proveedor)
        self.btNuevo.grid(row=0, column=0, padx=10, pady=10)

        self.btSalvar = tk.Button(self.frameBotones, text="Salvar", command=self.salvar_proveedor)
        self.btSalvar.grid(row=0, column=1, padx=10, pady=10)
        self.btSalvar.config(state=tk.DISABLED)

        self.btEditar = tk.Button(self.frameBotones, text="Editar", command=self.editar_proveedor)
        self.btEditar.grid(row=0, column=2, padx=10, pady=10)
        self.btEditar.config(state=tk.DISABLED)

        self.btCancelar = tk.Button(self.frameBotones, text="Cancelar", command=self.cancelar)
        self.btCancelar.grid(row=0, column=3, padx=10, pady=10)
        self.btCancelar.config(state=tk.DISABLED)

        self.btEliminar = tk.Button(self.frameBotones, text="Eliminar", command=self.eliminar_proveedor)
        self.btEliminar.grid(row=0, column=4, padx=10, pady=10)
        self.btEliminar.config(state=tk.DISABLED)

       

    def nuevo_proveedor(self):
        # Implementación de lógica para nuevo proveedor
        pass

    def salvar_proveedor(self):
        # Implementación de lógica para salvar proveedor
        pass

    def editar_proveedor(self):
        # Implementación de lógica para editar proveedor
        pass

    def cancelar(self):
        # Implementación de lógica para cancelar la operación
        pass

    def eliminar_proveedor(self):
        # Implementación de lógica para eliminar proveedor
        pass

    def buscar_proveedor(self):
        # Implementación de lógica para buscar proveedor
        pass

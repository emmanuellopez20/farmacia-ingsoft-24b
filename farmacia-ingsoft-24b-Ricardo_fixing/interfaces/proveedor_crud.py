import tkinter as tk
from tkinter import messagebox
from backend.proveedordb import dbProveedor
from utils.proveedorGS import Proveedor

class ProveedorCRUD(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Gestión de Proveedores")
        self.geometry("800x600")
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.user_id = None  # Para manejar ID de usuario si es necesario

        # Frame para buscar
        self.frameBuscar = tk.Frame(self)
        self.frameBuscar.grid(row=0, column=1, padx=10, pady=10)
        # Campo de búsqueda
        self.buscar_label = tk.Label(self.frameBuscar, text="Buscar Proveedor")
        self.buscar_label.grid(row=0, column=0, padx=10, pady=10)
        self.txBuscarProveedor = tk.Entry(self.frameBuscar)
        self.txBuscarProveedor.grid(row=0, column=1, padx=10, pady=10)
        self.btBuscar = tk.Button(self.frameBuscar, text="Buscar", command=self.buscar_proveedor)
        self.btBuscar.grid(row=0, column=2, padx=10, pady=10)

        # Frame para entrada de datos
        self.frameEntradaDeDatos = tk.Frame(self)
        self.frameEntradaDeDatos.grid(row=1, column=1, padx=10, pady=10)
        # Campos de entrada
        self.id_label = tk.Label(self.frameEntradaDeDatos, text="ID")
        self.id_label.grid(row=0, column=0, padx=10, pady=10)
        self.txId = tk.Entry(self.frameEntradaDeDatos)
        self.txId.grid(row=0, column=1, padx=10, pady=10)
        self.nombre_label = tk.Label(self.frameEntradaDeDatos, text="Nombre del Proveedor")
        self.nombre_label.grid(row=1, column=0, padx=10, pady=10)
        self.txNombre = tk.Entry(self.frameEntradaDeDatos)
        self.txNombre.grid(row=1, column=1, padx=10, pady=10)
        self.direccion_label = tk.Label(self.frameEntradaDeDatos, text="Dirección")
        self.direccion_label.grid(row=2, column=0, padx=10, pady=10)
        self.txDireccion = tk.Entry(self.frameEntradaDeDatos)
        self.txDireccion.grid(row=2, column=1, padx=10, pady=10)
        self.telefono_label = tk.Label(self.frameEntradaDeDatos, text="Teléfono")
        self.telefono_label.grid(row=3, column=0, padx=10, pady=10)
        self.txTelefono = tk.Entry(self.frameEntradaDeDatos)
        self.txTelefono.grid(row=3, column=1, padx=10, pady=10)
        self.email_label = tk.Label(self.frameEntradaDeDatos, text="Email")
        self.email_label.grid(row=4, column=0, padx=10, pady=10)
        self.txEmail = tk.Entry(self.frameEntradaDeDatos)
        self.txEmail.grid(row=4, column=1, padx=10, pady=10)

        # Frame para botones
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
        self.txId.delete(0, tk.END)
        self.txNombre.delete(0, tk.END)
        self.txDireccion.delete(0, tk.END)
        self.txTelefono.delete(0, tk.END)
        self.txEmail.delete(0, tk.END)
        db_proveedores = dbProveedor()
        nuevo_id = db_proveedores.getMaxId() + 1
        self.txId.insert(0, nuevo_id)
        self.btSalvar.config(state=tk.NORMAL)
        self.btCancelar.config(state=tk.NORMAL)
        self.btEditar.config(state=tk.DISABLED)
        self.btEliminar.config(state=tk.DISABLED)

    def salvar_proveedor(self):
        id_proveedor = self.txId.get()
        nombre = self.txNombre.get()
        direccion = self.txDireccion.get()
        telefono = self.txTelefono.get()
        email = self.txEmail.get()
        if not id_proveedor or not nombre or not direccion or not telefono or not email:
            messagebox.showerror("Error", "Todos los campos son obligatorios")
            return
        proveedor = Proveedor(id_proveedor, nombre, telefono, direccion, email)
        db_proveedores = dbProveedor()
        db_proveedores.save(proveedor)
        messagebox.showinfo("Éxito", "Proveedor guardado exitosamente")
        self.nuevo_proveedor()

    def cancelar(self):
        self.nuevo_proveedor()

    def editar_proveedor(self):
        id_proveedor = self.txId.get()
        nombre = self.txNombre.get()
        direccion = self.txDireccion.get()
        telefono = self.txTelefono.get()
        email = self.txEmail.get()
        if not id_proveedor or not nombre or not direccion or not telefono or not email:
            messagebox.showerror("Error", "Todos los campos son obligatorios")
            return
        proveedor = Proveedor(id_proveedor, nombre, telefono, direccion, email)
        db_proveedores = dbProveedor()
        db_proveedores.edit(proveedor)
        messagebox.showinfo("Éxito", "Proveedor editado exitosamente")
        self.nuevo_proveedor()

    def eliminar_proveedor(self):
        id_proveedor = self.txId.get()
        if not id_proveedor:
            messagebox.showerror("Error", "ID del proveedor es necesario para eliminar")
            return
        db_proveedores = dbProveedor()
        db_proveedores.remov(id_proveedor)
        messagebox.showinfo("Éxito", "Proveedor eliminado exitosamente")
        self.nuevo_proveedor()

    def buscar_proveedor(self):
        id_proveedor = self.txBuscarProveedor.get()
        if not id_proveedor:
            messagebox.showerror("Error", "ID del proveedor es necesario para buscar")
            return
        db_proveedores = dbProveedor()
        proveedor = db_proveedores.search(id_proveedor)
        if proveedor:
            self.txId.delete(0, tk.END)
            self.txId.insert(0, proveedor.getId_proveedor())
            self.txNombre.delete(0, tk.END)
            self.txNombre.insert(0, proveedor.getNombre())
            self.txDireccion.delete(0, tk.END)
            self.txDireccion.insert(0, proveedor.getDireccion())
            self.txTelefono.delete(0, tk.END)
            self.txTelefono.insert(0, proveedor.getTelefono())
            self.txEmail.delete(0, tk.END)
            self.txEmail.insert(0, proveedor.getEmail())
            self.btEditar.config(state=tk.NORMAL)
            self.btCancelar.config(state=tk.NORMAL)
            self.btEliminar.config(state=tk.NORMAL)
        else:
            messagebox.showerror("Error", "Proveedor no encontrado")

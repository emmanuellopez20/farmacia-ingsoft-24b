import tkinter as tk
from tkinter import messagebox
from backend.clientesdb import dbClientes
from utils.clienteGS import Cliente

class ClienteCRUD(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Gestión de Clientes")
        self.geometry("800x600")
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.user_id = None  # Para manejar ID de usuario si es necesario

        # Frame para buscar
        self.frameBuscar = tk.Frame(self)
        self.frameBuscar.grid(row=0, column=1, padx=10, pady=10)
        # Campo de búsqueda
        self.buscar_label = tk.Label(self.frameBuscar, text="Buscar Cliente")
        self.buscar_label.grid(row=0, column=0, padx=10, pady=10)
        self.txBuscarCliente = tk.Entry(self.frameBuscar)
        self.txBuscarCliente.grid(row=0, column=1, padx=10, pady=10)
        self.btBuscar = tk.Button(self.frameBuscar, text="Buscar", command=self.buscar_cliente)
        self.btBuscar.grid(row=0, column=2, padx=10, pady=10)

        # Frame para entrada de datos
        self.frameEntradaDeDatos = tk.Frame(self)
        self.frameEntradaDeDatos.grid(row=1, column=1, padx=10, pady=10)
        # Campos de entrada
        self.id_label = tk.Label(self.frameEntradaDeDatos, text="ID")
        self.id_label.grid(row=0, column=0, padx=10, pady=10)
        self.txId = tk.Entry(self.frameEntradaDeDatos)
        self.txId.grid(row=0, column=1, padx=10, pady=10)
        self.nombre_label = tk.Label(self.frameEntradaDeDatos, text="Nombre del Cliente")
        self.nombre_label.grid(row=1, column=0, padx=10, pady=10)
        self.txNombre = tk.Entry(self.frameEntradaDeDatos)
        self.txNombre.grid(row=1, column=1, padx=10, pady=10)
        self.rfc_label = tk.Label(self.frameEntradaDeDatos, text="RFC")
        self.rfc_label.grid(row=2, column=0, padx=10, pady=10)
        self.txRfc = tk.Entry(self.frameEntradaDeDatos)
        self.txRfc.grid(row=2, column=1, padx=10, pady=10)
        self.puntos_label = tk.Label(self.frameEntradaDeDatos, text="Puntos Acumulados")
        self.puntos_label.grid(row=3, column=0, padx=10, pady=10)
        self.txPuntos = tk.Entry(self.frameEntradaDeDatos)
        self.txPuntos.grid(row=3, column=1, padx=10, pady=10)

        # Frame para botones
        self.frameBotones = tk.Frame(self)
        self.frameBotones.grid(row=2, column=1, padx=10, pady=10)
        # Botones
        self.btNuevo = tk.Button(self.frameBotones, text="Nuevo", command=self.nuevo_cliente)
        self.btNuevo.grid(row=0, column=0, padx=10, pady=10)
        self.btSalvar = tk.Button(self.frameBotones, text="Salvar", command=self.salvar_cliente)
        self.btSalvar.grid(row=0, column=1, padx=10, pady=10)
        self.btSalvar.config(state=tk.DISABLED)
        self.btEditar = tk.Button(self.frameBotones, text="Editar", command=self.editar_cliente)
        self.btEditar.grid(row=0, column=2, padx=10, pady=10)
        self.btEditar.config(state=tk.DISABLED)
        self.btCancelar = tk.Button(self.frameBotones, text="Cancelar", command=self.cancelar)
        self.btCancelar.grid(row=0, column=3, padx=10, pady=10)
        self.btCancelar.config(state=tk.DISABLED)
        self.btEliminar = tk.Button(self.frameBotones, text="Eliminar", command=self.eliminar_cliente)
        self.btEliminar.grid(row=0, column=4, padx=10, pady=10)
        self.btEliminar.config(state=tk.DISABLED)

    def nuevo_cliente(self):
        self.txId.delete(0, tk.END)
        self.txNombre.delete(0, tk.END)
        self.txRfc.delete(0, tk.END)
        self.txPuntos.delete(0, tk.END)
        db_clientes = dbClientes()
        nuevo_id = db_clientes.getMaxId() + 1
        self.txId.insert(0, nuevo_id)
        self.btSalvar.config(state=tk.NORMAL)
        self.btCancelar.config(state=tk.NORMAL)
        self.btEditar.config(state=tk.DISABLED)
        self.btEliminar.config(state=tk.DISABLED)

    """     def salvar_cliente(self):
            id_cliente = self.txId.get()
            nombre = self.txNombre.get()
            rfc = self.txRfc.get()
            puntos_acumulados = self.txPuntos.get()
            if not id_cliente or not nombre or not rfc or not puntos_acumulados:
                messagebox.showerror("Error", "Todos los campos son obligatorios")
                return
            cliente = Cliente(id_cliente, nombre, rfc, puntos_acumulados)
            db_clientes = dbClientes()
            db_clientes.save(cliente)
            messagebox.showinfo("Éxito", "Cliente guardado exitosamente")
            self.nuevo_cliente() """
    
    def salvar_cliente(self):
        id_cliente = self.txId.get()
        nombre = self.txNombre.get()
        rfc = self.txRfc.get()
        puntos_acumulados = self.txPuntos.get()
        if not nombre or not rfc or not puntos_acumulados:
            messagebox.showerror("Error", "Todos los campos son obligatorios")
            return
        cliente = Cliente(id_cliente, nombre, rfc, puntos_acumulados)
        db_clientes = dbClientes()
        db_clientes.save(cliente)
        messagebox.showinfo("Éxito", "Cliente guardado exitosamente")
        self.nuevo_cliente()


    def cancelar(self):
        self.nuevo_cliente()

    def editar_cliente(self):
        id_cliente = self.txId.get()
        nombre = self.txNombre.get()
        rfc = self.txRfc.get()
        puntos_acumulados = self.txPuntos.get()
        if not id_cliente or not nombre or not rfc or not puntos_acumulados:
            messagebox.showerror("Error", "Todos los campos son obligatorios")
            return
        cliente = Cliente(id_cliente, nombre, rfc, puntos_acumulados)
        db_clientes = dbClientes()
        db_clientes.edit(cliente)
        messagebox.showinfo("Éxito", "Cliente editado exitosamente")
        self.nuevo_cliente()

    def eliminar_cliente(self):
        id_cliente = self.txId.get()
        if not id_cliente:
            messagebox.showerror("Error", "ID del cliente es necesario para eliminar")
            return
        db_clientes = dbClientes()
        db_clientes.remov(id_cliente)
        messagebox.showinfo("Éxito", "Cliente eliminado exitosamente")
        self.nuevo_cliente()

    def buscar_cliente(self):
        id_cliente = self.txBuscarCliente.get()
        if not id_cliente:
            messagebox.showerror("Error", "ID del cliente es necesario para buscar")
            return
        db_clientes = dbClientes()
        cliente = db_clientes.search(id_cliente)
        if cliente:
            self.txId.delete(0, tk.END)
            self.txId.insert(0, cliente.getIdCliente())
            self.txNombre.delete(0, tk.END)
            self.txNombre.insert(0, cliente.getNombre())
            self.txRfc.delete(0, tk.END)
            self.txRfc.insert(0, cliente.getRfc())
            self.txPuntos.delete(0, tk.END)
            self.txPuntos.insert(0, cliente.getPuntosAcumulados())
            self.btEditar.config(state=tk.NORMAL)
            self.btCancelar.config(state=tk.NORMAL)
            self.btEliminar.config(state=tk.NORMAL)
        else:
            messagebox.showerror("Error", "Cliente no encontrado")

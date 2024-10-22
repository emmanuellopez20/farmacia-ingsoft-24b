import tkinter as tk
from tkinter import ttk, messagebox
from backend.usuariosdb import dbUsuario
from utils.usuariosGS import Usuario
from mysql.connector import Error
import re


class Registro(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title('Registro')
        self.geometry('500x300')

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(2, weight=1)

        #Frame para Entrys correo y contraseña
        self.frameEntradaDeDatos = tk.Frame(self)
        self.frameEntradaDeDatos.grid(row=1, column=1, padx=10, pady=10)

        #Entry de nombre
        self.lbNombre = tk.Label(self.frameEntradaDeDatos, text='Nombre completo: ')
        self.lbNombre.grid(row=0, column=0, padx=10, pady=10)
        self.txNombre = tk.Entry(self.frameEntradaDeDatos)
        self.txNombre.grid(row=0, column=1, padx=10, pady=10)

        #Entry de correo
        self.lbCorreo = tk.Label(self.frameEntradaDeDatos, text='Correo: ')
        self.lbCorreo.grid(row=1, column=0, padx=10, pady=10)
        self.txCorreo = tk.Entry(self.frameEntradaDeDatos)
        self.txCorreo.grid(row=1, column=1, padx=10, pady=10)

        #Entry de Contraseña
        self.lbContraseña = tk.Label(self.frameEntradaDeDatos, text='Contraseña: ')
        self.lbContraseña.grid(row=2, column=0, padx=10, pady=10)
        self.txContraseña = tk.Entry(self.frameEntradaDeDatos, show="*")
        self.txContraseña.grid(row=2, column=1, padx=10, pady=10)

        #Entry de rol
        self.lbRol = tk.Label(self.frameEntradaDeDatos, text='Rol: ')
        self.lbRol.grid(row=3, column=0, padx=10, pady=10)
        self.cbRol = ttk.Combobox(self.frameEntradaDeDatos, values=["administrador","gerente", "cajero"])
        self.cbRol.grid(row=3, column=1, padx=10, pady=10)
        self.cbRol.bind("<<ComboboxSelected>>")
        
        #Frame para los botones
        self.frameBotones = tk.Frame(self)
        self.frameBotones.grid(row=2, column=1, padx=10, pady=10)

        # self.btnLogin = tk.Button(self, text='Login')
        # self.btnLogin.grid(row=1, column=0, padx=10, pady=10, sticky='W')
        
        self.btnRegistrar = tk.Button(self.frameBotones, text='Registrar', command=self.register)
        self.btnRegistrar.grid(row=1, column=1, padx=10, pady=10, sticky='E')

    def register(self):
        nombre = self.txNombre.get().strip()
        correo = self.txCorreo.get().strip()
        contraseña = self.txContraseña.get().strip()
        rol = self.cbRol.get()
        
        #validacion de Campos vacios
        if nombre == "" or correo == "" or contraseña == "" or rol == "":
            messagebox.showerror("Error", "Todos los campos son obligatorios")
            return
        
        #validacion de longitud de la contrasena
        if len(contraseña) < 5:
            messagebox.showerror("Error", "La contraseña debe tener al menos 5 caracteres")
            return
        
        #Validacion de entrada de correo
        if not re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", correo):
            messagebox.showerror("Error", "El formato del correo es inválido. Debe ser del tipo usuario@dominio.com")
            return False

        #validacion de perfil
        rolesValidos = ['administrador', 'gerente', 'cajero']
        if rol.lower() not in rolesValidos:
            messagebox.showerror("Error", "Perfil invalido. Debe ser 'administrador, gerente o cajero'")
            return
        
        try:
            db_usuario = dbUsuario()
            if db_usuario.exists(correo):
                messagebox.showerror("Error", "El correo ya esta en uso")
                return
            
            usuario = Usuario()
            usuario.setNombre(nombre)
            usuario.setCorreo(correo)
            usuario.setContraseña(contraseña)
            usuario.setRol(rol.lower())

            db_usuario.save(usuario)

            messagebox.showinfo("Exito", "Usuario registrado exitosamente")
            self.destroy()
            # self.login_window.deiconify()
        except Error as err:
            messagebox.showerror("Error", f"Error al conectar con la base de datos {err}")





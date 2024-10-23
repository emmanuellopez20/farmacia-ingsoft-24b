import mysql.connector
from mysql.connector import Error
import conexion as con
import tkinter as tk
from tkinter import ttk, messagebox
from interfaces.registro import Registro
from interfaces.paginaPrincipal import PuntoDeVentaApp
from backend.usuariosdb import dbUsuario
import re

class Login(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Login')
        self.geometry('300x400')

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(2, weight=1)

        #Frame para Entrys correo y contraseña
        self.frameEntradaDeDatos = tk.Frame(self)
        self.frameEntradaDeDatos.grid(row=1, column=1, padx=10, pady=10)

        #Entry de correo
        self.lbCorreo = tk.Label(self.frameEntradaDeDatos, text='Correo: ')
        self.lbCorreo.grid(row=0, column=0, padx=10, pady=10)
        self.txCorreo = tk.Entry(self.frameEntradaDeDatos)
        self.txCorreo.grid(row=0, column=1, padx=10, pady=10)

        #Entry de Contraseña
        self.lbContraseña = tk.Label(self.frameEntradaDeDatos, text='Contraseña: ')
        self.lbContraseña.grid(row=1, column=0, padx=10, pady=10)
        self.txContraseña = tk.Entry(self.frameEntradaDeDatos, show="*")
        self.txContraseña.grid(row=1, column=1, padx=10, pady=10)

        #Frame para los botones
        self.frameBotones = tk.Frame(self)
        self.frameBotones.grid(row=2, column=1, padx=10, pady=10)

        self.btnLogin = tk.Button(self.frameBotones, text='Login', command=self.login)
        self.btnLogin.grid(row=1, column=0, padx=10, pady=10, sticky='W')
        
        self.btnRegistrar = tk.Button(self.frameBotones, text='Registrar', command=self.abrirRegistro)
        self.btnRegistrar.grid(row=1, column=1, padx=10, pady=10, sticky='E')

    def login(self):
        correo = self.txCorreo.get()
        contraseña = self.txContraseña.get()

        #validacion de campos vacios
        if correo == "" or contraseña == "":
            messagebox.showerror("Error", "Todos los campos son obligatorios")
            return
        
        #Validacion de formato valido de correo
        if not re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", correo):
            messagebox.showerror("Error", "El formato del correo es inválido. Debe ser del tipo usuario@dominio.com")
            return False

        #Validacion de longitud minima de la contrasena
        if len(contraseña) < 5:
            messagebox.showerror("Error", "La contraseña debe tener al menos 6 caracteres")
            return
        
        try:
            db_con = con.conexion()
            conn = db_con.open()
            if conn is None:
                raise Exception("No se pudo conectar a la base de datos")
            cursor = conn.cursor(buffered=True)
            cursor.execute("SELECT * FROM usuarios WHERE correo=%s AND contraseña=%s", (correo, contraseña))
            row = cursor.fetchone()
            db_con.close()

            if row:
                id_user = row[0]
                messagebox.showinfo("Exito", "Login exitoso")
                self.abrirPantallaPrincipal()
            else:
                messagebox.showerror("Error", "Correo o contraseña incorrectos")
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error al conectar con la base de datos: {err}")


    def abrirRegistro(self):
        ventanaRegistro = Registro(self)
        ventanaRegistro.mainloop()
    
    def abrirPantallaPrincipal(self):
        # self.destroy()
        appPantallaPrincipal = PuntoDeVentaApp(self)
        appPantallaPrincipal.mainloop




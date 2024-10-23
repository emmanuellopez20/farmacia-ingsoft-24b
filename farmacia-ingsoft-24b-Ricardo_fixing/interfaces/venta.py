import tkinter as tk
from tkinter import ttk, messagebox
from backend.productodb import dbProductos
from backend.clientesdb import dbClientes
from backend.detalleventadb import dbDetalleVenta
from backend.ventasdb import dbVentas
from utils.detalleventaGS import DetalleVenta
from utils.ventaGS import Ventas
from fpdf import FPDF
import datetime

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Farmacia XYZ', 0, 1, 'C')

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

    def chapter_title(self, title):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, title, 0, 1, 'L')
        self.ln(10)

    def chapter_body(self, body):
        self.set_font('Arial', '', 12)
        self.multi_cell(0, 10, body)
        self.ln()

    def add_sale(self, venta, detalles):
        self.add_page()
        self.chapter_title(f'Folio: {venta.getId_venta()}')
        self.chapter_body(f'Cliente: {venta.getId_cliente()}\nFecha: {venta.getFecha_venta()}\nTotal: ${venta.getTotal()}')
        
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Detalles de la Venta', 0, 1, 'L')
        self.set_font('Arial', '', 12)
        for detalle in detalles:
            self.cell(0, 10, f'{detalle.getId_producto()} - {detalle.getCantidad()} unidades x ${detalle.getPrecio_unitario()} - Subtotal: ${detalle.getSubtotal()}', 0, 1, 'L')


class Venta(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title('Venta de Productos')
        self.geometry('1600x900')
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.productos_vendidos = []

        # Frame para el entry (a la izquierda)
        self.frameEntradaDeDatos = tk.Frame(self)
        self.frameEntradaDeDatos.grid(row=0, column=0, padx=10, pady=10, sticky='ns')
        tk.Label(self.frameEntradaDeDatos, text='Folio:').grid(row=0, column=0, padx=5, pady=5)
        self.folio_entry = tk.Entry(self.frameEntradaDeDatos)
        self.folio_entry.grid(row=0, column=1, padx=5, pady=5)
        tk.Label(self.frameEntradaDeDatos, text='Fecha:').grid(row=1, column=0, padx=5, pady=5)
        self.fecha_entry = tk.Entry(self.frameEntradaDeDatos)
        self.fecha_entry.grid(row=1, column=1, padx=5, pady=5)
        tk.Label(self.frameEntradaDeDatos, text='Buscar Producto:').grid(row=2, column=0, padx=5, pady=5)
        self.producto_entry = tk.Entry(self.frameEntradaDeDatos)
        self.producto_entry.grid(row=2, column=1, padx=5, pady=5)
        self.buscar_button = tk.Button(self.frameEntradaDeDatos, text='Buscar', command=self.buscar_producto)
        self.buscar_button.grid(row=2, column=2, padx=5, pady=5)
        tk.Label(self.frameEntradaDeDatos, text='Código:').grid(row=3, column=0, padx=5, pady=5)
        self.codigo_entry = tk.Entry(self.frameEntradaDeDatos)
        self.codigo_entry.grid(row=3, column=1, padx=5, pady=5)
        tk.Label(self.frameEntradaDeDatos, text='Nombre de Producto:').grid(row=4, column=0, padx=5, pady=5)
        self.nombre_entry = tk.Entry(self.frameEntradaDeDatos)
        self.nombre_entry.grid(row=4, column=1, padx=5, pady=5)
        tk.Label(self.frameEntradaDeDatos, text='Descripción:').grid(row=5, column=0, padx=5, pady=5)
        self.descripcion_entry = tk.Entry(self.frameEntradaDeDatos)
        self.descripcion_entry.grid(row=5, column=1, padx=5, pady=5)
        tk.Label(self.frameEntradaDeDatos, text='Precio:').grid(row=6, column=0, padx=5, pady=5)
        self.precio_entry = tk.Entry(self.frameEntradaDeDatos)
        self.precio_entry.grid(row=6, column=1, padx=5, pady=5)
        tk.Label(self.frameEntradaDeDatos, text='Stock:').grid(row=7, column=0, padx=5, pady=5)
        self.stock_entry = tk.Entry(self.frameEntradaDeDatos)
        self.stock_entry.grid(row=7, column=1, padx=5, pady=5)
        tk.Label(self.frameEntradaDeDatos, text='Cantidad:').grid(row=8, column=0, padx=5, pady=5)
        self.cantidad_entry = tk.Entry(self.frameEntradaDeDatos)
        self.cantidad_entry.grid(row=8, column=1, padx=5, pady=5)

        # Frame para la tabla de productos (en el centro)
        self.frameTabla = tk.Frame(self)
        self.frameTabla.grid(row=1, column=1, rowspan=5, padx=10, pady=10, sticky='nsew')
        columns = ('#1', '#2', '#3', '#4', '#5')
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
        self.tree.grid(row=0, column=0, columnspan=5, padx=5, pady=5, sticky='nsew')

        # Campo para buscar venta por folio (centrado y arriba)
        tk.Label(self, text='Buscar Venta por Folio:').grid(row=0, column=1, padx=5, pady=5, sticky='n')
        self.folio_buscar_entry = tk.Entry(self)
        self.folio_buscar_entry.grid(row=0, column=1, padx=5, pady=5, sticky='ne')
        self.buscar_folio_button = tk.Button(self, text='Buscar', command=self.buscar_venta_por_folio)
        self.buscar_folio_button.grid(row=0, column=1, padx=5, pady=5, sticky='ne')

        # Cuadro para Cliente (a la derecha)
        self.cliente_frame = tk.LabelFrame(self, text='Cliente')
        self.cliente_frame.grid(row=0, column=2, padx=10, pady=5, sticky='ns')
        tk.Label(self.cliente_frame, text='Código del cliente:').grid(row=0, column=0, padx=5, pady=5)
        self.nombre_cliente_entry = tk.Entry(self.cliente_frame)
        self.nombre_cliente_entry.grid(row=0, column=1, padx=5, pady=5)
        tk.Label(self.cliente_frame, text='Seleccionar Cliente:').grid(row=1, column=0, padx=5, pady=5)
        self.clientes_combo = ttk.Combobox(self.cliente_frame)
        self.clientes_combo.grid(row=1, column=1, padx=5, pady=5)
        tk.Label(self.cliente_frame, text='RFC:').grid(row=2, column=0, padx=5, pady=5)
        self.rfc_entry = tk.Entry(self.cliente_frame)
        self.rfc_entry.grid(row=2, column=1, padx=5, pady=5)

        # Frame para la información de la venta (arriba del frame de totales, a la derecha)
        self.frameInfoVenta = tk.Frame(self)
        self.frameInfoVenta.grid(row=4, column=2, padx=10, pady=10, sticky='ew')
        tk.Label(self.frameInfoVenta, text='Cliente:').grid(row=0, column=0, padx=5, pady=5)
        self.info_cliente_entry = tk.Entry(self.frameInfoVenta, state='readonly')
        self.info_cliente_entry.grid(row=0, column=1, padx=5, pady=5)
        tk.Label(self.frameInfoVenta, text='Usuario:').grid(row=1, column=0, padx=5, pady=5)
        self.info_usuario_entry = tk.Entry(self.frameInfoVenta, state='readonly')
        self.info_usuario_entry.grid(row=1, column=1, padx=5, pady=5)
        tk.Label(self.frameInfoVenta, text='Fecha:').grid(row=2, column=0, padx=5, pady=5)
        self.info_fecha_entry = tk.Entry(self.frameInfoVenta, state='readonly')
        self.info_fecha_entry.grid(row=2, column=1, padx=5, pady=5)
        tk.Label(self.frameInfoVenta, text='Total:').grid(row=3, column=0, padx=5, pady=5)
        self.info_total_entry = tk.Entry(self.frameInfoVenta, state='readonly')
        self.info_total_entry.grid(row=3, column=1, padx=5, pady=5)
        self.imprimir_ticket_button = tk.Button(self.frameInfoVenta, text='Imprimir Ticket', command=self.imprimir_ticket)
        self.imprimir_ticket_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

        # Frame para Subtotal, IVA y Total (esquina inferior derecha)
        self.frameTotales = tk.Frame(self)
        self.frameTotales.grid(row=5, column=2, padx=10, pady=10, sticky='se')
        tk.Label(self.frameTotales, text='Subtotal:').grid(row=0, column=0, padx=5, pady=5)
        self.subtotal_entry = tk.Entry(self.frameTotales, state='readonly')
        self.subtotal_entry.grid(row=0, column=1, padx=5, pady=5)
        tk.Label(self.frameTotales, text='IVA:').grid(row=1, column=0, padx=5, pady=5)
        self.iva_entry = tk.Entry(self.frameTotales, state='readonly')
        self.iva_entry.grid(row=1, column=1, padx=5, pady=5)
        tk.Label(self.frameTotales, text='Total:').grid(row=2, column=0, padx=5, pady=5)
        self.total_entry = tk.Entry(self.frameTotales, state='readonly')
        self.total_entry.grid(row=2, column=1, padx=5, pady=5)
        self.calcular_total_button = tk.Button(self.frameTotales, text='Calcular Total', command=self.calcular_total)
        self.calcular_total_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

        # Frame para botones de acción (al fondo de la ventana)
        self.frameBotones = tk.Frame(self)
        self.frameBotones.grid(row=6, column=1, padx=10, pady=10, sticky='ew')
        self.agregar_button = tk.Button(self.frameBotones, text='Agregar', command=self.agregar_producto)
        self.agregar_button.grid(row=0, column=0, padx=5, pady=5)
        self.quitar_button = tk.Button(self.frameBotones, text='Quitar', command=self.quitar_producto)
        self.quitar_button.grid(row=0, column=1, padx=5, pady=5)
        self.cancelar_button = tk.Button(self.frameBotones, text='Cancelar Venta', command=self.cancelar_venta)
        self.cancelar_button.grid(row=0, column=2, padx=5, pady=5)
        self.realizar_venta_button = tk.Button(self.frameBotones, text='Realizar Venta', command=self.realizar_venta)
        self.realizar_venta_button.grid(row=0, column=3, padx=5, pady=5)
        self.frameBotones.grid_columnconfigure(0, weight=1)
        self.frameBotones.grid_columnconfigure(1, weight=1)
        self.frameBotones.grid_columnconfigure(2, weight=1)
        self.frameBotones.grid_columnconfigure(3, weight=1)


        self.cargar_clientes()
        self.buscar_button.config(command=self.buscar_producto)
        self.agregar_button.config(command=self.agregar_producto)
        self.quitar_button.config(command=self.quitar_producto)
        self.cancelar_button.config(command=self.cancelar_venta)
        self.clientes_combo.bind("<<ComboboxSelected>>", self.seleccionar_cliente)

        self.inicializar()



    def inicializar(self):
        db_ventas = dbVentas()
        max_folio = db_ventas.get_max_id() + 1  # Obtener el folio máximo y sumar 1
        self.folio_entry.insert(0, str(max_folio))  # Inicializa el folio
        self.fecha_entry.insert(0, datetime.datetime.now().strftime("%Y-%m-%d"))  # Autopopular fecha
        self.cargar_clientes()

    def buscar_venta_por_folio(self):
        folio = self.folio_buscar_entry.get()
        if not folio:
            messagebox.showerror("Error", "Por favor, ingrese un número de folio")
            return

        db_ventas = dbVentas()
        venta = db_ventas.search(folio)
        
        if not venta:
            messagebox.showerror("Error", "No se encontró ninguna venta con ese folio")
            return
        
        db_detalle_venta = dbDetalleVenta()
        detalles = db_detalle_venta.get_all_by_venta_id(folio)

        # Mostrar la información de la venta en la interfaz
        self.info_cliente_entry.config(state='normal')
        self.info_cliente_entry.delete(0, tk.END)
        self.info_cliente_entry.insert(0, venta.getId_cliente())
        self.info_cliente_entry.config(state='readonly')
        self.info_usuario_entry.config(state='normal')
        self.info_usuario_entry.delete(0, tk.END)
        self.info_usuario_entry.insert(0, venta.getId_usuario())
        self.info_usuario_entry.config(state='readonly')
        self.info_fecha_entry.config(state='normal')
        self.info_fecha_entry.delete(0, tk.END)
        self.info_fecha_entry.insert(0, venta.getFecha_venta())
        self.info_fecha_entry.config(state='readonly')
        self.info_total_entry.config(state='normal')
        self.info_total_entry.delete(0, tk.END)
        self.info_total_entry.insert(0, venta.getTotal())
        self.info_total_entry.config(state='readonly')


    def cargar_clientes(self):
        db_clientes = dbClientes()
        clientes = db_clientes.get_all_clientes()
        if clientes:
            self.clientes_combo['values'] = [cliente.getNombre() for cliente in clientes]
            self.clientes_dict = {cliente.getNombre(): cliente for cliente in clientes}  # Mapa de nombres a objetos cliente
        else:
            messagebox.showerror("Error", "No hay clientes registrados")
    def seleccionar_cliente(self, event):
        cliente_nombre = self.clientes_combo.get()
        cliente = self.clientes_dict.get(cliente_nombre)
        if cliente:
            self.nombre_cliente_entry.delete(0, tk.END)
            self.nombre_cliente_entry.insert(0, cliente.getIdCliente())
            self.rfc_entry.delete(0, tk.END)
            self.rfc_entry.insert(0, cliente.getRfc())



    def buscar_producto(self):
        producto_nombre = self.producto_entry.get()
        db_productos = dbProductos()
        productos = db_productos.search_by_name(producto_nombre)
        if productos:
            producto = productos[0]  # Asume el primer producto de la lista
            self.codigo_entry.delete(0, tk.END)
            self.codigo_entry.insert(0, producto.getId_producto())
            self.nombre_entry.delete(0, tk.END)
            self.nombre_entry.insert(0, producto.getNombre_producto())
            self.descripcion_entry.delete(0, tk.END)
            self.descripcion_entry.insert(0, producto.getDescripcion())
            self.precio_entry.delete(0, tk.END)
            self.precio_entry.insert(0, producto.getPrecio())
            self.stock_entry.delete(0, tk.END)
            self.stock_entry.insert(0, producto.getCantidad_stock())
        else:
            messagebox.showerror("Error", "Producto no encontrado")



    def agregar_producto(self):
        codigo = self.codigo_entry.get()
        nombre = self.nombre_entry.get()
        descripcion = self.descripcion_entry.get()
        precio = self.precio_entry.get()
        stock = self.stock_entry.get()
        cantidad = self.cantidad_entry.get()

        if not codigo or not nombre or not descripcion or not precio or not stock or not cantidad:
            messagebox.showerror("Error", "Todos los campos son obligatorios")
            return

        if int(cantidad) > int(stock):
            messagebox.showerror("Error", "La cantidad excede el stock disponible")
            return

        precio_total = float(precio) * int(cantidad)

        # Actualizar el stock en la base de datos
        db_productos = dbProductos()
        db_productos.disminuir_stock(codigo, int(cantidad))

        # Buscar si el producto ya está en el carrito
        for row in self.tree.get_children():
            item = self.tree.item(row)
            if item['values'][0] == codigo:
                nueva_cantidad = int(item['values'][3]) + int(cantidad)
                nuevo_precio_total = float(precio) * nueva_cantidad
                self.tree.item(row, values=(codigo, descripcion, precio, nueva_cantidad, nuevo_precio_total))
                return

        self.tree.insert('', 'end', values=(codigo, descripcion, precio, cantidad, precio_total))

        self.codigo_entry.delete(0, tk.END)
        self.nombre_entry.delete(0, tk.END)
        self.descripcion_entry.delete(0, tk.END)
        self.precio_entry.delete(0, tk.END)
        self.stock_entry.delete(0, tk.END)
        self.cantidad_entry.delete(0, tk.END)
        self.productos_vendidos.append((codigo, int(cantidad)))


    def calcular_total(self):
        subtotal = 0
        for row in self.tree.get_children():
            item = self.tree.item(row)
            subtotal += float(item['values'][4])  # Precio Total

        iva = subtotal * 0.16
        total = subtotal

        self.subtotal_entry.config(state='normal')
        self.subtotal_entry.delete(0, tk.END)
        self.subtotal_entry.insert(0, f'{subtotal:.2f}')
        self.subtotal_entry.config(state='readonly')

        self.iva_entry.config(state='normal')
        self.iva_entry.delete(0, tk.END)
        self.iva_entry.insert(0, f'{iva:.2f}')
        self.iva_entry.config(state='readonly')

        self.total_entry.config(state='normal')
        self.total_entry.delete(0, tk.END)
        self.total_entry.insert(0, f'{total:.2f}')
        self.total_entry.config(state='readonly')



    def realizar_venta(self):
        db_productos = dbProductos()
        db_clientes = dbClientes()
        db_ventas = dbVentas()  # Instancia de dbVentas
        db_detalle_venta = dbDetalleVenta()  # Instancia de dbDetalleVenta
        
        id_cliente = self.nombre_cliente_entry.get()
        total = self.total_entry.get()

        # Verificar si los campos están vacíos
        if not id_cliente or not total:
            messagebox.showerror("Error", "Todos los campos son obligatorios")
            return

        # Crear un objeto venta y guardarlo en la base de datos
        venta = Ventas(id_cliente=id_cliente, id_usuario=1, fecha_venta=datetime.datetime.now(), total=total)
        id_venta = db_ventas.save(venta)

        # Insertar en la tabla detalle_venta
        for row in self.tree.get_children():
            item = self.tree.item(row)
            id_producto = item['values'][0]
            cantidad = item['values'][3]
            precio_unitario = item['values'][2]
            subtotal = item['values'][4]
            
            detalle_venta = DetalleVenta(id_venta=id_venta, id_producto=id_producto, cantidad=cantidad, precio_unitario=precio_unitario, subtotal=subtotal)
            db_detalle_venta.save(detalle_venta)

        messagebox.showinfo("Éxito", "Venta realizada correctamente")

        # Incrementar el folio y limpiar campos
        max_folio = id_venta + 1
        self.folio_entry.config(state='normal')
        self.folio_entry.delete(0, tk.END)
        self.folio_entry.insert(0, str(max_folio))
        self.folio_entry.config(state='readonly')
        self.nombre_cliente_entry.delete(0, tk.END)
        self.rfc_entry.delete(0, tk.END)
        self.tree.delete(*self.tree.get_children())
        self.productos_vendidos = []
        self.info_cliente_entry.config(state='normal')
        self.info_cliente_entry.delete(0, tk.END)
        self.info_cliente_entry.config(state='readonly')
        self.info_usuario_entry.config(state='normal')
        self.info_usuario_entry.delete(0, tk.END)
        self.info_usuario_entry.config(state='readonly')
        self.info_fecha_entry.config(state='normal')
        self.info_fecha_entry.delete(0, tk.END)
        self.info_fecha_entry.config(state='readonly')
        self.info_total_entry.config(state='normal')
        self.info_total_entry.delete(0, tk.END)
        self.info_total_entry.config(state='readonly')




    def quitar_producto(self):
        selected_item = self.tree.selection()
        if selected_item:
            item = self.tree.item(selected_item)
            codigo = item['values'][0]
            cantidad = item['values'][3]

            # Aumentar stock en la base de datos
            db_productos = dbProductos()
            db_productos.aumentar_stock(codigo, cantidad)

            # Eliminar el producto del carrito de productos vendidos
            for i, producto in enumerate(self.productos_vendidos):
                if producto[0] == codigo:
                    if producto[1] == int(cantidad):
                        del self.productos_vendidos[i]
                    else:
                        self.productos_vendidos[i] = (producto[0], producto[1] - int(cantidad))
                    break
            
            self.tree.delete(selected_item)




    def cancelar_venta(self):
        db_productos = dbProductos()
        db_ventas = dbVentas()
        db_detalle_venta = dbDetalleVenta()

        folio = self.folio_entry.get()
        if not folio:
            messagebox.showerror("Error", "No hay ninguna venta en proceso para cancelar")
            return

        venta_id = int(folio)
        if venta_id:
            detalles = db_detalle_venta.get_all_by_venta_id(venta_id)
            for detalle in detalles:
                db_productos.aumentar_stock(detalle.getId_producto(), detalle.getCantidad())

            db_detalle_venta.delete_by_venta_id(venta_id)
            db_ventas.delete_by_id(venta_id)

            print(f"Venta {venta_id} cancelada.")  # Debug

            # Limpiar campos y tabla
            for row in self.tree.get_children():
                self.tree.delete(row)
            self.codigo_entry.delete(0, tk.END)
            self.nombre_entry.delete(0, tk.END)
            self.descripcion_entry.delete(0, tk.END)
            self.precio_entry.delete(0, tk.END)
            self.stock_entry.delete(0, tk.END)
            self.cantidad_entry.delete(0, tk.END)
            self.productos_vendidos = []
            self.info_cliente_entry.config(state='normal')
            self.info_cliente_entry.delete(0, tk.END)
            self.info_cliente_entry.config(state='readonly')
            self.info_usuario_entry.config(state='normal')
            self.info_usuario_entry.delete(0, tk.END)
            self.info_usuario_entry.config(state='readonly')
            self.info_fecha_entry.config(state='normal')
            self.info_fecha_entry.delete(0, tk.END)
            self.info_fecha_entry.config(state='readonly')
            self.info_total_entry.config(state='normal')
            self.info_total_entry.delete(0, tk.END)
            self.info_total_entry.config(state='readonly')
            messagebox.showinfo("Éxito", "Venta cancelada")
        else:
            messagebox.showerror("Error", "No se encontró la venta para cancelar")

    def imprimir_ticket(self):
        folio = self.folio_entry.get()
        if not folio:
            messagebox.showerror("Error", "No se encontró ninguna venta con ese folio")
            return
        db_ventas = dbVentas()
        db_detalle_venta = dbDetalleVenta()

        venta = db_ventas.search(folio)
        print(venta)  # Debug
        if not venta:
            messagebox.showerror("Error", "No se encontró ninguna venta con ese folio")
            return

        detalles = db_detalle_venta.get_all_by_venta_id(int(folio))

        pdf = PDF()
        pdf.add_sale(venta, detalles)
        pdf.output(f'ticket_{folio}.pdf')
        messagebox.showinfo("Éxito", f'Ticket generado correctamente como ticket_{folio}.pdf')

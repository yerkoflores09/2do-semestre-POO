class Producto():
    def __init__(self, producto, precio, cantidad, codigo):
        self.producto = producto
        self.precio = precio
        self.cantidad = cantidad
        self.codigo = codigo
        self.historial = [] #lista de cambios en el stock

    #metodo para actualizar el stock
    def actualizar_stock(self, cambio):
        self.cantidad += cambio
        self.historial.append(cambio)
        print(f'Stock actualizado: {self.producto} ahora tiene {self.cantidad} unidades.')

    #metodo para calcular el valor total de los productos
    def valor_total(self):
        return self.cantidad * self.precio
    
    #metodo magico para mostrar el estado actual
    def __str__(self):
        return (f'Producto: {self.producto} | Codigo: {self.codigo}\n'
                f'Precio: {self.precio} | Cantidad: {self.cantidad}\n'
                f'Valor Total: ${self.valor_total()}\n'
                f'Hitorial de cambios: {self.historial}')
    

class Inventario():
    def __init__(self):
        self.productos = {} #diccionario {codigo: producto}

    #metodo que agregue un nuevo producto al inventario
    def agregar_producto(self, producto):
        if producto.codigo in self.productos:
            print('Error: ya existe un producto con ese nombre')
        else:
            self.productos[producto.codigo] = producto
            print(f'Producto {producto.producto} agregado al inventario.')

    #metodo para actualizar el stock
    def actualizar_stock_producto(self, codigo, cambio):
        if codigo in self.productos:
            self.productos[codigo].actualizar_stock(cambio)
        else:
            print('Produto no encontrado en inventario.')

    #metodo para mostrar todos los productos
    def mostrar_productos(self):
        if not self.productos:
            print('Inventario vacío.')
        for producto in self.productos.values(): #values() devuelve una vista de los valores del diccionario en forma de objeto iterable
            print(producto)
            print('-' * 40) #lineas para separar los productos

    #calcular el valor total del inventario
    def total_inventario(self):
        total = sum(p.valor_total() for p in self.productos.values())
        return total
    

p1 = Producto('manzanas', 500, 10, 'A1')
p2 = Producto('sandia', 900, 15, 'B2')

inventario = Inventario()
inventario.agregar_producto(p1)
inventario.agregar_producto(p2)

inventario.mostrar_productos()

inventario.actualizar_stock_producto('A1', -9) # se vendio 9 manzanas
inventario.actualizar_stock_producto('B2', 4) # se agregó 4 sandias

print('Valor total del inventario:', inventario.total_inventario())
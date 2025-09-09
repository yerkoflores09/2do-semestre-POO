class Pedido():
    def __init__(self, n_mesa):
        self.n_mesa = n_mesa
        self.platos = [] #lista (nombre, precio)
        self.total = 0

    #metodo para añadir platos al pedido
    def agregar_plato(self, nombre, precio):
        self.platos.append((nombre, precio)) #append agrega un único elemento al final de la lista existente
        self.total += precio
        print(f'Plato "{nombre}" agregando a la mesa {self.n_mesa} (${precio}).')

    #metodo para calcular el total del pedido
    def calcular_total(self):
        return sum(precio for _, precio in self.platos)
    
    #metodo magico para contar el numero de platos (len)
    def __len__(self):
        return len(self.platos)
    
    #metodo magico para combinar dos pedidos de la misma mesa
    def __add__(self, other):
        if self.n_mesa != other.n_mesa:
            raise ValueError('No se pueden combinar pedidos de mesas diferentes.')
        nuevo_pedido = Pedido(self.n_mesa)
        nuevo_pedido.platos = self.platos + other.platos
        nuevo_pedido.total = self.total + other.total
        return nuevo_pedido
    
    #mostrar la informacion
    def __str__(self):
        detalle = f'Pedido mesa {self.n_mesa}:\n'
        for nombre, precio in self.platos:
            detalle += f'- {nombre}: ${precio}\n'
        detalle += f'Total: ${self.total}'
        return detalle
    
    #finalizador
    def __del__(self):
        print(f'el pedido de la mesa {self.n_mesa} ha sido completado.')


pedido1 = Pedido(5)
pedido1.agregar_plato('pizza', 9000)
pedido1.agregar_plato('coquita', 2000)

pedido2 = Pedido(5)
pedido2.agregar_plato('cangreburger', 8000)

print(pedido1)
print('cantidad de platos en pedido1:', len(pedido1))
print('total pedido1:', pedido1.calcular_total())

#combinar pedidos de la misma mesa
pedido3 = pedido1 + pedido2
print(pedido3)

#al eliminar
del pedido3
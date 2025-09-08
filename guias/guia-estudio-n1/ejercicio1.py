class reservaHostal():
    def __init__(self, nombre_cliente, f_entrada, f_salida, n_habitacion):
        self.nombre_cliente = nombre_cliente
        self.f_entrada = f_entrada
        self.f_salida = f_salida
        self.n_habitacion = int(n_habitacion)

    #metodo para calcular la estadía del del cliente
    def calcular_estadia(self):
        return self.f_salida - self.f_entrada
    
    #metodo para cambiar la fecha de salida
    def cambiar_fecha_salida(self, nueva_salida):
        self.dia_salida = nueva_salida
        print(f'La nueva fecha de salida es: {self.dia_salida}')
    
    #metodo magico para mostrar informacion en reserva
    def __str__(self):
        return (f'Reserva de {self.nombre_cliente}'
                f'Habitacion: {self.n_habitacion}'
                f'Entrada: Día {self.f_entrada}'
                f'Salida: Día {self.f_salida}'
                f'Duracion: {self.calcular_estadia()} noches')
    
    #destructor
    def __del__(self):
        print(f'la reserva de {self.nombre_cliente} ha sido cancelada')

#ejemplo:
reserva1 = reservaHostal('bobEponja', 10, 16, 23)
print(reserva1)

print('duracion:', reserva1.calcular_estadia(), 'noches')

reserva1.cambiar_fecha_salida(18)
print(reserva1)

del reserva1 #al eliminar imprime el mensaje
class FuncionTrigonometrica():
    def __init__(self, tipo, amplitud=1, periodo=360):
        self.tipo = tipo.lower() #seno, coseno, tangente
        self.amplitud = amplitud
        self.periodo = periodo

    #metodo para evaluar de manera aprox
    def evaluar(self, x):
        #normalizar x dentro de 0-360
        x = x % 360
        rad = x * 3.14159 / 180 #conversión manual a radianes

        if self.tipo == 'seno':
            #serie de Taylor aproximada para seno
            return self.amplitud * (rad - (rad**3)/6 + (rad**5)/120)
        
        elif self.tipo == 'coseno':
            #serie de Taylor aproximada para coseno
            return self.amplitud * (1 - (rad**2)/2 + (rad**4)/24)
        
        elif self.tipo == 'tangente':
            seno = (rad - (rad**3)/6 + (rad**5)/120)
            coseno = (1 - (rad**2)/2 + (rad**4)/24)
            if coseno == 0:
                return 'indefinido'
            return self.amplitud * (seno / coseno)
        else:
            return 'funcion no válida'
        
    #metodo para graficar en texto
    def graficar(self, inicio=0, fin=360, paso=30):
        print(f'Gráfico de {self.tipo} (aproximado, en texto):')
        for x in range(inicio, fin+1, paso):
            y = self.evaluar(x)
            if isinstance(y, str):  # evitar indefinido en tangente
                print(f'x={x}° -> {y}')
            else:
                posiciones = int(y * 10) + 20
                print(' ' * max(0, posiciones) + '*')

    #metodo magico
    def __str__(self):
        return f'Funcion: {self.tipo}, Amplitud: {self.amplitud}, Periodo: {self.periodo}'
    
    #metodo para valores críticos
    def valor_critico(self):
        if self.tipo in ['seno', 'coseno']:
            return {'max': self.amplitud, 'min': -self.amplitud}
        elif self.tipo == 'tangente':
            return 'la tengente no tiene maximos ni minimos definidos.'
        else:
            return 'Funcion no válida'
        

f1 = FuncionTrigonometrica('seno', amplitud=1, periodo=360)

print(f1)
print('f(90) =', f1.evaluar(90))
print('valores críticos:', f1.valor_critico())
f1.graficar()

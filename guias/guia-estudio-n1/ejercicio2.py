class FuncionTrigonometrica():
    def __init__(self, tipo, amplitud=1, periodo=360):
        self.tipo = tipo.lower() #seno, coseno, tangente
        self.amplitud = amplitud
        self.periodo = periodo

    #metodo para evaluar de manera aprox
    def evaluar(self, x):
        #normalizar x dentro de 0-360
        x = x % 360
        rad = x * 3.14159 / 180

    
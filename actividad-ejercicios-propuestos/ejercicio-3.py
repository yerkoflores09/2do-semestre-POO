class fraccion():

    def __init__(self, fraccion, numerador, denominador):
        self.fraccion = float(fraccion)
        self.numerador = numerador
        self.denominador = denominador

    def __str__(self):
        return f'la fracción contiene {self.numerador} numerador, {self.denominador} y denominador'

    def __add__(self, fraction):
        resultado_denominador = self.denominador + fraction.denominador
        resultado_numerador = (self.numerador + fraction.denominador *
                               fraction.denominador + self.numerador)
        return fraccion(resultado_numerador, resultado_denominador)

    def __mull__(self, fraction):
        resultado_numerador = self.numerador * fraction.numerador
        resultado_denominador = self.denominador * fraction.denominador
        return fraccion(resultado_numerador, resultado_denominador)
    
    def __eq__(self, fraction):
        return fraccion(
            self.numerador/self.denominador == fraction.numerador/fraction.denominador
        )
    
fraccion1 = fraccion(1, 2)
fraccion2 = fraccion(2, 3)
fraccion3 = fraccion(3, 4)

class Cancion():
    #constructor de la clase
    def __init__(self, titulo, artista, duracion_segundos,):
        self.titulo = titulo
        self.artista = artista
        self.duracion_segundos = int(duracion_segundos)

    #metodos de clase 
    #convertir la duracion a formato mm:ss (3:45)
    def min_seg(self):
        m, s = divmod(max(self.duracion_segundos, 0), 60) #divmod divide y obtiene el resto (en formato de tupla)
        return f'{m}:{s:02d}' #ejemplo: 185 segundos -> "3:05"
    
    def __str__(self):
        return f'{self.titulo} - {self.artista} ({self.min_seg()})'



class Playlist():
    #Constructor de la clase
    def __init__(self, nombre):
        self.nombre = nombre
        self.canciones = []

    #metodos de clase
    def agregar(self, cancion):
        self.canciones.append(cancion)

    #duracion total de la playlist
    def duracion_total(self):
        #iterador for en una linea
        return sum(c.duracion_segundos for c in self.canciones)
    
    #muestra la duracion total en mm:ss
    def milisegundos_total(self):
        total = self.duracion_total()
        m, s = divmod(max(total, 0), 60)
        return f'{m}:{s}'
    
    #contar el numero de canciones
    def __len__(self):
        return len(self.canciones)
    
    #combinacion de las dos playlist
    def __add__(self, otra):
        nueva = Playlist(f'{self.nombre} + {otra.nombre}')
        
        #guardando las canciones en la playlist combinadas
        nueva.canciones = self.canciones + otra.canciones
        return nueva
    
    def __str__(self):
        #encabezado a Mostrar de la playlist
        encabezado = f'Playlist: {self.nombre} | {len(self.canciones)} | Total: {self.milisegundos_total()}'

        #lanzar mensaje si la lista está vacía
        if not self.canciones:
            return encabezado , f'lista vacía'
        
        #para la creacion del formato de impresion de la playlist
        lineas = [encabezado]

        #creacion de ciclo para mostrar el listado de canciones de la playlist combinada
        for i, c in enumerate(self.canciones):
            lineas.append(f'{i}: {c}')
            return '\n'.join(lineas) #combina el salto de lienas
        



#instanciar clases (creacion de objetos)
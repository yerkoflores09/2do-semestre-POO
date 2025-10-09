class AgendaTareas():

    #variable de la clase
    __contador = 0

    def __init__(self):
        self.__tareas = [] #privado, lista de tareas

    def agregar(self, titulo: str) -> int:
        """
        agrega una nueva tarea no realizada 
        
        precondicion: titulo no vacío
        postcondicion: agrega tarea y retorna ID
        """

        if not titulo or not titulo.strip():
            raise ValueError('el titulo no puede estra vacío')
        
        #incrementar contador de la clase
        AgendaTareas.__contador += 1

        #crear nueva tarea
        nueva_tarea = {
            'id' : AgendaTareas.__contador,
            'titulo' : titulo.strip(),
            'hecha' : False
        }

        self.__tareas.append(nueva_tarea)
        return AgendaTareas.__contador
    
    def marcar_hecha(self, id: int) -> None:
        """
        marca una tarea como realizada

        precondicion: ID valido        
        postcondicion: cambia estado a hecha
        """
        tarea = self._buscar_por_id(id)
        if tarea:
            tarea['hecha'] = True
        else:
            raise ValueError(f'ID {id} no encontrado')
        
    def listar_pendientes(self) -> list:
        """
        retorna lista de titulos de tareas pendientes
        postcondicion: cambia estado a hecha
        """
        return [tarea['titulo'] for tarea in self.__tareas if not tarea['hecha']]
    
    def __len__(self) -> int:
        #retorna el numero total de tareas
        return len(self.__tareas)
    
    @classmethod
    def total_creadas(cls) -> int:
        #retorna el contador total de tareas creadas
        return cls.__contador
    
    #metodo auxiliar privado
    def _buscar_por_id(self, id: int) -> dict:
        #busca una tarea por ID
        for  tarea in self.__tareas:
            if tarea['id'] == id:
                return tarea
        return None
    
    #metodo adicional para debugging
    def listar_todas(self) -> list:
        #retorna todas las tareas con su estado
        return self.__tareas.copy()
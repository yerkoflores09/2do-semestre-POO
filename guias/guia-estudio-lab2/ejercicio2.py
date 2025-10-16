class GestorEventos:
    # Atributo de clase (contador global)
    creados = 0

    def _init_(self):
        # Atributo privado (diccionario de eventos)
        self.__eventos = {}  # id -> {"titulo": str, "capacidad": int, "inscritos": int}

    def registrar(self, titulo: str, capacidad: int) -> int:
        if not titulo.strip():
            raise ValueError("El título no puede estar vacío.")
        if capacidad <= 0:
            raise ValueError("La capacidad debe ser mayor que 0.")

        # Incrementar contador global
        GestorEventos.creados += 1
        id_evento = GestorEventos.creados

        # Crear el evento
        self.__eventos[id_evento] = {
            "titulo": titulo,
            "capacidad": capacidad,
            "inscritos": 0
        }

        return id_evento

    def inscribir(self, id: int, cantidad: int = 1) -> None:
        if id not in self.__eventos:
            raise ValueError("ID inválido.")
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor que 0.")

        evento = self.__eventos[id]
        if evento["inscritos"] + cantidad > evento["capacidad"]:
            raise ValueError("No hay cupos disponibles suficientes.")

        evento["inscritos"] += cantidad

    def cancelar(self, id: int, cantidad: int = 1) -> None:
        if id not in self.__eventos:
            raise ValueError("ID inválido.")
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor que 0.")

        evento = self.__eventos[id]
        if cantidad > evento["inscritos"]:
            raise ValueError("No puedes cancelar más de los inscritos.")

        evento["inscritos"] -= cantidad

    def cupos_disponibles(self, id: int) -> int:
        if id not in self.__eventos:
            raise ValueError("ID inválido.")
        evento = self.__eventos[id]
        return evento["capacidad"] - evento["inscritos"]

    def _len_(self) -> int:
        return len(self.__eventos)

    @classmethod
    def total_creados(cls) -> int:
        return cls.creados
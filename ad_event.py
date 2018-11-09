class AdEvent:
    """Implementa um evento do simulador, que devera ser incluido numa fila.
    """
    def __init__(self, e_time, e_type, e_data):
        """Cria um novo evento com os parametros selecionados.

        :param e_time: float. tempo de chegada do evento na fila.
        :param e_type: int. tipo do evento.
        :param e_data: dados relacionados ao evento.
        """
        self.e_time = e_time
        self.e_type = e_type
        self.e_data = e_data
        self.e_pointer = None

class AdEvent:
    """Implementa um evento do simulador, que devera ser incluido numa lista de eventos.
    """
    def __init__(self, e_time, e_type, e_data):
        """Cria um novo evento com os parametros selecionados.

        :param e_time: float. tempo de chegada do evento na lista.
        :param e_type: int. tipo do evento.
        :param e_data: dados relacionados ao evento.
        """
        self.e_time = e_time
        self.e_type = e_type
        self.e_data = e_data
        self.e_pointer = None


class AdEventList:
    """ Implementa uma lista de eventos.
    """
    def __init__(self):
        """ Cria uma lista vazia.
        """
        self.list_size = 0
        self.list_events = []

    def list_is_empty(self):
        """ Verifica se a lista esta vazia.

        :return: Retorna True se vazia, False caso contrario.
        """
        if self.list_size == 0:
            return True
        else:
            return False

    def binary_search(self, time_of_new_event):
        """Usa busca binaria para determinar posicao do novo evento da lista.

        :param time_of_new_event: float. Tempo de ocorrencia do novo evento.
        :return: posicao da lista a ser inserido o novo evento.
        """
        # ToDo: Implementar a busca binaria e colocar retorno adequado.
        return len(self.list_events) + time_of_new_event

    def list_add(self, new_event):
        """
        Insere novo evento na lista. Atualiza os ponteiros dos eventos ao redor.
        Opera busca binaria para inserir no tempo correto.

        :param new_event: AdEvent. Novo evento a ser inserido.
        """
        if self.list_size == 0:
            self.list_events.append(new_event)
        else:
            position = self.binary_search(new_event.e_time)
            if position == 0:
                new_event.e_pointer = self.list_events[0]
            elif position == self.list_size - 1:
                self.list_events[-1].e_pointer = new_event
            else:
                self.list_events[position - 1].e_pointer = new_event
                new_event.e_pointer = self.list_events[position]
            self.list_events.insert(position, new_event)
        self.list_size += 1

    def list_pop(self):
        """Retorna o proximo evento a ser tratado.

        :return: Evento a ser tratado.
        """
        if self.list_size == 0:
            print("Error: attempt to pop empty queue")
            exit()
        self.list_size -= 1
        return self.list_events.pop(0)

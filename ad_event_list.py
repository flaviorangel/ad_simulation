class AdEvent:
    """Implementa um evento do simulador, que devera ser incluido numa lista de eventos.
    """
    def __init__(self, e_time, e_type, e_data=None,serv_begin_time=None):
        """Cria um novo evento com os parametros selecionados.

        :param e_time: float. tempo de chegada do evento na lista.
        :param e_type: int. tipo do evento. 0: chegada de cliente. 1: termino de atendimento.
        :param e_data: dados relacionados ao evento.
        """
        self.e_time = e_time
        self.e_type = e_type
        self.e_data = e_data
        self.serv_begin_time = serv_begin_time
        self.e_pointer = None


class AdEventList:
    """ Implementa uma lista de eventos.
    """
    def __init__(self):
        """ Cria uma lista vazia.
        """
        self.list_size = 0
        self.list_of_events = []

    def list_is_empty(self):
        """ Verifica se a lista esta vazia.

        :return: Retorna True se vazia, False caso contrario.
        """
        if self.list_size == 0:
            return True
        else:
            return False

    def print_time_of_events(self):
        print("[", end="")
        for i in range(0, self.list_size - 1):
            print(self.list_of_events[i].e_time, " ", end="")
        print(self.list_of_events[self.list_size - 1].e_time, "]")

    def binary_search(self, first_last, time_of_new_event):
        """Usa busca binaria para determinar posicao do novo evento na lista.

        :param first_last: array de 2 int. Representa primeira e ultima posicao a considerar na busca.
        :param time_of_new_event: float. Tempo de ocorrencia do novo evento.
        :return: posicao da lista a ser inserido o novo evento.
        """
        if first_last[0] == first_last[1]:
            if time_of_new_event > self.list_of_events[first_last[0]].e_time:
                return first_last[0] + 1
            else:
                return first_last[0]
        else:
            odd_size = False
            if (first_last[0] - first_last[1]) % 2 == 0:
                odd_size = True
            middle = (first_last[1] + first_last[0]) // 2
            if odd_size:
                if time_of_new_event < self.list_of_events[middle].e_time:
                    return self.binary_search([first_last[0], middle - 1], time_of_new_event)
                elif time_of_new_event > self.list_of_events[middle].e_time:
                    return self.binary_search([middle + 1, first_last[1]], time_of_new_event)
                else:
                    return middle
            else:
                if time_of_new_event < self.list_of_events[middle + 1].e_time:
                    return self.binary_search([first_last[0], middle], time_of_new_event)
                elif time_of_new_event > self.list_of_events[middle].e_time:
                    return self.binary_search([middle + 1, first_last[1]], time_of_new_event)
                else:
                    return middle

    def list_add(self, new_event, print_flag=False):
        """
        Insere novo evento na lista. Atualiza os ponteiros dos eventos ao redor.
        Opera busca binaria para inserir no tempo correto.

        :param new_event: AdEvent. Novo evento a ser inserido.
        :param print_flag: boolean. se True, printa informacoes ao final.
        """
        if self.list_size == 0 or \
           new_event.e_time > self.list_of_events[self.list_size - 1].e_time:
            self.list_of_events.append(new_event)
            if print_flag:
                print("event with time " + str(new_event.e_time) + " appended to list")
        else:
            position = self.binary_search([0, self.list_size - 1], new_event.e_time)
            if position == 0:
                new_event.e_pointer = self.list_of_events[0]
            else:
                self.list_of_events[position - 1].e_pointer = new_event
                new_event.e_pointer = self.list_of_events[position]
            self.list_of_events.insert(position, new_event)
            if print_flag:
                print("event with time " + str(new_event.e_time) + " added to position ", position)
        self.list_size += 1
        if print_flag:
            self.print_time_of_events()

    def list_pop(self):
        """Retorna o proximo evento a ser tratado.

        :return: Evento a ser tratado.
        """
        if self.list_size == 0:
            print("Error: attempt to pop empty queue")
            exit()
        self.list_size -= 1
        return self.list_of_events.pop(0)


if __name__ == "__main__":
    print("testing routines...")
    my_event_list = AdEventList()
    print("is list empty?")
    print(my_event_list.list_is_empty())
    my_event_list.list_add(AdEvent(1, 0, 0), True)
    my_event_list.list_add(AdEvent(3, 0, 0), True)
    my_event_list.list_add(AdEvent(5, 0, 0), True)
    print(my_event_list.list_pop().e_time)
    my_event_list.list_add(AdEvent(2, 0, 0), True)
    my_event_list.list_add(AdEvent(2.5, 0, 0), True)
    my_event_list.list_add(AdEvent(2.7, 0, 0), True)
    print(my_event_list.list_pop().e_time)
    my_event_list.list_add(AdEvent(1.5, 0, 0), True)
    my_event_list.list_add(AdEvent(0, 0, 0), True)
    my_event_list.list_add(AdEvent(4, 0, 0), True)
    my_event_list.list_add(AdEvent(4.2, 0, 0), True)
    print(my_event_list.list_pop().e_time)
    my_event_list.list_add(AdEvent(6, 0, 0), True)
    my_event_list.list_add(AdEvent(8, 0, 0), True)
    print(my_event_list.list_pop().e_time)


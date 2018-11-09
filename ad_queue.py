class AdQueue:
    """ Implementa uma fila do tipo FCFS ou LCFS.
    """
    def __init__(self, q_type):
        """ Cria uma nova fila do tipo selecionado.

        :param q_type: bool. Define se FCFS (True) ou LCFS (False)
        """
        self.q_type = q_type
        self.q_size = 0
        self.q_members = []

    def q_is_empty(self):
        """ Verifica se a fila esta vazia.

        :return: Retorna True se vazia, False caso contrario.
        """
        if self.q_size == 0:
            return True
        else:
            return False

    def q_push(self, new_event):
        """ Insere novo evento na fila. Posicao dependera do tipo da fila. Atualiza os ponteiros dos eventos.

        :param new_event: AdEvent. Novo evento a ser inserido.
        """
        if self.q_type:  # Se q_type True, tipo eh FCFS. No caso, evento ingressa no final da fila.
            if not self.q_is_empty():  # Em FCFS, o antigo ultimo da fila aponta para o novo evento.
                self.q_members[-1].e_pointer = new_event
            self.q_members.append(new_event)
        else:
            if not self.q_is_empty():  # Em LCFS, o novo evento aponta para o antigo 1o da fila.
                new_event.e_pointer = self.q_members[0]
            self.q_members.insert(0, new_event)
        self.q_size += 1

    def q_pop(self):
        """ Faz a fila andar.

        :return: Evento a ser servido.
        """
        if self.q_size == 0:
            print("Error: attempt to pop empty queue")
            exit()
        self.q_size -= 1
        return self.q_members.pop(0)

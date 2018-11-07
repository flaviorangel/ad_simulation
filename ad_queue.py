class Queue:
    """ Implementa uma fila do tipo FCFS ou LCFS
    """
    def __init__(self, q_type):
        """ Cria uma nova fila do tipo selecionado.

        :param q_type: bool. Define se FCFS (True) ou LCFS (False)
        """
        self.q_type = q_type
        self.q_size = 0
        self.q_members = []

    def is_empty(self):
        """ Verifica se a fila esta vazia.

        :return: Retorna True se vazia, False caso contrario.
        """
        if self.q_size == 0:
            return True
        else:
            return False

    def q_push(self, new_member):
        """ Insere novo membro na fila. Posicao dependera do tipo da fila.

        :param new_member: Novo membro a ser inserido.
        """
        if self.q_type:
            self.q_members.append(new_member)
        else:
            self.q_members.insert(0, new_member)
        self.q_size += 1

    def q_pop(self):
        """ Retira proximo membro da fila.

        :return: Membro removido da fila.
        """
        if self.q_size == 0:
            print("Error: attempt to pop empty queue")
            exit()
        self.q_size -= 1
        return self.q_members.pop(0)

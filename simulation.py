import exponential
import ad_event_list
import time
import numpy as np


class Queue:
    def __init__(self, type_of_queue):
        """Define uma fila FCFS ou LCFS.

        :param type_of_queue: boolean. True para FCFS ou False para LCFS.
        """
        self.type_of_queue = type_of_queue
        self.queue_size = 0
        self.clients = []

    def queue_is_empty(self):
        """ Verifica se a fila esta vazia.

        :return: Retorna True se vazia, False caso contrario.
        """
        if self.queue_size == 0:
            return True
        else:
            return False

    def print_queue(self):
        """Imprime a fila.
        """
        for i in range(0, len(self.clients)):
            print(self.clients[i])

    def queue_add(self, new_client, print_flag=False):
        """
        Insere novo cliente na fila.

        :param new_client: int. ID do novo cliente a inserir.
        :param print_flag: boolean. se True, printa informacoes ao final.
        """
        if self.type_of_queue or self.queue_size == 0:
            self.clients.append(new_client)
        else:
            self.clients.insert(0)
        self.queue_size += 1
        if print_flag:
            print("inserted ID ", new_client)
            self.print_queue()

    def queue_pop(self):
        """Retorna o proximo cliente a ser tratado.

        :return: ID do cliente a ser tratado.
        """
        if self.queue_size == 0:
            print("Error: attempt to pop empty queue")
            exit()
        self.queue_size -= 1
        return self.clients.pop(0)


class Simulation:
    def __init__(self, type_of_queue, average_service_time, average_client_arrival_time,rounds):
        """Define classe de simulacao com os parametros dados.

        :param type_of_queue: boolean. True para FCFS ou False para LCFS.
        :param average_service_time: tempo medio de atendimento do servidor.
        :param average_client_arrival_time: tempo medio entre chegadas de clientes.
        :param rounds: numero de rodadas da simulação
        """
        self.service = exponential.Exponential(1/average_service_time)
        self.client = exponential.Exponential(1/average_client_arrival_time)
        self.simulation_time = 0
        self.server_available = True
        self.client_in_queue = False
        self.my_queue = Queue(type_of_queue)
        self.my_event_list = ad_event_list.AdEventList()
        self.next_client_id = 0
        self.rounds = rounds

    def print_information(self):
        print("Simulation time: ", self.simulation_time)
        print("Clients in queue: ", self.my_queue.queue_size)
        if not self.my_queue.queue_is_empty():
            print("Next client ID to be served: ", self.my_queue.clients[0])
        print("Server occupied: ", not self.server_available)
        print()

    def deal_with_event(self, event, print_flag=False):
        """Lida com evento, tomando acoes dependendo do tipo.
        Tipos de evento podem ser: 0: chegada de cliente; 1: termino de atendimento.

        :param event: AdEvent a ser tratado.
        :param print_flag: boolean. Se True, imprime informacoes.
        """
        if event.e_type == 0:  # chegada de cliente, e_data guarda o ID.
            self.my_queue.queue_add(event.e_data)
            next_arrival = self.simulation_time + self.client.occurence_time()
            client_arrival_event = ad_event_list.AdEvent(next_arrival, 0, self.next_client_id)
            self.next_client_id += 1
            self.my_event_list.list_add(client_arrival_event)
            if print_flag:
                print("Client ", event.e_data, " arrives in simulation time ", event.e_time)
                print("Next client arrival will be in simulation time ", next_arrival)
                print()
        elif event.e_type == 1:  # termino de atendimento
            self.server_available = True
            if print_flag:
                print("Client ", event.e_data, " ended service in simulation time ", event.e_time)
                print()
            if self.my_queue.queue_is_empty():
                return

        if self.server_available:  # inicia atendimento se servidor disponivel
            self.server_available = False
            client_id = self.my_queue.queue_pop()
            service_time=self.service.occurence_time()
            service_end_time = self.simulation_time + service_time
            service_end_event = ad_event_list.AdEvent(service_end_time, 1, client_id,self.simulation_time)
            self.my_event_list.list_add(service_end_event)
            if print_flag:
                print("Service for client ", client_id, " began.")
                print("It will end in simulation time ", service_end_time)
        if print_flag:
            print()

    def add_first_client(self):
        """Acrescenta o primeiro cliente a simulacao.
        """
        first_client = ad_event_list.AdEvent(self.client.occurence_time(), 0, self.next_client_id)
        self.my_event_list.list_add(first_client)
        self.next_client_id += 1

    def t_student_interval(self):
        """calcula o intervalo de confianca da t-student
        """

    def run_simulation(self, wait_for_key=False, few_delay=True):
        """Roda a simulacao. Os parametros permitem acompanhar os eventos, seja apertando tecla ou aguardando.
        Se nenhum destes for escolhido, nada sera impresso ao longo.

        :param wait_for_key: boolean. Se True, a simulacao aguardara que o usuario pressione botao.
                             Desconsidera o atraso no tempo, se houver.
        :param few_delay: boolean. Se True, alguns segundos de atraso serao acrescentados.
        """

        kmin=1000
        counter=0
        is_transient=True
        self.add_first_client()
        print("----- SIMULATION STARTED -----")
        print()
        print_events = False
        if wait_for_key or few_delay:
            print_events = True

        #fase transiente
        #o final da fase transiente será determinado quando a média do tempo total começar a convergir
        print("-------INICIO DA FASE TRANSIENTE-------")
        print()
        current_mean=9999999
        prev_mean=1
        start_time_list=[]
        total_time_list_transient=[]
        while is_transient:
            if print_events:
                print("--------------------")
            next_event = self.my_event_list.list_pop()
            #print(next_event.e_data,next_event.e_type,next_event.e_time)
            if next_event.e_type==0:
                start_time_list.append(next_event.e_time)
                #print(len(start_time_list))
            self.simulation_time = next_event.e_time
            self.deal_with_event(next_event, print_events)
            if next_event.e_type==1:
                total_time_list_transient.append(self.simulation_time-start_time_list[next_event.e_data])
                current_mean=sum(total_time_list_transient)/len(total_time_list_transient)
                #print(len(total_time_list_transient))
                if abs((current_mean/prev_mean)-1)<=0.00001:
                    is_transient=False
                prev_mean=current_mean
            if print_events:
                self.print_information()
            if few_delay and not wait_for_key:
                time.sleep(2)
            if wait_for_key:
                print("Press any key to continue...")
                print()
                input()
        print("-------FINAL DA FASE TRANSIENTE-------")
        print()
        print(next_event.e_data)    


        #fora da fase transiente    
        for i in range(self.rounds):
            counter=0
            wait_time_list=[]
            number_of_people_queue_list=[] #lista que ira guardar o total de pessoas na fila
            #print("inicio da rodada:", i)
            while counter<kmin:
                if print_events:
                    print("--------------------")
                next_event = self.my_event_list.list_pop()
                #print(next_event.e_data,next_event.e_type,next_event.e_time)
                if next_event.e_type==1:
                    counter+=1
                else:
                    start_time_list.append(next_event.e_time)
                self.simulation_time = next_event.e_time 
                self.deal_with_event(next_event, print_events)
                if next_event.e_type==1:
                    number_of_people_queue_list.append(self.my_queue.queue_size)
                    wait_time_list.append(next_event.serv_begin_time-start_time_list[next_event.e_data])
                if print_events:
                    self.print_information()
                if few_delay and not wait_for_key:
                    time.sleep(2)
                if wait_for_key:
                    print("Press any key to continue...")
                    print()
                    input()
            #estatisticas do N
            est_mean_N=sum(number_of_people_queue_list)/len(number_of_people_queue_list)
            
            var_aux_list=[]
            for c in number_of_people_queue_list:
                var_aux_list.append((c-est_mean_N)**2)
            est_var_N=sum(var_aux_list)/(len(var_aux_list)-1)
            
            #estatisticas do W
            est_mean_W=sum(wait_time_list)/len(wait_time_list)
            
            var_aux_list=[]
            for f in wait_time_list:
                var_aux_list.append((f-est_mean_W)**2)
            est_var_W=sum(var_aux_list)/(len(var_aux_list)-1)
            
            #calculo do intervalo de confianca

            if print_events:
                print("media de W rodada",i," é igual a ")
                print(est_mean_W)
                print("variancia de W na rodada",i," é igual a ")
                print(est_var_W)

                print("media de N rodada",i," é igual a ")
                print(est_mean_N)
                print("variancia de N na rodada",i," é igual a ")
                print(est_var_N)

if __name__ == "__main__":
    my_simulation = Simulation(True, 1, 0.2)
    my_simulation.run_simulation(wait_for_key=True)

"""#todo: eliminar overhead de eventos que entram e não terminam
        intervalos de confiança
        determinar kmin
        
"""
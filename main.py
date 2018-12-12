import simulation

if __name__ == "__main__":
    type_of_queue = False  # True para FCFS e False para LCFS
    average_service_time = 1
    utilization=0.2
    average_client_arrival_time = 1/utilization
    rounds=3200
    
    #kmin determinado experimentalmente. 3000 para LCFS e 2850 para FCFS
    kmin=3000

    my_simulation = simulation.Simulation(type_of_queue, average_service_time,average_client_arrival_time,rounds, kmin)
    my_simulation.run_simulation(wait_for_key=False, few_delay=False)

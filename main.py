import simulation

if __name__ == "__main__":
    type_of_queue = True  # True para FCFS e False para LCFS
    average_service_time = 1
    average_client_arrival_time = 1/0.2
    rounds=3200


    my_simulation = simulation.Simulation(type_of_queue, average_service_time,average_client_arrival_time,rounds)
    my_simulation.run_simulation(wait_for_key=False, few_delay=False)

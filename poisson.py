import random as rdn
import math


class Poisson:
    def __init__(self, my_lambda):
        self.my_lambda = my_lambda
        self.my_random = rdn.SystemRandom()

    def arrival_time(self):
        """Calcula uma chegada Poisson com base na PDF.
        :return: tempo da chegada Poisson.
        """
        random_pdf = self.my_random.random()
        return math.log(1 - random_pdf)/(-self.my_lambda)


if __name__ == "__main__":
    print("testing poisson class")
    my_poisson = Poisson(2)
    add_numbers = 0
    add_numbers += my_poisson.arrival_time()
    add_numbers += my_poisson.arrival_time()
    add_numbers += my_poisson.arrival_time()
    add_numbers += my_poisson.arrival_time()
    add_numbers += my_poisson.arrival_time()
    add_numbers += my_poisson.arrival_time()
    add_numbers += my_poisson.arrival_time()
    add_numbers += my_poisson.arrival_time()
    add_numbers += my_poisson.arrival_time()
    add_numbers += my_poisson.arrival_time()
    add_numbers += my_poisson.arrival_time()
    add_numbers += my_poisson.arrival_time()
    add_numbers += my_poisson.arrival_time()
    add_numbers += my_poisson.arrival_time()
    add_numbers += my_poisson.arrival_time()
    add_numbers += my_poisson.arrival_time()
    add_numbers += my_poisson.arrival_time()
    add_numbers += my_poisson.arrival_time()
    add_numbers += my_poisson.arrival_time()
    add_numbers += my_poisson.arrival_time()
    add_numbers += my_poisson.arrival_time()
    add_numbers += my_poisson.arrival_time()
    add_numbers += my_poisson.arrival_time()
    add_numbers += my_poisson.arrival_time()
    add_numbers += my_poisson.arrival_time()
    add_numbers += my_poisson.arrival_time()
    add_numbers += my_poisson.arrival_time()
    add_numbers += my_poisson.arrival_time()
    add_numbers += my_poisson.arrival_time()
    add_numbers += my_poisson.arrival_time()
    print(add_numbers/30)
    # print(my_poisson.arrival_time())
    # print(my_poisson.arrival_time())
    # print(my_poisson.arrival_time())
    # print(my_poisson.arrival_time())
    # print(my_poisson.arrival_time())
    # print(my_poisson.arrival_time())
    # print(my_poisson.arrival_time())
    # print(my_poisson.arrival_time())
    # print(my_poisson.arrival_time())
    # print(my_poisson.arrival_time())
    # print(my_poisson.arrival_time())
    # print(my_poisson.arrival_time())
    # print(my_poisson.arrival_time())
    # print(my_poisson.arrival_time())
    # print(my_poisson.arrival_time())
    # print(my_poisson.arrival_time())
    # print(my_poisson.arrival_time())
    # print(my_poisson.arrival_time())
    # print(my_poisson.arrival_time())
    # print(my_poisson.arrival_time())
    # print(my_poisson.arrival_time())

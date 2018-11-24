import random as rdn
import math


class Exponential:
    def __init__(self, rate):
        self.rate = rate
        self.my_random = rdn.SystemRandom()

    def occurence_time(self):
        """Calcula o tempo de ocorrencia da exponencial.
        :return: tempo de ocorrencia.
        """
        random_pdf = self.my_random.random()
        return math.log(1 - random_pdf)/(-self.rate)


if __name__ == "__main__":
    print("testing poisson class")
    my_exponential = Exponential(2)
    add_numbers = 0
    add_numbers += my_exponential.occurence_time()
    add_numbers += my_exponential.occurence_time()
    add_numbers += my_exponential.occurence_time()
    add_numbers += my_exponential.occurence_time()
    add_numbers += my_exponential.occurence_time()
    add_numbers += my_exponential.occurence_time()
    add_numbers += my_exponential.occurence_time()
    add_numbers += my_exponential.occurence_time()
    add_numbers += my_exponential.occurence_time()
    add_numbers += my_exponential.occurence_time()
    add_numbers += my_exponential.occurence_time()
    add_numbers += my_exponential.occurence_time()
    add_numbers += my_exponential.occurence_time()
    add_numbers += my_exponential.occurence_time()
    add_numbers += my_exponential.occurence_time()
    add_numbers += my_exponential.occurence_time()
    add_numbers += my_exponential.occurence_time()
    add_numbers += my_exponential.occurence_time()
    add_numbers += my_exponential.occurence_time()
    add_numbers += my_exponential.occurence_time()
    add_numbers += my_exponential.occurence_time()
    add_numbers += my_exponential.occurence_time()
    add_numbers += my_exponential.occurence_time()
    add_numbers += my_exponential.occurence_time()
    add_numbers += my_exponential.occurence_time()
    add_numbers += my_exponential.occurence_time()
    add_numbers += my_exponential.occurence_time()
    add_numbers += my_exponential.occurence_time()
    add_numbers += my_exponential.occurence_time()
    add_numbers += my_exponential.occurence_time()
    print(add_numbers/30)
    # print(my_exponential.occurence_time())
    # print(my_exponential.occurence_time())
    # print(my_exponential.occurence_time())
    # print(my_exponential.occurence_time())
    # print(my_exponential.occurence_time())
    # print(my_exponential.occurence_time())
    # print(my_exponential.occurence_time())
    # print(my_exponential.occurence_time())
    # print(my_exponential.occurence_time())
    # print(my_exponential.occurence_time())
    # print(my_exponential.occurence_time())
    # print(my_exponential.occurence_time())
    # print(my_exponential.occurence_time())
    # print(my_exponential.occurence_time())
    # print(my_exponential.occurence_time())
    # print(my_exponential.occurence_time())
    # print(my_exponential.occurence_time())
    # print(my_exponential.occurence_time())
    # print(my_exponential.occurence_time())
    # print(my_exponential.occurence_time())
    # print(my_exponential.occurence_time())

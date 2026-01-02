import random
rand_list = [random.randrange(1,20) for _ in range(10)]

list_comprehension_below_10 = [i for i in rand_list if i<10]

def below_10(i):
    return i<10
list_comprehension_below_10 = list(filter(below_10,rand_list))
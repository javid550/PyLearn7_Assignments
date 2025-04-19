import random

def get_non_repeating_random_2d_list (start , end) :
    numbers = list(range(1 ,17))
    random.shuffle(numbers)

    grid = [numbers[i*4:(i+1)*4] for i in range(4)]
    return grid 
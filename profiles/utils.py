import random

available_number  = [x for x in range(10)]
size = 26

def generate_account_number():
    new_number_list = [str(random.choice(available_number)) for _ in range(size)]
    # print(new_number_list)
    new_number_str = "".join(new_number_list)
    # print(new_number_str)
    return new_number_str
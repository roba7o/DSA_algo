import random
import time

"""
Self Check:
Write two Python functions to find the minimum number in a list. 
The first function should compare each number to every other number on the list. 
The second function should be linear.

"""


def list_search_linear(input_list: list) -> int:
    start_time = time.time()
    min = input_list[0]
    for num in input_list:
        if num < min:
            min = num

    end_time = time.time()
    return min, (end_time - start_time)

def list_search_cubic(input_list: list) -> list:
    start_time = time.time()
    over_all_min = input_list[0]
    for i in input_list:
        is_smallest = True
        for j in input_list:
            if i > j:
                is_smallest = False
        if is_smallest:
            over_all_min = i
    end_time = time.time()
    return over_all_min, (end_time - start_time)

def random_list_generator():
    ran_list = [random.randrange(40) for i in range(10)]
    print(ran_list)
    return ran_list
    


if __name__ == "__main__":
    random_list = random_list_generator()
    result_linear = list_search_linear(random_list)
    result_cubic = list_search_cubic(random_list)

    print(f"cubic: {result_linear[0]} took {result_linear[1]} seconds")
    print(f"linear {result_cubic[0]} took {result_cubic[1]} seconds")



import random


def get_single_item(operation):
    """return a and b and answer,data_range(4*3)"""
    num_a = random.randint(1000, 10000)
    num_b = random.randint(100, 1000)
    answer = eval(str(num_a)+operation+str(num_b))
    return num_a, num_b, answer


def get_five_error_item(operation):
    """return 5 error practice ,data_range(3*2)"""
    item_list = []
    for i in range(5):
        num_a = random.randint(100, 1000)
        num_b = random.randint(10, 100)
        answer = eval(str(num_a)+operation+str(num_b))
        item_list.append((num_a, num_b, answer))
    return item_list


if __name__ == '__main__':
    result = get_five_error_item("*")
    print(result)


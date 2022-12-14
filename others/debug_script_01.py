#======================================
# file name:debug_script.py
# author:liangliangSu
# date of writing:2022-09-16 00:17
#======================================
#!/usr/bin/env python3
from loguru import logger
from itertools import combinations

def division(num1: int, num2: int):
    return num1/num2

@logger.catch # Add this to track errors
def divide_numbers(num_list: list):
    for comb in combinations(num_list, 2):
        num1, num2 = comb
        res = division(num1, num2)
        print(f"{num1} divided by {num2} is equal to {res}.")

if __name__ =='__main__':
    num_list = [2, 1, 0]
    divide_numbers(num_list)

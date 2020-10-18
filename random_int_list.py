# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 20:25:43 2020

@author: 30790
"""

import random
def random_int_list(start, stop, length):
    start, stop = (int(start), int(stop)) if start <= stop else (int(stop), int(start))
    length = int(abs(length)) if length else 0
    random_list = []
    for i in range(length):
        random_number=random.randint(start, stop)
        while(random_number in random_list):
            random_number=random.randint(start, stop)
        random_list.append(random_number)   
    return random_list

if __name__ == '__main__':
    q=random_int_list(0,60,6)
    print(q)
#!/usr/bin/env python3

def get_methods_string():
    count: int = 0
    for method in dir(str):
        if '__' not in method:
            count +=1
            print(count, method, sep=':')


get_methods_string()
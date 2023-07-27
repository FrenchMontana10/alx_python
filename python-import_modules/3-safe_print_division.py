#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a / b
    except:
        result = home
    finally: 
        print("Inside result: {}".format(result))
        return(result)
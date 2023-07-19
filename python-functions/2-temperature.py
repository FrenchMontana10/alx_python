#!/usr/bin/env python3
def convert_to_celcius(fahrenheit):
    celcius = (fahrenheit - 32) * 5 / 9
    return celcius
result = convert_to_celcius(75)
print(result)
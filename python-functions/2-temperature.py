def main():
    convert_to_celcius(100)
    convert_to_celcius(-40)
    convert_to_celcius(-459.67)
    convert_to_celcius(32)

def convert_to_celcius(fahrenheit):
    celcius = (fahrenheit - 32) * 5 / 9
    return celcius

main()
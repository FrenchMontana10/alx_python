import sys

def main():
    num_arguments = len(sys.argv) - 1

    print(f"Number of argument(s): {num_arguments}", end=' ')

    if num_arguments == 1:
        print("argument", end='')
    else:
        print("arguments", end='')

        print(":" if num_arguments > 0 else ".")

    if num_arguments > 0:
        for i, arg in enumerate(sys.argv[1:], start=1):
            print(f"{i}: {arg}")

if __name__ == "__main__":
    main()
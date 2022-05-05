import sys

def add_two_nums(num1: int, num2: int):
    sum = num1 + num2
    return sum

if __name__ == "__main__":
    num1 = int(sys.argv[1])
    num2 = int(sys.argv[2])
    sum = add_two_nums(num1, num2)
    print(f"sum: {sum}")


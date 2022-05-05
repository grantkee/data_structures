import sys

def find_factorial(n):
    factorial = 1
    for num in range(2, n + 1):
        factorial *= num
    return factorial

if __name__ == "__main__":
    factorial = find_factorial(int(sys.argv[1]))
    print(f"{factorial}")

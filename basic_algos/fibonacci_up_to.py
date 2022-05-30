import sys

def fibonacci_up_to(n):
    a = 1
    b = 2
    while a <= n:
        tmp = a
        a = a + b
        b = tmp
    return b

if __name__ == "__main__":
    num = int(sys.argv[1])
    print(fibonacci_up_to(num))

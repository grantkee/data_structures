import sys

def fibonacci_up_to(n):
    a = 0
    b = 1
    print(b)
    while a <= n:
        tmp = a
        a = a + b
        b = tmp
        print(b)

if __name__ == "__main__":
    num = int(sys.argv[1])
    fibonacci_up_to(num)

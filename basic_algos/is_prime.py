import sys

def is_prime(n):
    prime = True
    i = 2
    while i <= n/2:
        if n%i == 0:
            prime = False
        i += 1
    return prime

if __name__ == "__main__":
    num = int(sys.argv[1])
    if is_prime(num) or num == 3:
        print(f"{num} is prime")
    else:
        print(f"{num} is not prime")

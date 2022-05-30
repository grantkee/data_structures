import sys

def find_largest_number(args):
    print(f"{args}")
    largest = int(args[0])
    for a in args:
        num = int(a)
        if num > largest:
            largest = num
    return largest

if __name__ == "__main__":
    print(find_largest_number(sys.argv[1:]))

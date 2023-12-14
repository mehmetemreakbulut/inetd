import sys

def square(num):
    return num ** 2

if __name__ == "__main__":
    input_num = int(sys.argv[1])
    result = square(input_num)
    sys.stdout.write(str(result))

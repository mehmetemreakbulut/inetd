import sys

def cube(num):
    return num ** 3

if __name__ == '__main__':
    input_num = int(sys.argv[1])
    result = cube(input_num)
    sys.stdout.write(str(result))

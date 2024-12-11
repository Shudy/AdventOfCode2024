import re

memory_data = ''
mul_operations = []

mul_regex = r"mul\((\d{1,3}),(\d{1,3})\)"


def read_data(path):
    global memory_data
    with open(path) as f:
        memory_data = f.read()
    f.close()


def find_mul_operations():
    global mul_operations
    mul_operations = re.findall(mul_regex, memory_data)


def execute_mul_operations():
    result = 0
    for operation in mul_operations:
        result += int(operation[0]) * int(operation[1])
    return result


def main():
    read_data('../data/day3')

    print(f'--------PART 1--------')
    find_mul_operations()
    print(f"Result of the memory: {execute_mul_operations()}")


if __name__ == '__main__':
    main()

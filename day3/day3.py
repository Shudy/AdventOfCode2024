import re

memory_data = ''
mul_regex = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")
mul_regex_tokens = re.compile(r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)")


def read_data(path):
    global memory_data
    with open(path) as f:
        memory_data = f.read()
    f.close()


def execute_mul_operations():
    result = 0
    mul_operations = re.findall(mul_regex, memory_data)
    for operation in mul_operations:
        result += int(operation[0]) * int(operation[1])
    return result


def execute_advanced_mul_operations():
    mul_enabled = True
    result = 0
    tokens = re.findall(mul_regex_tokens, memory_data)
    for token in tokens:
        if token == "do()":
            mul_enabled = True
        elif token == "don't()":
            mul_enabled = False
        else:
            if mul_enabled:
                match = re.match(mul_regex, token)
                if match:
                    result += int(match.groups()[0]) * int(match.groups()[1])

    return result


def main():
    read_data('../data/day3')

    print(f'--------PART 1--------')
    print(f"Result of the memory: {execute_mul_operations()}")

    print(f'--------PART 2--------')
    print(f"Result of advances memory: {execute_advanced_mul_operations()}")


if __name__ == '__main__':
    main()

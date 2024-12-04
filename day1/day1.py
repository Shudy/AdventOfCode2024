first_numbers = []
second_numbers = []


def read_data(path):
    with open(path) as f:
        for line in f.readlines():
            numbers = [int(num) for num in line.split()]
            if len(numbers) == 2:
                first_numbers.append(numbers[0])
                second_numbers.append(numbers[1])
    f.close()


def sort_min_to_max(numbers):
    return numbers.sort()


def calculate_distance():
    total_distance = 0
    for i in range(len(first_numbers)):
        total_distance += abs(first_numbers[i] - second_numbers[i])
    return total_distance


def count_similarities():
    total_similarity = 0
    for i in range(len(first_numbers)):
        number = first_numbers[i]
        number_occurrences = second_numbers.count(number)
        number_similarity = number * number_occurrences
        total_similarity += number_similarity
    return total_similarity


def main():
    read_data('../data/day1')

    # Part 1: Calculate the distance between the two lists
    sort_min_to_max(first_numbers)
    sort_min_to_max(second_numbers)

    print(f'Total distance: {calculate_distance()}')

    # Part 2: Calculate the similarity between the two lists
    print(f'Similarity: {count_similarities()}')


if __name__ == '__main__':
    main()

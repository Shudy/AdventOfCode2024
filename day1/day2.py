reports = []


def read_data(path):
    with open(path) as f:
        for line in f.readlines():
            report = [int(num) for num in line.split()]
            reports.append(report)
    f.close()


def is_report_safe(report: list[int]):
    distances = []
    for i in range(len(report) - 1):
        distances.append(report[i] - report[i + 1])

    if all(distance < 0 for distance in distances) or all(distance > 0 for distance in distances):
        if all(abs(distance) in range(1, 4) for distance in distances):
            return True
    return False


def main():
    read_data('../data/day2')
    number_of_save_reports = 0
    for report in reports:
        if is_report_safe(report):
            number_of_save_reports += 1

    print(f'Number of save reports: {number_of_save_reports}')


if __name__ == '__main__':
    main()

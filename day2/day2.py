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


def is_possible_to_fix_report(report: list[int]):
    for i in range(len(report)):
        alternative_report = report.copy()
        alternative_report.pop(i)
        if is_report_safe(alternative_report):
            return True
    return False


def main():
    read_data('../data/day2')
    unsafe_reports = []
    # Part 1:
    number_of_safe_reports = 0
    for report in reports:
        if is_report_safe(report):
            number_of_safe_reports += 1
        else:
            unsafe_reports.append(report)

    print(f'--------PART 1--------')
    print(f'Number of safe reports: {number_of_safe_reports}')
    print(f'Number of unsafe reports: {len(unsafe_reports)}')

    # Part 2:
    fixed_reports = 0
    for unsafe_report in unsafe_reports:
        if is_possible_to_fix_report(unsafe_report):
            fixed_reports += 1
    total_safe_reports = number_of_safe_reports + fixed_reports

    print(f'--------PART 2--------')
    print(f'Number of fixed reports: {fixed_reports}')
    print(f'Total safe reports: {total_safe_reports}')


if __name__ == '__main__':
    main()

from itertools import product


def evaluate_expression(operators, numbers):
    result = int(numbers[0])
    for i in range(len(operators)):
        if operators[i] == "+":
            result += int(numbers[i + 1])
        elif operators[i] == "*":
            result *= int(numbers[i + 1])
        elif operators[i] == "||":
            result = int((str(result) + numbers[i + 1]))
    return result


def can_form_test_value(test_value, numbers):
    operators = ["+", "*", "||"]
    for ops in product(operators, repeat=len(numbers) - 1):
        if evaluate_expression(ops, numbers) == test_value:
            return True
    return False


def part1(data):
    result = []

    for numbers in data:
        target_number = int(numbers[0])
        child_numbers = numbers[1].strip().split(" ")
        if can_form_test_value(target_number, child_numbers):
            result.append(target_number)
    return sum(result)


if __name__ == "__main__":
    data = []
    f = open("./input.txt", "r")
    for line in f.readlines():
        numbers = line.strip().split(":")
        data.append(numbers)
    print(part1(data))

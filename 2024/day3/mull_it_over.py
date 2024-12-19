import re


def part1(lines):
    total = 0
    for line in lines:
        # print(line)
        matches = re.findall(r"(mul\([1-9]?[0-9]?[0-9],[1-9]?[0-9]?[0-9]?\))", line)
        for match in matches:
            # print(match)
            nums = match.replace("mul", "").replace("(", "").replace(")", "").split(",")
            total += int(nums[0]) * int(nums[1])
    return total


def part2(lines):
    total = 0
    pattern = re.compile(r"(do\(\)|don't\(\)|mul\((\d+),(\d+)\))")
    enabled = True

    for line in lines:
        instructions = pattern.findall(line)
        for instruction in instructions:
            if instruction[0] == "do()":
                enabled = True
            elif instruction[0] == "don't()":
                enabled = False
            elif enabled and instruction[1] and instruction[2]:
                total += int(instruction[1]) * int(instruction[2])
    return total


if __name__ == "__main__":
    data = []
    f = open("./input.txt", "r")
    for line in f.readlines():
        data.append(line)
    print(part2(data))
    f.close()

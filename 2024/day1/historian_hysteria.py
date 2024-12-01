from collections import Counter


def part1(left_arr, right_arr):
    total_distance = 0

    for i, left_val in enumerate(left_arr):
        total_distance += abs(int(right_arr[i]) - int(left_val))

    return total_distance


def part2(left_arr, right_arr):
    score = 0
    right_counter = Counter(right_arr)
    for _, left_val in enumerate(left_arr):
        append = right_counter[left_val]
        score += int(left_val) * append

    return score


if __name__ == "__main__":
    left_arr = []
    right_arr = []
    f = open("./input.txt", "r")
    for line in f.readlines():
        words = line.strip().split(" ")
        left_arr.append(words[0])
        right_arr.append(words[3])
    f.close()

    left_arr.sort()
    right_arr.sort()
    print(part1(left_arr, right_arr))
    print(part2(left_arr, right_arr))

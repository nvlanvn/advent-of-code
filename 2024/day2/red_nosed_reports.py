def part1(reports):
    total = 0
    for _, levels in enumerate(reports):
        j = 0
        increment = False
        decrement = False
        if int(levels[0]) > int(levels[1]):
            decrement = True
        else:
            increment = True

        while j < len(levels) - 1:
            j_val = int(levels[j])
            j1_val = int(levels[j + 1])

            if decrement:
                if j_val < j1_val:
                    break
                diff = j_val - j1_val
                if diff <= 0 or diff > 3:
                    break
            if increment:
                if j_val > j1_val:
                    break
                diff = j1_val - j_val
                if diff <= 0 or diff > 3:
                    break
            j += 1
        if j == len(levels) - 1:
            total += 1
    return total


def part2(reports):
    total = 0
    for _, levels in enumerate(reports):
        original = levels
        j = 0
        increment = False
        decrement = False
        counter = 0
        while j < len(levels) - 1:
            j_val = int(levels[j])
            j1_val = int(levels[j + 1])
            if counter > 1:
                break
            if j_val == j1_val:
                counter += 1
                del levels[j + 1]
                continue
            if not decrement and not increment:
                if int(levels[0]) > int(levels[1]):
                    decrement = True
                else:
                    increment = True

            if decrement:
                diff = j_val - j1_val
                if j_val > j1_val and diff > 0 and diff <= 3:
                    j += 1
                else:
                    if counter > 0:
                        break
                    del levels[j + 1]
                    counter += 1
            if increment:
                diff = j1_val - j_val
                if j1_val > j_val and diff > 0 or diff <= 3:
                    j += 1
                else:
                    if counter > 0:
                        break
                    del levels[j + 1]
                    counter += 1
        print(
            f"original {original}, levels: {levels}, decrement: {decrement}, increment: {increment} ,condition {(j == len(levels) - 1) and counter == 0} "
        )
        if j == len(levels) - 1 and counter == 0:
            total += 1
    return total


if __name__ == "__main__":
    reports = []
    f = open("./input.txt", "r")
    for line in f.readlines():
        reports.append(line.strip().split(" "))
    print(part2(reports))
    f.close()

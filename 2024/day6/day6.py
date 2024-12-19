def find_begin(grid):
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            val = grid[row][col]
            if val == "^":
                return [row, col]
    return [0, 0]


def part1(grid):
    begin = find_begin(grid)
    result = 0
    top = 1
    right = 2
    bottom = 3
    left = 4

    direction = top

    row = begin[0]
    col = begin[1]
    pre_checked = {}
    while True:
        while row < len(grid) and col < len(grid[0]) and row >= 0 and col >= 0:
            key = f"{row}-{col}"
            if grid[row][col] != "#":
                if not pre_checked.get(key):
                    result += 1
                if direction == top:
                    row -= 1
                elif direction == right:
                    col += 1
                elif direction == bottom:
                    row += 1
                else:
                    col -= 1
                pre_checked.update({key: key})
            else:
                if direction == left:
                    print(f"left before {result}, row: {row}, col: {col}")
                    direction = 1
                    row -= 1
                    col += 1
                    print(f"left row: {row}, col: {col}")
                else:
                    if direction == top:
                        print(f"before {result}, row: {row}, col: {col}")
                        row += 1
                        col += 1
                        print(f"after row: {row}, col: {col}")
                    elif direction == right:
                        print(f"right before {result}, row: {row}, col: {col}")
                        row += 1
                        col -= 1
                        print(f"after before {result}, row: {row}, col: {col}")
                    elif direction == bottom:
                        print(f"right before {result}, row: {row}, col: {col}")
                        row -= 1
                        col -= 1
                        print(f"right before {result}, row: {row}, col: {col}")
                    direction += 1
        if row >= len(grid) or col >= len(grid[0]) or row < 0 or col < 0:
            break
    return result


if __name__ == "__main__":
    grid = []
    f = open("./input.txt", "r")
    for line in f.readlines():
        rows = list(line.strip())
        grid.append(rows)
    f.close()
    print(part1(grid))

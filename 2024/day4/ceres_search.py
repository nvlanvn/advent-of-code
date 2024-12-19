def part1(arr):
    total = 0
    xmas = "XMAS"
    xmas_revert = "SAMX"

    for row in range(len(arr)):
        for col in range(len(arr[row])):
            begin_char = arr[row][col]
            # i = row + 3
            # j = col + 3

            # check row
            if col + 3 < len(arr[col]):
                row_word = (
                    begin_char
                    + arr[row][col + 1]
                    + arr[row][col + 2]
                    + arr[row][col + 3]
                )
                if row_word == xmas or row_word == xmas_revert:
                    total += 1

            # col down
            if row + 3 < len(arr[row]):
                col_word = (
                    begin_char
                    + arr[row + 1][col]
                    + arr[row + 2][col]
                    + arr[row + 3][col]
                )
                if col_word == xmas or col_word == xmas_revert:
                    total += 1
            # # left
            if col - 3 >= 0 and row + 3 < len(arr[row]):
                left_diagonal = (
                    begin_char
                    + arr[row + 1][col - 1]
                    + arr[row + 2][col - 2]
                    + arr[row + 3][col - 3]
                )
                if left_diagonal == xmas or left_diagonal == xmas_revert:
                    total += 1
            # right
            if col + 3 < len(arr[col]) and row + 3 < len(arr[row]):
                right_diagonal = (
                    begin_char
                    + arr[row + 1][col + 1]
                    + arr[row + 2][col + 2]
                    + arr[row + 3][col + 3]
                )
                if right_diagonal == xmas or right_diagonal == xmas_revert:
                    total += 1
    return total


def part2(grid):
    patterns = [
        ["M", ".", "S"],
        [".", "A", "."],
        ["M", ".", "S"],
        ["S", ".", "M"],
        [".", "A", "."],
        ["S", ".", "M"],
    ]

    def match_pattern(grid, pattern, row, col):
        for i in range(3):
            for j in range(3):
                if pattern[i][j] != "." and grid[row + i][col + j] != pattern[i][j]:
                    return False
        return True

    count = 0
    for i in range(len(grid) - 2):
        for j in range(len(grid[0]) - 2):
            for pattern in patterns:
                if match_pattern(grid, pattern, i, j):
                    count += 1

    return count


def prepare_data(lines):
    arr = []
    for row in lines:
        characters = [c for c in row]
        arr.append(characters)
    return arr


if __name__ == "__main__":
    data = []
    f = open("./input.txt", "r")
    for line in f.readlines():
        data.append(line.strip())
    arr = prepare_data(data)
    print(part2(arr))
    f.close()

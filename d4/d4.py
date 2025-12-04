fileName = "input.txt"

width = 0
length = 0


def countNeighbours(matrix, x, y):
    count = 0
    dirs = [(1, 0), (0, 1), (1, 1), (-1, 0), (0, -1), (-1, -1), (1, -1), (-1, 1)]
    for d in dirs:
        newX = x + d[0]
        newY = y + d[1]
        if newX >= 0 and newX < width and newY >= 0 and newY < height:
            count += matrix[newY][newX]
    return count


def step(matrix):
    changed = False
    newMatrix = [[0 for _ in range(width)] for _ in range(height)]
    for y in range(height):
        for x in range(width):
            if matrix[y][x] == 1 and countNeighbours(matrix, x, y) < 4:
                newMatrix[y][x] = 0
                changed = True
            else:
                newMatrix[y][x] = matrix[y][x]
    return (newMatrix, changed)


with open(fileName) as file:
    lines = file.read().splitlines()
    width = len(lines[0])
    height = len(lines)
    matrix = [[0 for _ in range(width)] for _ in range(height)]
    for h, line in enumerate(lines):
        for w, e in enumerate(line):
            matrix[h][w] = 1 if e != "." else 0

    count1 = 0
    for y in range(height):
        for x in range(width):
            if matrix[y][x] == 1 and countNeighbours(matrix, x, y) < 4:
                count1 += 1
    print(f"Result Part 1: {count1}")

    count2 = 0
    (newMatrix, changed) = step(matrix)
    while changed:
        for y in range(height):
            for x in range(width):
                if matrix[y][x] == 1 and countNeighbours(matrix, x, y) < 4:
                    count2 += 1

        matrix = newMatrix
        (newMatrix, changed) = step(matrix)
    print(f"Result Part 2: {count2}")

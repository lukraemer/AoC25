fileName = "input.txt"


def findHighestJoltage(line):
    max = 0
    for i in range(len(line)):
        for j in range(i + 1, len(line)):
            number = int(line[i] + line[j])
            max = max if max > number else number
    return max


def findHighestJoltage2(line):
    res = []
    k = 12
    n = len(line)
    for i, d in enumerate(line):
        digit = int(d)
        while res and digit > int(res[-1]) and len(res) + n - i > k:
            res.pop()
        res.append(d)

    return int("".join(res)[:k])


with open(fileName) as file:
    sumPart1 = 0
    sumPart2 = 0
    for line in file.readlines():
        sumPart1 += findHighestJoltage(line.strip())
        # findHighestJoltage2(line.strip())
        sumPart2 += findHighestJoltage2(line.strip())

    print(f"Result Part 1: {sumPart1}")
    print(f"Result Part 2: {sumPart2}")

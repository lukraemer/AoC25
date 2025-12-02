import re


def checkForInvalidIdsPart1(number):
    number = str(number)
    if len(number) % 2 != 0:
        return 0
    middle = int(len(number) / 2)
    for i in range(middle):
        if number[i] != number[i + middle]:
            return 0
    return int(number)


def checkForInvalidIdsPart2(number):
    number = str(number)
    j = 0
    checkStr = number[j]
    while len(checkStr) < (len(number)):
        found = False
        for i in range(len(checkStr), len(number), len(checkStr)):
            if checkStr != number[i : i + len(checkStr)]:
                found = True
                break
        if not found:
            print(f"Found Number {number} with Checkstr {checkStr}")
            return int(number)
        j += 1
        checkStr += number[j]
        # print(f"Number: {number}, CheckStr: {checkStr}")
    return 0


fileName = "input.txt"

regex = r"[0-9]+-[0-9]+"
regex = r"([0-9]+)-([0-9]+)"
with open(fileName) as file:
    line = file.readline()
    sumPart1 = 0
    sumPart2 = 0
    ranges = re.findall(regex, line)
    for r in ranges:
        start = int(r[0])
        end = int(r[1])
        for i in range(start, end + 1):
            sumPart1 += checkForInvalidIdsPart1(i)
            sumPart2 += checkForInvalidIdsPart2(i)

    print(f"Result Part 1: {sumPart1}")
    print(f"Result Part 2: {sumPart2}")

fileName = "input.txt"
with open(fileName) as file:
    counter = 0
    dial = 50
    for line in file.readlines():
        dir = line[0]
        num = int(line[1:])
        if dir == "L":
            dial = (dial - num) % 100
        if dir == "R":
            dial = (dial + num) % 100
        if dial == 0:
            counter += 1
    print(f"Result Part 1: {counter}")

with open(fileName) as file:
    counter = 0
    dial = 50
    for line in file.readlines():
        dir = line[0]
        num = int(line[1:])
        if dir == "L":
            for i in range(num):
                dial = (dial - 1) % 100
                if dial == 0:
                    counter += 1
        if dir == "R":
            for i in range(num):
                dial = (dial + 1) % 100
                if dial == 0:
                    counter += 1
    print(f"Result Part 2: {counter}")

from itertools import cycle

with open("input/input.txt", "r") as f:
    instructions, map_data = f.read().split("\n\n")

    map = {}
    for line in map_data.split("\n"):
        source, destinations = line.split(" = ")
        left, right = destinations.strip("()").split(", ")
        map[source] = (left, right)

    cur = 'AAA'
    count = 0
    for inst in cycle(instructions):
        if cur == 'ZZZ':
            break
        
        if inst == 'L':
            cur = map[cur][0]
        elif inst == 'R':
            cur = map[cur][1]

        count += 1

    print(count)

from itertools import cycle
from math import lcm

with open("input/input.txt", "r") as f:
    instructions, map_data = f.read().split("\n\n")

    map = {}
    for line in map_data.split("\n"):
        source, destinations = line.split(" = ")
        left, right = destinations.strip("()").split(", ")
        map[source] = (left, right)

    def find_steps(start):
        cur = start
        count = 0
        for inst in cycle(instructions):
            if cur[2] == "Z":
                break

            if inst == "L":
                cur = map[cur][0]
            elif inst == "R":
                cur = map[cur][1]
            count += 1
        return count

    curs = [k for k in map.keys() if k[2] == "A"]
    steps = [find_steps(c) for c in curs]
    print(lcm(*steps))
    
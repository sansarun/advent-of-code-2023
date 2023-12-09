import re
import math


def find_ways(record):
    record_time, record_distance = record[0], record[1]
    ways = 0

    for charge_time in range(int(record_time) + 1):
        run_time = record_time - charge_time
        distance = charge_time * run_time

        if distance > record_distance:
            ways += 1

    return ways


with open("input/input.txt", "r") as f:
    lines = f.read().split("\n")
    times, distances = [re.split(r"\s+", line.split(":")[1].strip()) for line in lines]
    records = [(int(time), int(distance)) for time, distance in zip(times, distances)]

    result = math.prod(list(map(find_ways, records)))
    print(result)

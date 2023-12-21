def diff_sequence(case):
    slices = [case[i : i + 2] for i in range(len(case) - 1)]
    diffs = [b - a for a, b in slices]
    return diffs


def prediction(case):
    if all([num == 0 for num in case]):
        return 0
    return case[0] - prediction(diff_sequence(case))


with open("input/input.txt", "r") as f:
    lines = f.read().split("\n")
    cases = [list(map(int, line.split(" "))) for line in lines]
    print(sum([prediction(c) for c in cases]))

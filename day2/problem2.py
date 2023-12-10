def process_show(show):
    result = {}
    gem_datas = show.split(", ")
    for data in gem_datas:
        num, gem = data.split(" ")
        if gem == "red":
            result["red"] = int(num)
        elif gem == "green":
            result["green"] = int(num)
        elif gem == "blue":
            result["blue"] = int(num)

    return result


def process_game(line):
    shows = line.split(": ")[1].split("; ")

    red = [0]
    green = [0]
    blue = [0]

    for show in shows:
        show_data = process_show(show)
        red.append(show_data.get("red", 0))
        green.append(show_data.get("green", 0))
        blue.append(show_data.get("blue", 0))
    power = max(red) * max(green) * max(blue)
    return power


with open("input/input.txt", "r") as f:
    lines = f.read().split("\n")
    powers = sum(map(process_game, lines))
    print(powers)

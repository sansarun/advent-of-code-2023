def gear_number(symbol, numbers):
    adjacent_numbers = []
    for number in numbers:
        for coordinate in number["coordinates"]:
            if is_adjacent(coordinate, symbol["coordinate"]):
                adjacent_numbers.append(number)
                break

    if len(adjacent_numbers) == 2:
        return adjacent_numbers[0]["number"] * adjacent_numbers[1]["number"]
    else:
        return 0
        

def is_adjacent(c1, c2):
    if abs(c1[0] - c2[0]) <= 1 and abs(c1[1] - c2[1]) <= 1:
        return True
    return False


with open("input/input.txt", "r") as f:
    input = f.read()
    lines = input.split("\n")

    numbers = []
    symbols = []

    for lineIndex, line in enumerate(lines):
        num_buffer = ""
        coordinates_buffer = []
        for charIndex, char in enumerate(line + "."):
            if char.isdigit():
                num_buffer += char
                coordinates_buffer.append((lineIndex, charIndex))
            else:
                if num_buffer != "":
                    numbers.append(
                        {"number": int(num_buffer), "coordinates": coordinates_buffer}
                    )
                    num_buffer = ""
                    coordinates_buffer = []

                if char != ".":
                    symbols.append(
                        {"symbol": char, "coordinate": (lineIndex, charIndex)}
                    )

    gear_numbers = [gear_number(symbol, numbers) for symbol in symbols]
    print(sum(gear_numbers))

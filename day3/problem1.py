def is_relavant(number, symbols):
    for coordinate in number["coordinates"]:
        for symbol in symbols:
            if is_adjacent(coordinate, symbol):
                return True
    return False

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
        for charIndex, char in enumerate(line+"."):
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
                    symbols.append((lineIndex, charIndex))

    relavant_numbers = [number["number"] for number in numbers if is_relavant(number, symbols)]
    print(relavant_numbers)
    print(sum(relavant_numbers))


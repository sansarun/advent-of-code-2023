import re

replacements = [
    ("one", "1"),
    ("two", "2"),
    ("three", "3"),
    ("four", "4"),
    ("five", "5"),
    ("six", "6"),
    ("seven", "7"),
    ("eight", "8"),
    ("nine", "9"),
]

regex = "one|two|three|four|five|six|seven|eight|nine|1|2|3|4|5|6|7|8|9"
reverse_regex = "eno|owt|eerht|ruof|evif|xis|neves|thgie|enin|1|2|3|4|5|6|7|8|9"


def replace_words(line):
    for word, number in replacements:
        line = line.replace(word, number)

    return line


with open("input/input.txt", "r") as f:
    lines = f.read().split("\n")
    numbers = []
    for line in lines:
        reversed_line = line[::-1]
        nums = re.findall(regex, line)
        nums = [replace_words(num) for num in nums]
        first = nums[0]

        nums = re.findall(reverse_regex, reversed_line)
        last = [replace_words(num[::-1]) for num in nums][0]

        num = int(first + last)
        numbers.append(num)

    print(sum(numbers))

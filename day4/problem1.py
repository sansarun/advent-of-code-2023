import re


def card_score(card):
    numbers = card.split(":")[1]
    winning_numbers, my_numbers = numbers.strip().split("|")
    winning_numbers, my_numbers = [
        re.split(r"\s+", winning_numbers.strip()),
        re.split(r"\s+", my_numbers.strip()),
    ]

    matched_numbers = len(set(winning_numbers).intersection(set(my_numbers)))
    if matched_numbers == 0:
        return 0
    else:
        return pow(2, matched_numbers - 1)


with open("input/input.txt", "r") as f:
    input = f.read()
    cards = input.split("\n")

    total = sum([card_score(card) for card in cards])
    print(total)

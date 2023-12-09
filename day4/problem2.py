import re


def matching_num(card):
    nums = card.split(":")[1].split("|")
    winning_nums, my_nums = [re.split(r"\s+", n.strip()) for n in nums]
    return len(set(winning_nums).intersection(set(my_nums)))


def card_count(cards):
    if len(cards) == 0:
        return 0

    total = len(cards)
    for card in cards:
        new_cards = range(card + 1, card + 1 + matching_nums[card])
        total += card_count(new_cards)
    return total


with open("input/input.txt", "r") as f:
    lines = f.read().split("\n")
    matching_nums = {}
    for index, card in enumerate(lines):
        matching_nums[index] = matching_num(card)

    initial_cards = list(range(len(lines)))
    print(card_count(initial_cards))

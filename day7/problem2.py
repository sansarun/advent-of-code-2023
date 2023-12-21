from collections import Counter

card_powers = {
    "A": "25",
    "K": "24",
    "Q": "23",
    "T": "21",
    "9": "20",
    "8": "19",
    "7": "18",
    "6": "17",
    "5": "16",
    "4": "15",
    "3": "14",
    "2": "13",
    "J": "12",
}

pattern_powers = {
    "5": 7,
    "4,1": 6,
    "3,2": 5,
    "3,1,1": 4,
    "2,2,1": 3,
    "2,1,1,1": 2,
    "1,1,1,1,1": 1,
}


def find_power(cards):
    original_cards = cards.copy()

    print(cards)

    # handle joker
    c = Counter([c for c in cards if c != "J"])
    if len(list(c.elements())) > 0:
        max_occurence = max(c.values())
        most_commons = [k for k, v in c.items() if v == max_occurence]
        most_common = most_commons.sort(key=lambda x: card_powers[x], reverse=True)
        most_common = most_commons[0]
        cards = [most_common if c == "J" else c for c in cards]
    else:
        cards = ["A" if c == "J" else c for c in cards]

    print(cards)
    print("===============")

    count = {}
    for card in cards:
        if card not in count:
            count[card] = 0
        count[card] += 1

    hand_pattern = ",".join([str(c) for c in sorted(count.values(), reverse=True)])
    pattern_power = pattern_powers[hand_pattern]
    card_power = "".join([card_powers[card] for card in original_cards])
    power = str(pattern_power) + card_power
    return int(power)


def process_hand(line):
    cards, bid = line.split(" ")
    cards = list(cards)
    return {"cards": cards, "bid": int(bid), "power": find_power(cards)}


with open("input/input.txt", "r") as f:
    lines = f.read().split("\n")
    hands = list(map(process_hand, lines))

    sorted_hands = sorted(hands, key=lambda hand: hand["power"])

    ranked_hands = []
    for index, hand in enumerate(sorted_hands):
        ranked_hands.append(
            {
                "rank": index + 1,
                "cards": hand["cards"],
                "bid": hand["bid"],
                "power": int(hand["power"]),
            }
        )

    # for r in ranked_hands:
    #     print(r)

    ans = sum([r["rank"] * r["bid"] for r in ranked_hands])
    print(ans)

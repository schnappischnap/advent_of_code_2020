from collections import deque


def part_1(data):
    decks = [deque(int(line) for line in player.splitlines()[1:])
             for player in data.split("\n\n")]

    while all(len(deck) > 0 for deck in decks):
        cards = [deck.popleft() for deck in decks]
        winner = cards.index(max(cards))
        decks[winner].extend(reversed(sorted(cards)))

    winning_deck = max(decks, key=lambda x: len(x))
    return sum(i * card for i, card in enumerate(reversed(winning_deck), start=1))


def part_2(data):
    def play_round(decks, level=0):
        seen = set()

        while all(len(deck) > 0 for deck in decks):
            decks_tuple = tuple(tuple(deck) for deck in decks)
            if decks_tuple in seen:
                return 0
            seen.add(decks_tuple)

            cards = [deck.popleft() for deck in decks]
            if all(len(deck) >= card for deck, card in zip(decks, cards)):
                new_decks = [deque(list(deck)[0:card])
                             for deck, card in zip(decks, cards)]
                winner = play_round(new_decks, level+1)
                decks[winner].extend(cards if winner == 0 else reversed(cards))
            else:
                winner = cards.index(max(cards))
                decks[winner].extend(reversed(sorted(cards)))

        if level > 0:
            return 0 if len(decks[0]) > 0 else 1
        else:
            winning_deck = max(decks, key=lambda x: len(x))
            return sum(i * card for i, card in enumerate(reversed(winning_deck), start=1))

    return play_round([deque(int(line) for line in player.splitlines()[1:])
                       for player in data.split("\n\n")])


if __name__ == '__main__':
    with open('day_22_input.txt', 'r') as f:
        inp = f.read()
        print("Part 1 answer: " + str(part_1(inp)))
        print("Part 2 answer: " + str(part_2(inp)))

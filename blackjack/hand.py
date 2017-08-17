from card import Card

class Hand(object):
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def show(self,hide_dealer=False):
        result = ""
        for card in self.cards:
            result += card.number + card.suit + " "
            if hide_dealer:
                break
        return result

    def calculate(self):
        # import pdb; pdb.set_trace()
        a = sum([card.value() for card in self.cards])
        if any([card.has_a() for card in self.cards]):
            a += 10
            return [a - 10] if a > 21 else [a, a - 10]
        return [a]

    def is_blackjack(self):
        return len(self.cards) == 2 and abs(self.cards[0].value() - self.cards[1].value()) == 9 and abs(self.cards[0].value() + self.cards[1].value()) == 11

    def is_bust(self):
        return any([True for i in self.calculate() if i > 21])

    def __cmp__(self, other):
        return cmp(max(self.calculate()), max(other.calculate()))

    def is_splittable(self):
        return len(self.cards) == 2 and self.cards[0].number == self.cards[1].number

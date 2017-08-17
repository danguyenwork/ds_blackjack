class Card(object):
    value_dict = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
                  '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10,
                  'K': 10, 'A': 1}

    def __init__(self, number, suit):
        self.suit = suit
        self.number = number

    def value(self):
        return Card.value_dict[self.number]

    def has_a(self):
        return self.number == 'A'

    def __repr__(self):
        return "%s%s" % (self.number, self.suit)

    def __cmp__(self, other):
        return cmp(self.value_dict[self.number], self.value_dict[other.number])

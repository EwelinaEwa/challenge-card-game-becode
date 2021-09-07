class Symbol:

    color = ["Hearts", "Diamonds", "Clubs", "Spades"]
    icon = ["♥", "♦", "♣", "♠"]

    def __init__(self, color, icon):
        self.color = color
        self.icon = icon

    def __str__(self):
        return self.icon


class Card (Symbol):

    value = ['A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K']

    def __init__(self, value, color, icon):
        super(Card, self).__init__(color, icon)
        self.value = value

    def __str__(self):
        return self.value + self.icon


new_card = Card('A', "Hearts", "♠")
print(new_card)


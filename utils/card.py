class Symbol:

    color = ["Hearts", "Diamonds", "Clubs", "Spades"]
    icon = ["♥", "♦", "♣", "♠"]

    def __init__(self, color, icon):
        self.color = color
        self.icon = icon

    def __str__(self):
        return self.icon


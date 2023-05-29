class Card(object):
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def getRank(self):
        return self.rank

    def cardPoints(self):
        # Rerturns amount points for some card
        if self.rank in ["10", "J", "Q", "K", "A"]:
            if self.rank == "A":
                # 11 points for ace
                return 11
            else:
                # 10 points for 10, jack, queen or king
                return 10
        else:
            # Amount points for any other card
            return ["6", "7", "8", "9"].index(self.rank) + 6

    def __str__(self):
        return "%s %s" % (self.rank, self.suit)
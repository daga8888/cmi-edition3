from random import shuffle
kolory = ['kier', 'trefl', 'karo', 'pik']
figury = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']


class Karta(object):

    def __init__(self, kolor, figura):
        self.kolor = kolor
        self.figura = figura

    def __str__(self):
        return f'{self.figura}-{self.kolor}'


def utworz_talie():
    return [Karta(kolor, figura) for figura in figury for kolor in kolory]


def tasuj(talia):
    return shuffle(talia)


class Dealer(object):

    def __init__(self, talia = None, shuffle = True):
        if talia is None:
            talia = utworz_talie()
        if shuffle:
            tasuj(talia)

        def create_generator(talia):
            while len(talia) > 0:
                yield talia.pop(0)

        self.generator = create_generator(talia)

    def nastepna(self):
        return next(self.generator)

    def split(self, no_players=2, cards='all'):
        result = [ [] for _ in range(no_players)]
        i = 0
        for card in self.generator:
            result[i % no_players].append(card)
            i += 1
            if cards != 'all' and i >= cards:
                break
        return result


d = Dealer()
gracz1, gracz2, gracz3, gracz4 = d.split(no_players=4)



from random import random, randrange, sample

class Choroba(object):

    def __init__(self):
        self.trwanie = 0

    def mija_dzien(self):
        self.trwanie += 1

    def czy_koniec(self):
        czas_trwania = 15
        return self.trwanie > czas_trwania

class Czlowiek(object):

    def __init__(self):
        self.zdrowie = 100
        self.odpornosc = 0
        self.choroba = None

    def czy_chory(self):
        return self.choroba is not None

    def kontakt(self, czlowiek):
        if self.choroba is not None and czlowiek.choroba is None:
            losowa = random() #[0,1]
            if int(losowa*100) > czlowiek.odpornosc:
                nowa_choroba = Choroba()
                czlowiek.choroba = nowa_choroba

    def mija_dzien(self):
        if self.choroba is not None and self.choroba.czy_koniec():
            self.odpornosc = 100
            self.choroba = None
        if self.choroba is None:
            self.zdrowie +=1
        else:
            self.zdrowie -=5
        if self.odpornosc > 0:
            self.odpornosc -= 1


class Swiat(object):

    # funkcja stworzenia swiata
    def __init__(self, liczba_ludzi = 0, liczba_chorych = 0, licza_spotkan_kazdego_czlowieka = (0,10)):
        self.rok=2020
        self.dzien=0
        self.populacja = []
        self.choroby = []
        self.liczba_spotkan_kazdego_czlowieka = licza_spotkan_kazdego_czlowieka
        for _ in range(liczba_chorych):
            nowy = Czlowiek()
            nowa_choroba = Choroba()
            nowy.choroba = nowa_choroba
            self.populacja.append(nowy)
            self.choroby.append(nowa_choroba)
        for _ in range(liczba_ludzi-liczba_chorych):
            nowy = Czlowiek()
            self.populacja.append(nowy)

    def wypisz_stan_pandemii(self):
        liczba_chorych = len([czlowiek for czlowiek in self.populacja if czlowiek.czy_chory()])
        liczba_ludzi = len(self.populacja)
        print(f'Populacja liczy {liczba_ludzi} osób z których chorych jest {liczba_chorych:5}', end=' ')
        print(f'Stanowi to {int(liczba_chorych/liczba_ludzi * 100):3}% populacji', end=' ')
        print(f'Przeciętna odporność wynosi {sum([int(czlowiek.odpornosc) for czlowiek in self.populacja])/len(self.populacja):3}%')

    def mija_dzien(self):
        # co sie dzieje codziennie na swiecie
        print(f'Mamy dzień {self.dzien:3} roku {self.rok}', end=' ')
        ## kontakty miedzy ludzkie
        min, maks = self.liczba_spotkan_kazdego_czlowieka
        for czlowiek in self.populacja:
            ile_spotkan = randrange(min, maks)
            for drugi_czlowiek in sample(self.populacja, ile_spotkan):
                czlowiek.kontakt(drugi_czlowiek)
                drugi_czlowiek.kontakt(czlowiek)
        ##
        for czlowiek in self.populacja:
            czlowiek.mija_dzien()
        self.choroby = [ czlowiek.choroba for czlowiek in self.populacja if czlowiek.czy_chory()]
        for choroba in self.choroby:
            choroba.mija_dzien()
        self.wypisz_stan_pandemii()
        self.dzien +=1
        if self.dzien %365 == 0:
            self.rok += 1
            self.dzien = 0


    def uruchom_przez(self, liczba_dni):
        for _ in range(liczba_dni):
            self.mija_dzien()

swiat = Swiat(liczba_ludzi=10000, liczba_chorych=1, licza_spotkan_kazdego_czlowieka=(0,4))
swiat.uruchom_przez(365)
from random import random, sample, randrange

class Swiat(object):
    
    def __init__(self, liczba_ludzi = 0, liczba_chorych = 0, liczba_spotkan = 2):
        self.rok = 2020
        self.dzien = 0
        self.liczba_spotkan = liczba_spotkan
        self.populacji = []
        for _ in range(liczba_chorych):
            nowy_czlowiek = Czlowiek()
            nowa_choroba = Choroba() #tworzymy chorobe
            nowy_czlowiek.choroba = nowa_choroba #przypisujemy chorobe do czlowieka
            self.populacji.append(nowy_czlowiek) #dolacz go do populacji swiata
        for _ in range(liczba_ludzi - liczba_chorych):
            nowy_czlowiek = Czlowiek() #stworz nowego czlowieka
            self.populacji.append(nowy_czlowiek) #dolacz go do populacji swiata
    
    def mija_dzien(self):
        self.dzien += 1
        if self.dzien % 365 == 0:
            self.rok += 1
            self.dzien = 0
        
        for czlowiek in self.populacji:
            #losujemy ludzi z ktorymi sie on tego dnia spotka
            for spotkanego_czlowieka in sample(self.populacji, self.liczba_spotkan):
                czlowiek.kontakt(spotkanego_czlowieka)
                spotkanego_czlowieka.kontakt(czlowiek)
        
        print(f'\nMamy dzien {self.dzien:3} roku {self.rok}', end=' ')
        choroby = []
        
        zywi = []
        for czlowiek in self.populacji:
            if czlowiek.czy_zywy():
                zywi.append(czlowiek)
        self.populacji = zywi         
        
        for czlowiek in self.populacji:
            czlowiek.mija_dzien()
            if czlowiek.choroba is not None:
                choroby.append(czlowiek.choroba)
        for choroba in choroby:
            choroba.mija_dzien()
        self.wypisz_stan_pandemii()
            
    
    def wypisz_stan_pandemii(self):
        liczba_ludzi = len(self.populacji)
        chory = []
        for czlowiek in self.populacji:
            if czlowiek.czy_chory():
                chory.append(czlowiek)
        liczba_chorych = len(chory)
        
        print(f'Populacja liczy {liczba_ludzi:5} osób z których chorych jest {liczba_chorych:5}', end = ' ')
        print(f'Stanowi to {int(liczba_chorych/liczba_ludzi * 100):3}% całej populacji', end =' ')
        
    def uruchom_przez(self, dni):
        for _ in range(dni):
            self.mija_dzien()
            
class Czlowiek(object):
    
    def __init__(self):
        self.zdrowie = 100
        self.odpornosc = 0
        self.choroba = None
    
    def mija_dzien(self):
        
        if self.choroba is not None and self.choroba.czy_koniec(): # chorowal, ale choroba juz mija
            self.choroba = None #wyzdrowial
            self.odpornosc = 100
            
        if self.choroba is None and self.zdrowie < 100:
            self.zdrowie += 2
        elif self.choroba is not None:
            self.zdrowie -= self.choroba.szkodliwosc
        
        if self.odpornosc > 0:
            self.odpornosc -= 1

    def czy_chory(self):
        return self.choroba is not None
    
    def czy_zywy(self):
        return self.zdrowie > 0
    
    def kontakt(self, inny_czlowiek):
        if self.choroba is not None and inny_czlowiek.choroba is None:
            losowa = random() #(0,1)
            if int(losowa * 100) > inny_czlowiek.odpornosc:
                nowa_choroba = Choroba() # tworzona jest kolejna choroba
                inny_czlowiek.choroba = nowa_choroba
            

class Choroba(object):
    
    def __init__(self):
        self.trwania = 0
        self.szkodliwosc = randrange(5,12) # wylosowac z przedzialu [5,12]
    
    def mija_dzien(self):
        self.trwania += 1
        
    def czy_koniec(self):
        czas_trwania = 15
        return self.trwania > czas_trwania
  
swiat = Swiat(liczba_ludzi = 10000, liczba_chorych = 1, liczba_spotkan = 5)
swiat.uruchom_przez(180)          

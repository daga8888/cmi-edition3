
## Napisac program, ktory dla podanej daty (w formacie , dzien, miesiac, rok) poda nam date dnia nastepnego

## Zastanowmy sie jakie sa ogolne kroki jakie musimy wykonac

def czy_to_koniec_roku(dzien, miesiac):
    if miesiac == 12 and dzien == 31:
        return True
    else:
        return False

def czy_rok_przestepny(rok):
    # Możliwości
    # Rok taki jak 1600, 2000 (podzielny przez 400) - tak przestepny
    # Rok 1700 (podzielny przez 4, przez 100, ale nie przez 400) - nie jest przestepny
    # Rok taki jak 2004 - jest przestepny jako podzielny przez 4
    # Rok taki jak 2021 - nie jest przestepny
    if rok % 400 == 0:
        return True
    elif rok %400 != 0 and rok %100 == 0:
        return False
    elif rok %100 != 0 and rok % 4 == 0:
        return True
    else :
        return False

def czy_to_koniec_miesiaca(dzien, miesiac, rok):
    # Jakie przypadki
    # miesiace 31 dniowe - styczen
    # miesiace 30 dniowe - kwiecien
    # luty :-/ 28, 29 dni
    if miesiac==2 and dzien == 29 and czy_rok_przestepny(rok):
        return True
    elif miesiac==2 and dzien == 28 and not czy_rok_przestepny(rok):
        return True
    elif miesiac in [4,6,9,11] and dzien == 30:
        return True
    elif miesiac in [1,3,5,7,8,10,12] and dzien == 31:
        return True
    else:
        return False

def dzien_nastepny(dzien, miesiac, rok):
    # Mozliwe jest kilka przypadkow
    # 16-10-2021 -> 17-10-2021 -> normalnego dnia !
    # koniec miesiaca
    # koniec roku <- rygorystyczny przypadek
    if czy_to_koniec_roku(dzien, miesiac):
        return 1,1,rok+1
    elif czy_to_koniec_miesiaca(dzien, miesiac, rok):
        return 1, miesiac+1, rok
    else :
        return dzien + 1, miesiac, rok

## Donata
# 15:27
# dzisiaj
# Odpisz na wiadomość
# Przypnij wiadomość na górze
# Kopiuj
# Jacek
# 15:27
# 3.7.1975
# Odpisz na wiadomość
# Przypnij wiadomość na górze
# Kopiuj
# Mirek
# 15:27
#24 czerwca 2022

print(dzien_nastepny(31,12,2021))

def data_za_dni(dzien, miesiac, rok, ile_dni):
    for _ in range(ile_dni):
        dzien, miesiac, rok = dzien_nastepny(dzien, miesiac, rok)
    return dzien, miesiac, rok

print(data_za_dni(31,12,2021, 700))
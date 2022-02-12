K = 132

nominaly = [1, 2, 5, 10, 20, 50]

def change_making_dynamic(K, nominaly, maks_size = 1000000):
    change_making = {}
    for i in range(1,K+1):
        change_making[i] = [] #najpierw nie znamy przepisu na zadna z liczb
    for i in range(1,K+1):
        if i in nominaly: #jesli nasza liczba jest wsrod dostepnych nominalow - to najprosciej wydac ja na raz
            change_making[i].append(i)
            continue # nie ma bardziej optymalnego sposobu
        # inaczej rozwazamy wszystkie pary i wyszukujemy najmniejszego zestawu reszt
        min_size = maks_size
        min_ind = 1
        for j in range(1,i):
            # len(change_making[j]) + len(change_making[i-j]) to ilosc monet w reszcie przy probie podzialu
            # i na j + (i-j)
            if min_size > len(change_making[j]) + len(change_making[i-j]):
                min_size = len(change_making[j]) + len(change_making[i-j])
                min_ind = j
        # przypisanie najoptymalniejszego podziału (dowolnego tj pierwszego) do tablicy wyników
        change_making[i] = change_making[min_ind].copy()
        change_making[i].extend(change_making[i-min_ind])
    return change_making

print(change_making_dynamic(K, nominaly))
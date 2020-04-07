def tri_rapide(tableau):
    if not tableau:
        return []
    else:
        pivot = tableau[-1]
        plus_petit = [x for x in tableau     if x <  pivot]
        plus_grand = [x for x in tableau[:-1] if x >= pivot]
        return tri_rapide(plus_petit) + [pivot] + tri_rapide(plus_grand)


tab=[13,11,12,1,71,15]
print(tab)

plus_petit = [x for x in tab     if x <  tab[-1]]
plus_grand = [x for x in tab[:-1] if x >= tab[-1]]
print(plus_petit)
print(plus_grand)

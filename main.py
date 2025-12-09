# 7
sonlar = [-5, 3, -8, 0, 12, -1, 7, 9]
musbat_tuple = tuple(x for x in sonlar if x > 0)
print(musbat_tuple)


#8
kvadrat_juftliklar = tuple((i, i**2) for i in range(1, 16))
print(kvadrat_juftliklar)


# 9
matn = "tuple misollari"
oxirgi_harflar = tuple(soz[-1] for soz in matn.split())
print(oxirgi_harflar)

# 10
toq_indeks_kvadrat = tuple(x**2 for i, x in enumerate(range(1, 21)) if i % 2 == 1)
print(toq_indeks_kvadrat)


# 11
sozlar = ["anor", "banan", "olma", "shaftoli", "uzum", "qovun", "apelsin", "behi"]
unlilar = "aeiouAEIOU"
unli_boshlanuvchilar = tuple(soz for soz in sozlar if soz and soz[0] in unlilar)
print(unli_boshlanuvchilar)


# 12
def palindrom(son):
    return str(son) == str(son)[::-1]

palindromlar = tuple(x for x in range(1, 51) if palindrom(x))
print(palindromlar)  

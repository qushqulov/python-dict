mahsulotlar = {
    "olma": 12000,
    "banan": 25000,
    "uzum": 18000,
    "anor": 20000
}

kalit = input("Mahsulot nomini kiriting: ").lower()

if kalit in mahsulotlar:
    print(f"{kalit.capitalize()}ning narxi: {mahsulotlar[kalit]} so'm")
else:
    print()
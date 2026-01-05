person = {
    "name": "Ali",
    "age": 25,
    "city": "Tashkent"
}

key = input("O‘chiriladigan kalit nomini kiriting: ")

if key in person:
    del person[key]
    print("Kalit o‘chirildi")
else:
    print("Bunday kalit yo‘q")

print(person)

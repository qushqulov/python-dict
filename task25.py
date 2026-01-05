def group_by_age(people):
    result = {}

    for person in people:
        age = person["age"]
        name = person["name"]

        if age not in result:
            result[age] = []

        result[age].append(name)

    return result

people = [
    {"name": "Ali", "age": 20},
    {"name": "Vali", "age": 21},
    {"name": "Sami", "age": 20},
    {"name": "Karim", "age": 21}
]

natija = group_by_age(people)
print(natija)

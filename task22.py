def group_students(students):
    result = {}

    for student in students:
        group = student["group"]
        name = student["name"]

        if group not in result:
            result[group] = []

        result[group].append(name)

    return result

students = [
    {"name": "Ali", "group": "A"},
    {"name": "Soli", "group": "A"},
    {"name": "Vali", "group": "B"},
    {"name": "Karim", "group": "B"}
]

result = group_students(students)
print(result)
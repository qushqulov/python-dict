def group_by_age(people):
    result = {}
    for p in people:
        age = p["age"]
        result.setdefault(age, []).append(p["name"])
    return result

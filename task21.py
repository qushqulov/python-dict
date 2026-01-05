def count_names(names):
    result = {}

    for name in names:
        if name not in result:
            result[name] = 1
        else:
            result[name] += 1

    return result

names = ["Ali", "Vali", "Ali", "Sami", "Ali", "Vali"]
result = count_names(names)
print(result)

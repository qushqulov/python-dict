def merge_dicts(a, b):
    result = a.copy()
    result.update(b)
    return result


dict1 = {"a": 1, "b": 2}
dict2 = {"b": 99, "c": 3}

merged = merge_dicts(dict1, dict2)
print(merged)

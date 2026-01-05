def filter_non_zero(d):
    result = {}
    for k, v in d.items():
        if v != 0:
            result[k] = v
    return result

data = {
    "a": 0,
    "b": 3,
    "c": 0,
    "d": 5
}

filtered = filter_non_zero(data)
print(filtered)

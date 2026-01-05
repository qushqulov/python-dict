def group_indices(numbers):
    result = {}

    for i, num in enumerate(numbers):
        if num not in result:
            result[num] = []
        result[num].append(i)

    return result


numbers = [1, 2, 1, 3, 2, 1]
result = group_indices(numbers)
print(result)

def group_by_length(words):
    result = {}

    for word in words:
        length = len(word)

        if length not in result:
            result[length] = []

        result[length].append(word)

    return result

words = ["olma", "anor", "banan", "uzum", "shaftoli"]

result = group_by_length(words)
print(result)

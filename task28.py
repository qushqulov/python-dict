def group_by_length(words):
    result = {}
    for word in words:
        l = len(word)
        result.setdefault(l, []).append(word)
    return result

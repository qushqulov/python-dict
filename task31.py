def count_letters(text):
    result = {}
    for ch in text:
        if ch != " ":
            result[ch] = result.get(ch, 0) + 1
    return result

text = "assalomu alaykum"
counts = count_letters(text)
print(counts)

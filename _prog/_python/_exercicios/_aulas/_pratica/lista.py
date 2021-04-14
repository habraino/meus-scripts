def is_abecedarian(word):
    i = 0
    while i < len(word) - 1:
        if word[i+1] < word[i]:
            return False
        i += 1
    return True

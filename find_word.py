def find_word(sentence, word):
    sentence = (f' {sentence} ')
    result = []
    lenght = len(word)
    min_lenght = 0
    for i, _ in enumerate(sentence):
        if sentence[min_lenght:lenght] == word:
            if sentence[min_lenght-1] == ' ':
                if sentence[lenght] == ' ':
                    result.append(i-1)
        min_lenght += 1  
        lenght += 1
    return result


s = 'find a word in some sentence'
w = 'in'
print(find_word(s, w))

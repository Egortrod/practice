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



def find_word2(sentencee, wordd):
    return([pos for pos, char in enumerate(sentencee) if char == wordd])


s = str(input('Input sentence: '))  
w = str(input('Input finding thing: '))
print(find_word(s, w))
print(find_word2(s, w))
data = {
    'б': 'н', 'в': 'б', 'г': 'ф', 'д': 'з', 'е': 'ы',
    'ё': 'о', 'ж': 'в', 'з': 'х', 'и': 'и', 'й': 'ь',
    'к': 'п', 'л': 'г', 'м': 'ц', 'н': 'й', 'о': 'э',
    'п': 'р', 'р': 'д', 'с': 'ч', 'т': 'к', 'у': 'ю',
    'ф': 'с', 'х': 'е', 'ц': 'ш', 'ч': 'л', 'ш': 'я',
    'щ': 'т', 'ы': 'щ', 'ь': 'м', 'э': 'а', 'ю': 'у', 'я': 'ж'
}

def find_and_replace(letter):
    for k, v in data.items():
        if letter == k:
            output = v
    return output


def decoding(text):
    out = ''
    for letter in text:
        if letter in data.keys():
            out += find_and_replace(letter)
        else:
            out += letter
    return out

with open('data.txt', 'r') as f:
    to_decoding = f.read()
print(decoding(to_decoding)) 




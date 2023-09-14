def capitalize(word):
    first_letter_small = word[0]
    first_letter_big = chr(ord(first_letter_small) - ord('a') + ord('A'))
    return first_letter_big + word[1:]

source = input().split()
res = []
for word in source:
    res.append(capitalize(word))
print(' '.join(res))

def capitalize_full(word):

    """ Функция делает заглавными все буквы каждого слова в строке, поступившей на вход. """

    letter_big = word.upper()
    return letter_big

source = input().split()
res = []
for word in source:
    res.append(capitalize_full(word))
print(' '.join(res))
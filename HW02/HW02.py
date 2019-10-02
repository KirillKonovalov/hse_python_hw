word = input('Введите слово: ')
words = []
while word:
    words.append(word)
    word = input('Введите слово: ')
    continue
print('Введенные слова, длина которых больше 5 символов:')
for word in words:
    if len(word) > 5:
        print(word)

from textblob import TextBlob
text = TextBlob(input())
wrd = text.words
count = 0
for i in range(len(text)):
    if text[i] in 'АЕЁИОУЫЭЮЯаеёиоуыэюя' or text[i] in 'aeiouyAEIOUY':
        count+=1
print('Предложений:', len(text.sentences))
print('Слов:', len(wrd))
print('Слогов:', count)
print('Средняя длина предложения в словах:', len(wrd)/len(text.sentences))
print('Средняя длина слова в слогах:', count/len(wrd))


"""9999999"""

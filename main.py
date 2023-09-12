import ru_local as ru
from textblob import TextBlob
text = TextBlob(input())
wrd = text.words
count = 0
for i in range(len(text)):
    if text[i] in 'АЕЁИОУЫЭЮЯаеёиоуыэюя' or text[i] in 'aeiouyAEIOUY':
        count+=1

avearge_word_lenght = len(wrd)/len(text.sentences)
avearge_syllable_lenght = count/len(wrd)
print('Предложений:', len(text.sentences))
print('Слов:', len(wrd))
print('Слогов:', count)
print('Средняя длина предложения в словах:', avearge_word_lenght)
print('Средняя длина слова в слогах:', avearge_syllable_lenght)

if text[1].upper() in "ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ":
    flash_index = 206.835 - 1.3*avearge_word_lenght - 60.1*avearge_syllable_lenght
else:
    flash_index = 206.835 - 1.015 * avearge_word_lenght - 84.6 * avearge_syllable_lenght

print("Индекс удобочитаемости Флеша: ", flash_index)
if 90< flash_index <=100:
    print()
elif 80< flash_index <=90:
    print()
elif 70< flash_index <=80:
    print()
elif 60< flash_index <=70:
    print()
elif 50< flash_index <=60:
    print()
elif 30< flash_index <=50:
    print()
elif flash_index <=30:
    print()

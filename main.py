import ru_local as ru
from textblob import TextBlob
from deep_translator import GoogleTranslator

text = TextBlob(input())
wrd = text.words
cnt = 0

for i in range(len(text)):
    if text[i] in 'АЕЁИОУЫЭЮЯаеёиоуыэюя' or text[i] in 'aeiouyAEIOUY':
        cnt+=1

avearge_word_lenght = len(wrd)/len(text.sentences)
avearge_syllable_lenght = cnt/len(wrd)
print(ru.SENTENCE, len(text.sentences))
print(ru.WORD, len(wrd))
print(ru.SYLLABLE, cnt)
print(ru.AVEARGE_WORD_LENGHT, avearge_word_lenght)
print(ru.AVEARGE_SYLLABLE_LENGHT, avearge_syllable_lenght)

flash_index = 0
if text[1].upper() in 'ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ':
    flash_index = 206.835 - 1.3*avearge_word_lenght - 60.1*avearge_syllable_lenght
else:
    flash_index = 206.835 - 1.015 * avearge_word_lenght - 84.6 * avearge_syllable_lenght

print(ru.FLASH_INDEX , flash_index)
if 80 < flash_index <= 100:
    print(ru.FLASH_INDEX_RESULT_1)
elif 50 < flash_index <= 80:
    print(ru.FLASH_INDEX_RESULT_2)
elif 25 < flash_index <= 50:
    print(ru.FLASH_INDEX_RESULT_3)
elif flash_index <= 25:
    print(ru.FLASH_INDEX_RESULT_4)



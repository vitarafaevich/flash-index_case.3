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
print(ru.SENTENCE, len(text.sentences))
print(ru.WORD, len(wrd))
print(ru.SYLLABLE, count)
print(ru.AVEARGE_WORD_LENGHT, avearge_word_lenght)
print(ru.AVEARGE_SYLLABLE_LENGHT, avearge_syllable_lenght)

flash_index = 0
if text[1].upper() in 'ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ':
    flash_index = 206.835 - 1.3*avearge_word_lenght - 60.1*avearge_syllable_lenght
else:
    flash_index = 206.835 - 1.015 * avearge_word_lenght - 84.6 * avearge_syllable_lenght

print(ru.FLASH_INDEX,flash_index)
if 90< flash_index <=100:
    print(ru.FLASH_INDEX_RESULT_1)
elif 80< flash_index <=90:
    print(ru.FLASH_INDEX_RESULT_2)
elif 70< flash_index <=80:
    print(ru.FLASH_INDEX_RESULT_3)
elif 60< flash_index <=70:
    print(ru.FLASH_INDEX_RESULT_4)
elif 50< flash_index <=60:
    print(ru.FLASH_INDEX_RESULT_5)
elif 30< flash_index <=50:
    print(ru.FLASH_INDEX_RESULT_6)
elif flash_index <=30:
    print(ru.FLASH_INDEX_RESULT_7)

'''
Котлярова Полина 93
Рафаевич Вита 93
Якимова Антонина 93
'''

import ru_local as ru
from textblob import TextBlob
from deep_translator import GoogleTranslator

def translate(text):
    translated = GoogleTranslator(source='auto', target='en').translate(text)
    return translated

text = input()
text_translate = text

text = TextBlob(text)
word = text.words
cnt = 0
for i in range(len(text)):
    if text[i] in 'АЕЁИОУЫЭЮЯаеёиоуыэюя' or text[i] in 'aeiouyAEIOUY':
        cnt+=1

avearge_word_lenght = len(word)/len(text.sentences)
avearge_syllable_lenght = cnt/len(word)
print(ru.SENTENCE, len(text.sentences))
print(ru.WORD, len(word))
print(ru.SYLLABLE, cnt)
print(ru.AVEARGE_WORD_LENGHT, avearge_word_lenght)
print(ru.AVEARGE_SYLLABLE_LENGHT, avearge_syllable_lenght)

flash_index = 0
if text[0].upper() in 'ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ':
    text_translate= translate(text_translate)
    flash_index = 206.835 - 1.3*avearge_word_lenght - 60.1*avearge_syllable_lenght
else:
    flash_index = 206.835 - 1.015 * avearge_word_lenght - 84.6 * avearge_syllable_lenght

text = TextBlob(text_translate)

print(ru.FLASH_INDEX , flash_index)
if 80 < flash_index <= 100:
    print(ru.FLASH_INDEX_RESULT_1)
elif 50 < flash_index <= 80:
    print(ru.FLASH_INDEX_RESULT_2)
elif 25 < flash_index <= 50:
    print(ru.FLASH_INDEX_RESULT_3)
elif flash_index <= 25:
    print(ru.FLASH_INDEX_RESULT_4)

text_polarity = text.sentiment.polarity
if -0.5 <= text_polarity <= 0.5:
    print(ru.TEXT_POLARITY_NEUTRAL)
elif text_polarity < -0.5:
    print(ru.TEXT_POLARITY_NEGATIV)
elif text_polarity > 0.5:
    print(ru.TEXT_POLARITY_POSITIVE)

print(f'{ru.OBJECTIVITY}: {text.sentiment.subjectivity*100}%')



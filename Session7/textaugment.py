import random
import googletrans
from  googletrans import Translator

# Back translate a sentence back to english
def back_translate(sentence):

    translator = Translator()
    sentence = [sentence]
    available_langs = list(googletrans.LANGUAGES.keys())
    trans_lang = random.choice(available_langs)
    # print(f"Translating to {googletrans.LANGUAGES[trans_lang]}")

    translations = translator.translate(sentence, dest=trans_lang)
    t_text = [t.text for t in translations]
    # print(t_text)

    translations_en_random = translator.translate(t_text, src=trans_lang, dest='en')
    # en_text = [t.text for t in translations_en_random]
    en_text = translations_en_random[0].text
    return en_text, googletrans.LANGUAGES[trans_lang]


#randomly deletes words from a sentence
def random_deletion(sentence, p=0.2):
    words = str(sentence).split()
    if len(words) == 1: # return if single word
        return words
    remaining = list(filter(lambda x: random.uniform(0,1) > p,words))
    if len(remaining) == 0: # if not left, sample a random word
        return ' '.join([random.choice(words)])
    else:
        return ' '.join(remaining)

#Randomly swap words in a sentence
def random_swap(sentence, n=3):
    words = str(sentence).split()
    length = range(len(words))
    if len(words) > n+2:
        for _ in range(n):
            idx1, idx2 = random.sample(length, 2)
            words[idx1], words[idx2] = words[idx2], words[idx1]
    return ' '.join(words)

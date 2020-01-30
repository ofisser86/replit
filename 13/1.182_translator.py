from googletrans import Translator
from translate import Translator as offline_translate

translator = Translator()

try:
    with open('text_for_translator.tx', 'r') as f:
        print(translator.translate(f.readline(), dest='zh-TW').text)
except FileNotFoundError as er:
    print('first try -> file does not exist in this funny library')
    # continue or not
    #raise Exception('Stop doing this')

try:
    with open('text_for_translator.txt', 'r') as f:
        offline = offline_translate(to_lang="zh")
        print(offline.translate(f.readline()))
except FileNotFoundError as er:
    print('Second try -> file does not exist in this funny library', er)

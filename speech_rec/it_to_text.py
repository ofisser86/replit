import speech_recognition as speech_recog
from googletrans import Translator



sample_audio = speech_recog.AudioFile("C:/Users/Мама/Documents/GitHub/replit/speech_rec/OSR_us_000_0018_8k.wav")
recog = speech_recog.Recognizer()
with sample_audio as audio_file:
    audio_content = recog.record(audio_file)

print(type(audio_content))
text = recog.recognize_google(audio_content)

with open('it.txt', 'w') as f:
    f.writelines(text)

translator = Translator()

try:
    with open('it.txt', 'r') as f:
        print(translator.translate(f.readline(), dest='ru').text)
except FileNotFoundError as er:
    print('first try -> file does not exist in this funny library')


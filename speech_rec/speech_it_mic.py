import speech_recognition as speech_recog

mic = speech_recog.Microphone()

recog = speech_recog.Recognizer()
with mic as audio_file:
    print("Speak Please")

    recog.adjust_for_ambient_noise(audio_file)
    audio = recog.listen(audio_file)

    print("Converting Speech to Text...")
    try:
        print("You said: " + recog.recognize_google(audio))
    except speech_recog.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except speech_recog.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

#print(speech_recog.Microphone.list_microphone_names())
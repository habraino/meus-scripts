import speech_recognition as sr

def _listen():
    micro = sr.Recognizer()

    with sr.Microphone() as source:
        micro.adjust_for_ambient_noise(source)
        print('diga alguma coisa: ')

        audio = micro.listen(source)

    try:
        frase = micro.recognize_google(audio, language='pt-PT')
        print('você disse:', frase)
    except sr.UnknownValueError:
        print('Não entendi')

    return frase


_listen()




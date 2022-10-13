#https://www.youtube.com/watch?v=XF2WVUVxAGQ&ab_channel=DimPy
import json, pyaudio 
from vosk import Model, KaldiRecognizer
import pyttsx3
engine = pyttsx3.init()


model = Model('vosk-model-small-ru-0.4')
rec = KaldiRecognizer(model, 16000)
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True,frames_per_buffer=8000)
stream.start_stream()

engine.say("я робот кот, готов спать и есть")
engine.runAndWait()

def listen():
    while True:
        data = stream.read(4000, exception_on_overflow=False)
        if (rec.AcceptWaveform(data)) and (len(data) > 0):
            answer = json.loads(rec.Result())
            if answer['text']:
                yield answer['text']
print()
for text in listen():
    print(text)
    if text == 'кушать':
        print("мяу!")
        engine.say("Мяу!")
        engine.runAndWait()
    elif text == 'мурзик ко мне':
        print("мр-мр-мр")
        engine.say("мыр-мыр-мыр")
        engine.runAndWait()
    else:
        print('я тебя не понимаю')

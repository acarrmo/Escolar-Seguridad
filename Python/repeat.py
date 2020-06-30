import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
#import os

def speak(audioString):
    print(audioString)
    tts = gTTS(text=audioString, lang='fr')
    tts.save("audio.mp3")
    #os.system("playsound audio.mp3")
    playsound("audio.mp3")

if __name__ == "__main__":
    #print(os.environ['PATH'])
    #os.environ['PATH'] += ":"+"/usr/local/bin"
    #print(os.environ['PATH'])
    #print(os.getcwd())
            
    #text to speech    
    #speak('Angelica')
    
    r = sr.Recognizer()
    mic = sr.Microphone()

    print("speak:")
    with mic as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    repeat = r.recognize_google(audio, language="fr-FR")
       
    speak(repeat)
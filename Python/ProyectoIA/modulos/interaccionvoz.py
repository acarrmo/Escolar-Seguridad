import speech_recognition as sr
from gtts import gTTS
import os
import platform

class interaccionvoz:
    arr_preguntas_base = [
        "¿Usualmente usas computadora?",
        "¿Manejas terminología médica?",
        "¿Tienes pacientes?",
        "¿Puedes diagnosticar enfermedades a pacientes humanos?"
    ]

    arr_respuestas_base = []

    ruta = "misc/voz.mp3"
    audio = 'cmdmp3' if platform.system() == 'Windows' else 'mpg321' 
    def __init__(self):
        print("Interacción con voz")

    def escuchar_voz(self): 
        bandera=True 
        texto = "---" 
 
        while(bandera): 
            r = sr.Recognizer() 
            r.dynamic_energy_threshold = True 
            mic = sr.Microphone() 
            try: 
                with mic as source: 
                    r.adjust_for_ambient_noise(source) 
                    audio = r.listen(source, timeout=None, phrase_time_limit=3) 
                texto = r.recognize_google(audio, language="es-MX") 
                bandera = False 
            except sr.UnknownValueError: 
                texto = '---' 
            except sr.RequestError as e: 
                texto = '---'   
        return texto
    
    def reproducir_voz(self,texto): 
        print(texto) 
        tts = gTTS(text=texto, lang='es') 
        tts.save(self.ruta) 
        os.system(self.audio+" "+self.ruta)
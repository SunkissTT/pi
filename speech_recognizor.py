import speech_recognition as sr
import sounddevice
from tts import MyTTS
import time

# Initialize recognizer
rec = sr.Recognizer()
rec.energy_threshold = 400
 
# Function to capture audio and recognize speech
def Recognize_speech():
    # Use the microphone as source for input (specify the microphone index)
    with sr.Microphone() as source:
        # Adjusting for ambient noise
        rec.adjust_for_ambient_noise(source, duration=1)
        
        print("질문을 하거나, 번역이 필요하면 \'번역\', 종료하고싶으면 \'종료\'라고 말하세요")
        audio = rec.listen(source, timeout=5, phrase_time_limit=5)

        try:
            # Recognize speech using Google Web Speech API
            text = rec.recognize_google(audio, language="ko-KR")
            print("You said: " + text)
            return text
            
        except sr.UnknownValueError:
            print("음성 인식 실패")
        
        except sr.RequestError as e:
            print(f"HTTP Request Error 발생 : {e}")
        
        except sr.WaitTimeoutError:
            print("WaitTimeout Error 발생")

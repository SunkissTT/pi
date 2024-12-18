from speech_recognizor import Recognize_speech
from translator import Translate_text
from tts import MyTTS
import wake_word
from qa import Qa
import sys


'''
while(1):
    #print("시동어 : 하이 파이")
    #wake_word.main()
    #text = input('번역할 한국어 문장을 입력하세요 : ')
    text = Recognize_speech()
    if text == "종료":
        break
    elif text == "번역":
        text = Recognize_speech()
        translated_text = Translate_text(text)
        MyTTS(translated_text)
    else:
        translated_text = Translate_text(text)
        print('your question is : '+translated_text)
        answer = Qa(translated_text)
        print(answer)
        MyTTS(answer)
        
'''

user_input = sys.argv[1] if len(sys.argv) > 1 else ""

translated_text = Translate_text(user_input)
print("You said&nbsp;&nbsp;&nbsp;: "+user_input)
print("<br>Translated : "+translated_text)
#MyTTS(translated_text)

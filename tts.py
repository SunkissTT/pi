from gtts import gTTS
import os
from io import BytesIO
from pygame import mixer

def MyTTS(text):
  mixer.init()
  mp3audio = BytesIO()
  
  tts = gTTS(text, lang='en', tld = 'us')
  
  tts.write_to_fp(mp3audio)
  
  mp3audio.seek(0)
  mixer.music.load(mp3audio, "mp3")
  mixer.music.play()
  
  while mixer.music.get_busy():
    pass

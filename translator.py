from googletrans import Translator
import os

translator = Translator()

def Translate_text(text, retries=3):
    for attempt in range(retries):
        try:
            result = translator.translate(text, dest='en')
            return result.text
        except ReadTimeout:
            print(f"시도 {attempt + 1}/{retries}이 시간 초과되었습니다. 다시 시도 중...")
            continue
        except Exception as e:
            print(f"오류가 발생했습니다. 다시 시도해주세요.")
            break
    return None

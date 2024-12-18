import os

import pvporcupine
from pvrecorder import PvRecorder
from tts import MyTTS

def main():
    ## Wake word Setting
    porcupine = pvporcupine.create(
        access_key = 'gf6ZxnSXPHI1bVNevP2tT2cm0+KXJukMzsc6DhIsg7PpYU9EMNdFzg==',
        keyword_paths=[os.getcwd()+"/하이-파이_ko_raspberry-pi_v3_0_0.ppn"],
        model_path=os.getcwd()+"/porcupine_params_ko.pv",
    )
    
    ## Mic Setting
    ### devices = PvRecorder.get_available_devices()
    recorder = PvRecorder(frame_length=512, device_index=1)
    recorder.start()
    #print("[준비 완료] 마이크 입력이 준비되었습니다.")
    	
    # 계속해서 마이크 인식을 진행함
    while True:
        pcm = recorder.read()
        keyword_index = porcupine.process(pcm) # 키워드 인식
        if keyword_index == 0:
            # 키워드 감지 시, 반응하는 구간
            print('하이 파이 감지')
            break

if __name__=="__main__":
	main()

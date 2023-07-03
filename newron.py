from cvzone.HandTrackingModule import HandDetector
import cv2
from torchvision.models.detection import retinanet_resnet50_fpn
import matplotlib.pyplot as plt
import eye
import vosk
import pyaudio
import speech_recognition as sr
import trueeye
import threading

###初期設定

# recognizerインスタンスを作成
r = sr.Recognizer()

#ライブラリ
#耳
# モデルの読み込み
# モデルの読み込み
model = vosk.Model("model")

# マイクからの音声入力の設定
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=2000)
stream.start_stream()

# 画像処理の初期設定
cap = cv2.VideoCapture(0)
cap.set(3, 2256)
cap.set(4, 1504)
success, img = cap.read()
h, w, _ = img.shape

#関数
def capturing():
    while True:
        success, img = cap.read()
        return img

#ループする処理
face_thread = threading.Thread(target=eye.face, args=(capturing,))
hand_thread = threading.Thread(target=eye.hand, args=(capturing,))
eye_thread=threading.Thread(target=trueeye.listen)
mycapturing=threading.Thread(target=capturing)

###本番

try:
    face_thread.start()
    hand_thread.start()
    eye_thread.start()
    mycapturing.start()

except Exception as e:
    pass

face_thread.join()
hand_thread.join()
eye_thread.join()
mycapturing.join()

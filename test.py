import cv2
import threading
import eye
import trueeye

# 画像処理の初期設定
cap = cv2.VideoCapture(0)
cap.set(3, 2256)
cap.set(4, 1504)
success, img = cap.read()
h, w, _ = img.shape

# 初期処理
eyedata = eye.face(img)
senddata = []

def face_thread():
    global eyedata
    while True:
        success, img = cap.read()
        eyedata = eye.face(img)

def hand_thread():
    while True:
        success, img = cap.read()
        eye.hand(img)

# マルチスレッドで処理を実行
face_thread = threading.Thread(target=face_thread)
hand_thread = threading.Thread(target=hand_thread)

face_thread.start()
hand_thread.start()

try:
    while True:
        # 画像処理のデータを使用
        senddata.append(eyedata)
        print(senddata)

        trueeye.listen()

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

except Exception as e:
    pass

# スレッドを終了
face_thread.join()
hand_thread.join()

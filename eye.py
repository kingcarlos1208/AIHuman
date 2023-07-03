import cv2
from cvzone.HandTrackingModule import HandDetector
from deepface import DeepFace

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

handdetector = HandDetector(detectionCon=0.8, maxHands=2)
cap = cv2.VideoCapture(0)
cap.set(3, 2256)
cap.set(4, 1504)

def face(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    try:
        if len(faces) > 0:
            for (x, y, w, h) in faces:
                face_img = img[y:y+h, x:x+w]
                result = DeepFace.analyze(face_img, actions=['emotion'])
                emotions = result[0]['emotion']
                max_emotion = max(emotions, key=emotions.get)
                print(max_emotion)
    except ValueError as e:
        a = 2

def hand(img):
    hands, img = handdetector.findHands(img)
    h, w, _ = img.shape
    if hands:
        data = []
        hand = hands[0]
        lmList = hand["lmList"]
        for lm in lmList:
            data.extend([lm[0], h - lm[1], lm[2]])

        message = str(data) + '\n'
        print(message)

while True:
    success, img = cap.read()
    if not success:
        break

    face(img)
    hand(img)

    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == 27:  # ESCキーでループを終了
        break

cap.release()
cv2.destroyAllWindows()

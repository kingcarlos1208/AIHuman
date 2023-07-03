import speech_recognition as sr

# recognizerインスタンスを作成
r = sr.Recognizer()

# 本番

def listen():
    while True:
        with sr.Microphone() as source:
            try:
                #print("準備ができました")
                audio = r.listen(source, timeout=10)
                #print("recognizing...")
                send = r.recognize_google(audio, language="ja-JP")
                #print("あなた:" + send)
            except sr.WaitTimeoutError:
                #print("Timeout occurred.")
                a=2
            except sr.UnknownValueError:
                #print("Sorry, I can't understand your voice")
                a=1

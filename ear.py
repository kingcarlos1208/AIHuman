import vosk
import pyaudio
import json

# モデルの読み込み
model = vosk.Model("model")

# 音声認識器の作成
rec = vosk.KaldiRecognizer(model, 16000)

# マイクからの音声入力の設定
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=2000)
stream.start_stream()

# 音声認識の実行
def realear(stream):
    data = stream.read(2000)
    if len(data) == 0:
        pass
    if rec.AcceptWaveform(data):
        # 認識結果を表示
        result = json.loads(rec.Result())
        text = result['text']
        print(text)

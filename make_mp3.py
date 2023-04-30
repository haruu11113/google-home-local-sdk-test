from gtts import gTTS
text = "ダイエットの時間です、腹筋してください。"

tts = gTTS(text=text, lang='ja')
tts.save('greeting.mp3')

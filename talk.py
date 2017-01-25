# -*- coding: utf-8 -*-

from gtts import gTTS

word = ("yüz metre sonra sola dönün")
tts = gTTS(text=word, lang='tr')
tts.save("C:/Users/dogan_coruh/Desktop/test.mp3")
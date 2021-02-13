from gtts import gTTS
import os

myText = 'Tr you got a message'

language = 'en'

myObject = gTTS(text = myText, lang = language, slow = False)
myObject.save('tone.mp3')
os.system('tone.mp3')

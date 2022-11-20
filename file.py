from gtts import gTTS

# This module is imported so that we can
# play the converted audio
import os

mytext = input("Enter the text")
language = 'en'
myobj = gTTS(text=mytext, lang=language, fast=True)

myobj.save("welcome.mp3")

os.system("welcome.mp3")
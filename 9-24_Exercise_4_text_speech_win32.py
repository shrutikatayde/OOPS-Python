# pip install pypiwin32

# text to speech coversion by using win32 API

import win32com.client

speak = win32com.client.Dispatch("SAPI.SpVoice")
while 1:
    print("Enter the string : ")
    str = input()
    speak.Speak(str)

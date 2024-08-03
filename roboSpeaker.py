import win32com.client as wincom

# you can insert gaps in the narration by adding sleep calls
import time

print("Welcome to Robo Speaker ")

speak = wincom.Dispatch("SAPI.SpVoice")

text = "Python text-to-speech test. using win32com.client"
speak.Speak(text)

speak.Speak("Hello satya")
# 3-second sleep
time.sleep(3)

# text = "This text is read after 3 seconds"
# speak.Speak(text)

while True:
        x = input("Enter what you want to say : ")

        if x == "q":
            speak.Speak("bye friend")
            break

        speak.Speak(x)

# this code is for mac os
# import os
# if __name__ == '__main__':
#     print("Welcome to Robo Speaker ")
#
#     while True:
#         x = input("Enter what you want to say : ")
#
#         if x == "q":
#             os.system("say 'bye friend'")
#             break
#
#         command = f"say{x}"
#         os.system(command)

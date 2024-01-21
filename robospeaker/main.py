
import win32com.client as wincom
if __name__ == '__main__':
    print("welcome to robo speak system")
    while True:
        x = input("please enter what you want me to speak")
        speak = wincom.Dispatch("SAPI.SpVoice")
        if x == "q":
          break
        command = f"{x}"
        speak.Speak(command)










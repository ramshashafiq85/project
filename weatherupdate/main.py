
import win32com.client as wincom
x = input("what do you want me to speak\n")
url = f"https://api.weatherapi.com/v1/current.json?key=0963c1c1c6be47a0be4184127231912&q={city}"
r = requests.get(url)
print(r.text)
wdic = json.loads(r.text)
w = wdic["current"]["temp_c"]
l = wdic["location"]["lat"]
speak = wincom.Dispatch("SAPI.SpVoice")
text = (f"the current weather in {city} is {w} degrees and the location of the {city}  is {l}")
speak.speak(text)





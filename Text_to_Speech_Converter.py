import pyttsx3
engine = pyttsx3.init('sapi5')  # only for windows
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # "voice" and voiceID
text = " Hey , welcome to my channel !!"
txt = " Dont, Forget to Codescribe , ok then , let's build a GUI app"
engine.say(txt)
engine.runAndWait()

engine.save_to_file("Trial", 'text.mp3')
engine.runAndWait()

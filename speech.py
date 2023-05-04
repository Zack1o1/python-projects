#importing all requird libraries
import pyttsx3
from tkinter import *
from tkinter import ttk
import tkinter as tk

# creating new window
root = tk.Tk()
root.title('Speech App')
root.geometry("560x528")
root.resizable(False, False)

# styling button
style = ttk.Style()
style.configure('TButton', foreground="green")
# initialize pyttsx3 
try:
    engine = pyttsx3.init()
except:
    print('Maybe pyttsx3 is not installed!')

# creating frame
frame = ttk.Frame(root,padding=10)
frame.pack()

# creating speak function to read the entered text
def speak():
    # getting the user entered text by get function 
    speaking_text = text.get('1.0', 'end')
    
    # using pyttsx3 to speak entered text
    engine.say(speaking_text)
    engine.runAndWait()

# creating button to speak
btn = ttk.Button(frame, text='Speak', command=speak)
btn.pack(padx=5,side=LEFT)

# creating label to show
label = ttk.Label(frame, text='Enter your text:',font=('Arial',15))
label.pack(pady=10)


# creating text box to write
text = Text(frame,foreground='green',background='white',font=('Arial',14), borderwidth=2, relief="groove",height=19)
text.pack(padx=30)

def save_file():
    entered_text = text.get('1.0','end')
    engine.save_to_file(entered_text, 'speech.mp3')
    
# creating button to save file to mp3
btn_save = ttk.Button(frame, text='save audio', command=save_file)
btn_save.pack(pady=5,side=LEFT)

mainloop()


# Lalit Rajbanshi
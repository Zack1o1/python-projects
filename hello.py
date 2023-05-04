# importing all required libraries
import pyttsx3
from tkinter import *
from tkinter import ttk

# for new window
root = Tk()
root.title('Display name')
root.geometry("350x350")
root.resizable(False, False)

# for styling ttk
style = ttk.Style()
style.configure('TButton', padding=5)
style.configure('cus.TButton', foreground="blue", font=("Arial",12))

# frame
frame = ttk.Frame(root, padding=20)
frame.grid(pady=70)

# library to read aloud
engine = pyttsx3.init()

# main fun for our app
def main():
    def display_name():
        get_name = "Hello " + name_box.get()
        name.destroy()
        name_box.destroy()
        btn.destroy()
        engine.say(get_name)
        engine.runAndWait()
        def quit():
            root.destroy()
        
        def rename():
            new_frame.destroy()
            display.destroy()
            main()
            
            
        new_frame = ttk.Frame(root, padding=5)
        new_frame.grid(pady=70)
        
        display = ttk.Label(frame, text=get_name,font=("Arial", 18), foreground="green",wraplength=300)
        reset_btn = ttk.Button(new_frame, text="reset", command=rename)
        quit_btn = ttk.Button(new_frame, text="Quit", command=quit)
        
        display.grid(row=0, column=0)
        reset_btn.grid(row=1, column=0, padx=10, pady=10)
        quit_btn.grid(row=1, column=1, padx=10, pady=10)
        
    name = ttk.Label(frame, text="Enter Your Name:",font=("Arial", 15), foreground="green")
    name_box = ttk.Entry(frame, font=("Arial", 20))
    btn = ttk.Button(frame, text="submit", command=display_name, style="cus.TButton")
    
    name.grid()
    name_box.grid(pady=20)
    btn.grid(pady=20)

  
main()
# dead center
root.eval('tk::PlaceWindow %s center' % root.winfo_toplevel())    
root.mainloop()
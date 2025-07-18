from tkinter import * 
from tkinter.scrolledtext import ScrolledText
from PasswordGeneration import *
from PasswordBruteForce import *
import ctypes

# f = ctypes.CDLL('./libBF.so', winmode=0)

a = []

def show_message():
    label['text'] = 'Введите заметку'
    if entry.get() != '': 
        a.append(f'{len(a) + 1}. ' + Generation() + f' - {entry.get()}')
        res = ''
        for i in a:
            res += '' + i + '\n'
        
        st.delete('1.0', END)
        st.insert(END, f'{res}') 
        label['text'] = res

def show_message2():
    label['text'] = 'Введите заметку'
    if entry.get() != '': 
        a.append(f'взломан за ' + f'{BruteForce(entry.get())}' + f' - {entry.get()}')
        res = ''
        for i in a:
            res += '' + i + '\n'
        
        st.delete('1.0', END)
        st.insert(END, f'{res}') 
        label['text'] = res

    

root = Tk()
root.title('HackPassword(YanaSola)')
icon = PhotoImage(file = "iconYana.png")
root.iconphoto(False, icon)
root.geometry('400x300')

def on_modified(event):
    label["text"]=editor.selection_get()

editor = Text(height=8)
editor.bind("<<Selection>>", on_modified)
	
st = ScrolledText(root, width=10,  height=10)
st.pack(fill=BOTH, side=LEFT, expand=True)

entry = Entry()
entry.pack(anchor=NW, padx=6, pady=6)
  
btn = Button(text="Click Generations", command=show_message)
btn.pack(anchor=NW, padx=6, pady=6)

btn = Button(text="Click the Brute Force", command=show_message2)
btn.pack(anchor=NW, padx=6, pady=1)

label = Label()
label.pack(anchor=NW, padx=6, pady=6)

  
root.mainloop()
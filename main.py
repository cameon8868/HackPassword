from tkinter import * 
from tkinter.scrolledtext import ScrolledText
from PasswordGeneration.PG import *
from BruteForce.PBF import *
import ctypes

lib = ctypes.CDLL('./BruteForce/libBF.so', winmode=0)
lib.print_string.argtypes = [ctypes.c_char_p]
lib.print_string.restype = ctypes.c_double
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
        a.append(f'взломан за ' + f'{lib.print_string(entry.get().encode('utf-8'))} секунд' + f' - {entry.get()}')
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
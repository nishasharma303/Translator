from tkinter import *
from tkinter import ttk, messagebox
from deep_translator import GoogleTranslator

root = Tk()
root.title("Google Translator")
root.geometry("1080x400")

def label_change():
    c = combo1.get()
    c1 = combo2.get()
    label1.configure(text=c)
    label2.configure(text=c1)
    root.after(1000, label_change)

def translate_now():
    try:
        text_ = text1.get(1.0, END).strip()
        if not text_:
            messagebox.showwarning("Warning", "Please enter text to translate.")
            return
        
        src_lang = combo1.get().lower()
        dest_lang = combo2.get().lower()

        translated_text = GoogleTranslator(source=src_lang, target=dest_lang).translate(text_)
        text2.delete(1.0, END)
        text2.insert(END, translated_text)

    except Exception as e:
        messagebox.showerror("Translation Error", f"Error: {str(e)}")

languages = GoogleTranslator().get_supported_languages()
languageV = [lang.capitalize() for lang in languages]

combo1 = ttk.Combobox(root, values=languageV, font="Roboto 14", state="r")
combo1.place(x=110, y=20)
combo1.set("english")

label1 = Label(root, text="English", font="segoe 30 bold", bg="white", width=18, bd=5, relief=GROOVE)
label1.place(x=10, y=50)

f = Frame(root, bg="BLACK", bd=5)
f.place(x=10, y=118, width=440, height=210)

text1 = Text(f, font="Robote 20", bg="white", relief=GROOVE, wrap=WORD)
text1.place(x=0, y=0, width=430, height=200)

scrollbar1 = Scrollbar(f)
scrollbar1.pack(side="right", fill="y")
scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar1.set)

combo2 = ttk.Combobox(root, values=languageV, font="Roboto 14", state="r")
combo2.place(x=730, y=20)
combo2.set("select language")

label2 = Label(root, text="English", font="segoe 30 bold", bg="white", width=18, bd=5, relief=GROOVE)
label2.place(x=620, y=50)

f1 = Frame(root, bg="BLACK", bd=5)
f1.place(x=620, y=118, width=440, height=210)

text2 = Text(f1, font="Robote 20", bg="white", relief=GROOVE, wrap=WORD)
text2.place(x=0, y=0, width=430, height=200)

scrollbar2 = Scrollbar(f1)
scrollbar2.pack(side="right", fill="y")
scrollbar2.configure(command=text2.yview)
text2.configure(yscrollcommand=scrollbar2.set)

translate = Button(root, text="Translate", font="Roboto 15 bold italic",
                   activebackground="grey", cursor="hand2",
                   bd=5, bg="blue", fg="white", command=translate_now)
translate.place(x=480, y=250)

label_change()
root.configure(bg="white")
root.mainloop()

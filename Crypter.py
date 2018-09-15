#Я конечно хз что редачить, но думаю что моему комменту здесь есть место)
import pyAesCrypt
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import os

def PrintMessage(message, style):
    Viewer.insert(INSERT, message, style)

def EnCrypt(file):
    bufferSize = os.path.getsize(file)*1024
    PrintMessage("# Crypt file " + str(file) + "\n#\n", 'normal')
    try: pyAesCrypt.encryptFile(str(file), str(file) + '.jmz', str(EditPass.get()), bufferSize)
    except:
        PrintMessage("# File " + str(file) + " failed\n#\n", 'error')
        return -1
    else: PrintMessage("# File " + str(file) + " crypted success\n#\n", 'success')
    os.remove(file)

def DeCrypt(file):
    bufferSize = os.path.getsize(file)*1024
    PrintMessage( "# Decrypt file " + str(file) + "\n#\n", 'normal')
    try: pyAesCrypt.decryptFile(str(file), str(os.path.splitext(file)[0]), str(EditPass.get()), bufferSize)
    except:
        PrintMessage("# File " + str(file) + " failed\n#\n", 'error')
        return -1
    else: PrintMessage("# File " + str(file) + " decrypted success\n#\n", 'success')
    os.remove(os.path.splitext(file)[0] + '.jmz')

def Encrypt_Path_Walk(dir):
    for name in os.listdir(dir):
        path = os.path.join(dir, name)
        filename, file_extension = os.path.splitext(path)
        if file_extension == '.jmz': pass
        else:
            if os.path.isfile(path) : EnCrypt(path)
            else: Encrypt_Path_Walk(path)

def Decrypt_Path_Walk(dir):
    if dir == '' or EditPass.get() == '': return
    for name in os.listdir(dir):
        path = os.path.join(dir, name)
        filename, file_extension = os.path.splitext(path)
        if file_extension != '.jmz': return
        else:
            if os.path.isfile(path):
                try: DeCrypt(path)
                except: pass
            else: Decrypt_Path_Walk(path)

def Changer_Crypt(dir):
    if dir == '' or EditPass.get() == '': return
    filename, file_extension = os.path.splitext(dir)
    if os.path.exists(dir):
        if os.path.isfile(dir) :
            if file_extension == '.jmz':
                PrintMessage("# File " + dir + " crypted!\n#\n", 'error')
                return
            EnCrypt(dir)
        else: Encrypt_Path_Walk(dir)
    else:
        PrintMessage("# Error: not found directory \n#\n", "error")

def Changer_Decrypt(dir):
    if dir == '' or EditPass.get() == '': return
    filename, file_extension = os.path.splitext(dir)
    if os.path.exists(dir):
        if os.path.isfile(dir) :
            if file_extension != '.jmz':
                PrintMessage("# File " + dir + " not crypted!\n#\n", 'error')
                return
            DeCrypt(dir)
        else: Decrypt_Path_Walk(dir)
    else:
        PrintMessage("# Error: not found directory \n#\n", "error")

def Open_File():
    # file = tkFileDialog.askopenfilename()
    file = filedialog.askopenfilename(filetypes = (("All files", "*.*"), ("Text file", "*.txt"), ("Images file", "*.jpg, *.jpeg, *.png")) )
    EditPath.delete(0, END)
    EditPath.insert(0, str(file))

root = Tk()
root.title("Crypter by jimezo")
root.geometry("800x600")
root.resizable(width=False, height=False)

EditPath = ttk.Entry(root, font=('Times New Roman', 14))
EditPath.place(width=440, height=40, x=300, y=90)

EditPass = ttk.Entry(root, font=('Times New Roman', 14))
EditPass.place(width=250, height=40, x=20, y=90)

EditPathLabel = ttk.Label(root, text="Путь к файлу: ", font=('Times New Roman', 18))
EditPathLabel.place(x=300, y=50)

EditPathLabel = ttk.Label(root, text="Пароль: ", font=('Times New Roman', 18))
EditPathLabel.place(x=20, y=50)

EncryptBtn = ttk.Button(root, text="Зашифровать",command=lambda: Changer_Crypt(EditPath.get()))
EncryptBtn.place(width=120, height=40, x=20, y=160)

DecryptBtn = ttk.Button(root, text="Расшифровать", command=lambda: Changer_Decrypt(EditPath.get()))
DecryptBtn.place(width=120, height=40, x=150, y=160)

OpenFIleBtn = ttk.Button(root, text="...", command=Open_File)
OpenFIleBtn.place(width=40, height=40, x=750, y=90)

Viewer = Text(root)
Viewer.place(width=760, height=330, x=20, y=240)
Viewer.bind("<Key>", lambda e: "break")
vscroll = ttk.Scrollbar(Viewer, orient=VERTICAL, command=Viewer.yview)
Viewer['yscroll'] = vscroll.set
vscroll.pack(side=RIGHT, fill=Y)
Viewer.tag_config('success', foreground="green")
Viewer.tag_config('error', foreground="red")
Viewer.tag_config('normal', foreground="black")


root.mainloop()

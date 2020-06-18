from tkinter import *
import tkinter as tk
from tkinter.filedialog import askopenfilename
from urllib.parse import unquote
import re
from urllib.parse import urlparse
import base64
import string
import random
import alan_mod_ph
import alan_mod_mlwscan
import requests

#PHISHING MENU
def ScanSimpleURL():
    def IsLive():
        r = requests.get(e1.get())
        try:
            if r.status_code == 200:
                return True
            elif r.status_code == 301:
                return True
            else:
                return False
        except:
            return False
    master = tk.Tk()
    tk.Label(master,text="URL", width=30, heigh=1).grid(row=0)
    e1 = tk.Entry(master)
    e1.grid(row=0, column=1)
    tk.Button(master, text='Quit', command=master.quit).grid(row=3, column=0, sticky=tk.W, pady=4)
    tk.Button(master, text='Check', command=IsLive).grid(row=3, column=1, sticky=tk.W, pady=4)
    tk.mainloop()

def NewTargetPattern():
    target = "YmlsbC5mb3JkLmdhbGxhbnRpbmVAaG90bWFpbC5jb20="
    text_box = tk.Text(root, heigh=10, width= 30)
    text_box.insert("1.0", "[New Target Pattern]\n")
    text_box.insert("2.0", target)
    text_box.pack()

def ScanFilePhishing():
    name = askopenfilename()
    t_file = open(name, 'r')
    for line in t_file:
        dec = alan_mod_ph.DecoderDetector(line)
        print(dec)
        try:
            alan_mod_ph.RenderHTTPRequest(dec)
        except:
            pass
    text_box = tk.Text(root, heigh=10, width=30)
    text_box.insert("1.0", "[URL]\n")
    text_box.insert("2.0", dec)
    text_box.pack()
    if alan_mod_ph.IsLive(dec) == True:
        msg = tk.Message(root, text="Live")
        msg.config(bg='green')
        msg.pack()
    else:
        msg = tk.Message(root, text="Down")
        msg.config(bg='red')
        msg.pack()

#MALWARE MENU
def ScanEXEImports():
    name = askopenfilename()     
    res = alan_mod_mlwscan.ShowImportsDllEXE(name)
    tex = alan_mod_mlwscan.GetLineFromFile('suspectedlibfunc.txt')
    compare_arrays = set(res) & set(tex)
    S = tk.Scrollbar(root)
    labelexeimports = tk.Text(root, heigh=9, width=30)
    labelexeimports.insert("1.0", "[List of DLLs]\n")
    labelexeimports.insert("2.0", compare_arrays)
    if len(compare_arrays) <= 2:
        labelexeimports.insert("3.0", "\nExe probably packed")
    S.pack(side=tk.RIGHT, fill=tk.Y)
    labelexeimports.pack(side=tk.LEFT, fill=tk.Y)
    S.config(command=labelexeimports.yview)

def GetAddressAndFunctions():
    name = askopenfilename()
    res = alan_mod_mlwscan.GetHexFromImportFunctions(name)
    S = tk.Scrollbar(root)
    labelexeimports = tk.Text(root, heigh=70, width=70)
    labelexeimports.insert("1.0", "[Address : Function]\n")
    labelexeimports.insert("2.0", res)
    S.pack(side=tk.RIGHT, fill=tk.Y)
    labelexeimports.pack(side=tk.TOP, fill=tk.Y)
    S.config(command=labelexeimports.yview)

def UploadAndReportFileToVT():
    name = askopenfilename()
    up_file = alan_mod_mlwscan.WrapperVTApiScanFile(name)
    r_file = alan_mod_mlwscan.WrapperVTApiGetReportFile(up_file)
    S = tk.Scrollbar(root)
    labelexeimports = tk.Text(root, heigh=70, width=60)
    labelexeimports.insert("1.0", "[Upload File Info]\n")
    labelexeimports.insert("2.0", up_file)
    labelexeimports.insert("3.0", "\n[Scan Result]\n")
    labelexeimports.insert("4.0", r_file)
    S.pack(side=tk.RIGHT, fill=tk.Y)
    labelexeimports.pack(side=tk.TOP, fill=tk.Y)
    S.config(command=labelexeimports.yview)

#SPAM MENU

#ABOUTMENU
def PrintBanner():
    var = StringVar()
    label = Message(root, textvariable= var, relief = RAISED)
    var.set("@mpalonso_")
    label.pack(side=TOP, pady = 6)
#GUI
root = Tk()
root.title("Alan by @cyberk1w1")
root.geometry("800x600")

# MENU
menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label="Phishing", menu=filemenu)
filemenu.add_command(label="Scan Phishing", command=ScanFilePhishing)
filemenu.add_command(label="Scan URL", command=ScanSimpleURL)
filemenu.add_command(label="New Target Pattern", command=NewTargetPattern)
mlwmenu = Menu(menu)
menu.add_cascade(label="Malware", menu=mlwmenu)
mlwmenu.add_command(label="Scan Imports of EXE file", command=ScanEXEImports)
mlwmenu.add_command(label="Scan Address + Functions of EXE file", command=GetAddressAndFunctions)
mlwmenu.add_command(label="Upload & Report to VT", command=UploadAndReportFileToVT)
mlwmenu.add_command(label="Scan Strings of EXE file", command="")
#TO DO
spammenu = Menu(menu)
menu.add_cascade(label="Spam", menu=spammenu)
spammenu.add_command(label="Submit HTML file", command="")
spammenu.add_command(label="Submit EML file", command="")
helpmenu = Menu(menu)
menu.add_cascade(label="About", menu=helpmenu)
helpmenu.add_command(label="About...", command=PrintBanner)
helpmenu.add_command(label='Exit', command=root.quit)
mainloop()
#############################/Imports/######################################################
from tkinter import *
from tkinter import ttk
import tkinter
from tkinter.ttk import *
from tkinter import filedialog
from pytube import *
from pytube import YouTube
import os
import sys
from asyncio.log import logger
import logging
#############################/Imports/######################################################
#############################/debugger/######################################################
def debugMode():
    CheckboxNotCriying=checkbox_var.get()
    
    if CheckboxNotCriying==True:
        logging.basicConfig(filename='test.log',level=logging.DEBUG)
        logging.debug('debugging is enabled')
    else:
        print('debugger is not enabled and you cant see this')
        print(CheckboxNotCriying)
#############################/debugger/######################################################
#############################/defs/######################################################
# basically makes the default folder desktop, as for now this is a windows only app.
directorio=desktop = os.path.expanduser("~/Desktop")
#############################/defs/######################################################
#############################/file_explorer/######################################################
def browseFiles():
    global directorio
    directorio = filedialog.askdirectory()
#############################/file_explorer/######################################################
#############################/descargarmp3/######################################################
def descargar1():
    try:
        stream1.download(output_path=directorio)
        os.chdir(directorio)
        finalName=stream1.default_filename.replace('.mp4','')
        os.rename(stream1.default_filename,finalName + ".mp3")
        WinCon.destroy()
    except :
        logger.exception('you fucked up')
#############################/descargarmp3/######################################################
def descargar2():
    try:
        yt = YouTube(txt1.get())
        stream2 = yt.streams.get_highest_resolution()
        stream2.download(output_path=directorio)
        WinCon.destroy()
    except:
        logger.exception('you fucked up at descargar2')
#############################/descargarmp4/######################################################
#############################/ConfirmarMP3/######################################################
def confirmarmp3():
    try:
        global stream1,Rounded1,WinCon
        yt = YouTube(txt1.get())
        stream1 = yt.streams.filter(only_audio=True).get_audio_only()
        Rounded1 = round(stream1.filesize_approx / 1000 / 1000, 2)
        WinCon = Tk()
        WinCon.title("confirmar")
        txt2 = Label(WinCon, width=10, text=str(Rounded1)+" Mb")
        txt2.grid(column=0, row=0)
        txt3 = Label(WinCon, text=stream1.title)
        txt3.grid(column=0, row=1)
        confirmar = Button(WinCon,text="confirmar", command=descargar1)
        confirmar.grid(column=0,row=2)
        negar = Button(WinCon,text="Cancelar",command=WinCon.withdraw)
        negar.grid(column=1,row=2)
        WinCon.mainloop()
    except:
        logger.exception('you fucked up at confirmarmp3')
#############################/ConfirmarMP3/######################################################
#############################/ConfirmarMP4/######################################################
def confirmarmp4():
    try:
        global stream2,Rounded2,WinCon
        yt = YouTube(txt1.get())
        stream2 = yt.streams.get_highest_resolution()
        Rounded2 = round(stream2.filesize_approx / 1000 / 1000, 2)
        WinCon = Tk()
        WinCon.title("confirmar")
        txt2 = Label(WinCon, width=10, text=str(Rounded2,'Mb'))
        txt2.grid(column=0, row=0)
        txt3 = Label(WinCon, text=stream2.title)
        txt3.grid(column=0, row=1)
        confirmar = Button(WinCon, text="confirmar", command=descargar2)
        confirmar.grid(column=0, row=2)
        negar = Button(WinCon, text="Cancelar", command=WinCon.withdraw)
        negar.grid(column=1, row=2)
        WinCon.mainloop()
    except:
        logger.exception('you fucked up at confirmarmp4')
#############################/ConfirmarMP4/######################################################
#############################/ConfirmarMP4/######################################################
window = Tk()                                                           #ClassDefinition
window.title("Yotube Downloader")                                       #Titulo
#window.iconbitmap("icon.ico")                                          #icon broken i dont know how to make it work
checkbox_var = IntVar()                                                 #int var, odio esto
checkbox = ttk.Checkbutton(window,
                text='Debug Mode',
                command=debugMode,
                variable=checkbox_var,
                onvalue=True,
                offvalue=False).grid(column=0, row=3)
lbl = Label (window, text="Youtube Downloader")                         #Label Decorativa
lbl.grid(column=0, row=0)                                               #Label Decorativa
btnmp3 = Button (window, text="Descargar Mp3",command=confirmarmp3)     #Descargarmp3   boton
btnmp3.grid(column=2, row=0)                                            #Descargarmp3   boton
btnmp4 = Button(window, text="Descargar Mp4", command=confirmarmp4)     #descargarMP4   boton
btnmp4.grid(column=2, row=1)                                            #descargarMP4   boton
txt1 = Entry(window,width=40)                                           #link
txt1.grid(column=0, row=2)                                              #link
txt1.get()                                                              #link
btn = Button(window, text="Donde descargar", command=browseFiles)       #FileExplorer boton
btn.grid(column=2, row=2)                                               #FileExplorer boton
window.mainloop()
#############################/mainUI/######################################################   
#############################/notes/######################################################
# notes
# pyinstaller --onefile -w -F --icon="icon.ico" --add-binary "icon.ico;." "SimplePyDownloader.py"
# pyinstaller --onefile -w -F "SimplePyDownloader.py"
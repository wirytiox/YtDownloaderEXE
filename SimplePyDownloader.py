#############################/Imports/######################################################
from tkinter import *
from tkinter.ttk import *
from pytube import *
from pytube import YouTube
from tkinter import filedialog
import os
#############################/Imports/######################################################
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
    stream1.download(output_path=directorio)
    os.chdir(directorio)
    finalName=stream1.default_filename.replace('.mp4','')
    os.rename(stream1.default_filename,finalName + ".mp3")
    WinCon.destroy()
#############################/descargarmp3/######################################################
def descargar2():
    yt = YouTube(txt1.get())
    stream2 = yt.streams.get_highest_resolution()
    stream2.download(output_path=directorio)
    WinCon.destroy()
#############################/descargarmp4/######################################################
#############################/ConfirmarMP3/######################################################
def confirmarmp3():
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
#############################/ConfirmarMP3/######################################################
#############################/ConfirmarMP4/######################################################
def confirmarmp4():
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
#############################/ConfirmarMP4/######################################################
#############################/mainUI/######################################################
window = Tk()                                                           #ClassDefinition
window.title("Yotube Downloader")                                       #Titulo
#window.iconbitmap("icon.ico")                                           #icon
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
window.mainloop()                                                       #Loop
#############################/mainUI/######################################################
#############################/notes/######################################################
# notes
# pyinstaller --onefile -w -F --icon="icon.ico" --add-binary "icon.ico;." "SimplePyDownloader.py"

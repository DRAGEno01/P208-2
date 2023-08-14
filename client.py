#-----------Bolierplate Code Start -----
import socket
from threading import Thread
from tkinter import *
from tkinter import ttk


PORT  = 8080
IP_ADDRESS = '127.0.0.1'
SERVER = None
BUFFER_SIZE = 4096


name = None
listbox =  None
textarea= None
labelchat = None
text_message = None


def openChatWindow():

   
    print("\n\t\t\t\tMusic Share App")

    #Client GUI starts here
    window=Tk()

    window.title('Music Share App')
    window.geometry("300x350")
    window.configure(bg="LightSkyBlue")

    global name
    global listbox
    global textarea
    global labelchat
    global text_message
    global filePathLabel

    selectLabel = Label(window, text= "Select Song", font = ("Calibri",8), bg="LightSkyBlue")
    selectLabel.place(x=10, y=2)

    listbox = Listbox(window,height = 10,width = 39,activestyle = 'dotbox', font = ("Calibri",10), bg="LightSkyBlue", borderwidth=2)
    listbox.place(x=10, y=18)

    scrollbar1 = Scrollbar(listbox)
    scrollbar1.place(relheight = 1,relx = 1)
    scrollbar1.config(command = listbox.yview)

    playButton=Button(window,text="Play/Pause",bd=1, font = ("Calibri",10), width=10, bg="SkyBlue")
    playButton.place(x=30,y=200)

    stop=Button(window,text="Stop",bd=1, font = ("Calibri",10), width=10, bg="SkyBlue")
    stop.place(x=200,y=200)

    upload=Button(window,text="Upload",bd=1, font = ("Calibri",10), width=10, bg="SkyBlue")
    upload.place(x=30,y=250) 

    download=Button(window,text="Download",bd=1, font = ("Calibri",10), width=10, bg="SkyBlue")
    download.place(x=200,y=250)

    infoLabel = Label(window, text="", font=("Calibri",8), fg="blue")
    infoLabel.place(x=4,y=280)
  
    window.mainloop()




def setup():
    global SERVER
    global PORT
    global IP_ADDRESS

    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.connect((IP_ADDRESS, PORT))

   
    openChatWindow()

setup()

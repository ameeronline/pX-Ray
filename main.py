import imp
from tkinter import *
from tkinter import filedialog
import tkinter as tk
from PIL import Image, ImageTk
import os 
from predict import Predict

def openimage():
    global filename
    filename=filedialog.askopenfilename(initialdir=os.getcwd(),title='Select Image File', filetypes=(("JPEG File", "*.jpeg"),("PNG File", "*.png"),("JPG File", "*.jpg"),("All File", "*.txt")))
    img = Image.open(filename)
    size = (250, 250)
    img2 = img.resize(size, Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img2)
    lbl.configure(image=img, width=250, height=250)
    lbl.image=img

def diagnose():
    path = filename.replace("/", "\\")
    result = Predict(path=path)
    if result == 'Person is safe.':
        text1 = Text(frame2,font="Robote 15", bg="white", fg='green', relief=GROOVE)
        text1.place(x=0,y=0,width=320,height=295)
    else:
        result = 'Person is affected with Pneumonia. \n60% disease spread diagnosed..'
        text1 = Text(frame2,font="Robote 15", bg="white", fg='red', relief=GROOVE)
        text1.place(x=0,y=0,width=320,height=295)
    text1.delete(1.0,END)
    text1.insert(END, result)


def run():
    global lbl, text1, frame2
    root = Tk()
    root.title("pX-Ray - Project")
    root.geometry("700x500+150+180")
    root.resizable(False,False)
    root.configure(bg="#000000")

    #Icon
    image_icon = PhotoImage(file='icon.png')
    root.iconphoto(False,image_icon)

    #Logo
    logo = PhotoImage(file='logo.png')
    Label(root,image=logo,bg="#000000").place(x=10,y=25)

    Label(root,text="MEDICAL SCIENCE", bg="#000000", fg="white", font="arial 25 bold").place(x=100,y=15)

    #First Frame
    frame1=Frame(root,bd=3,bg="black",width=340,height=280,relief=GROOVE)
    frame1.place(x=10,y=80)
    
    lbl=Label(frame1,bg='black')
    lbl.place(x=40,y=10)

    #Second Frame
    frame2=Frame(root,bd=3,bg="white",width=340,height=280,relief=GROOVE)
    frame2.place(x=350,y=80)

    text1 = Text(frame2,font="Robote 20", bg="white", fg='black', relief=GROOVE)
    text1.place(x=0,y=0,width=320,height=295)

    scrollbar1=Scrollbar(frame2)
    scrollbar1.place(x=320,y=0,height=300)

    scrollbar1.configure(command=text1.yview)
    text1.configure(yscrollcommand=scrollbar1.set)

    #Third Frame

    frame3=Frame(root,bd=3,bg='#000000',width=330,height=100,relief=GROOVE)
    frame3.place(x=10, y=370)

    Button(frame3,text='Open X-Ray', width=10, height=2, font='arial 14 bold',command=openimage).place(x=20,y=30)
    #Button(frame3,text='Save Image', width=10, height=2, font='arial 14 bold',command=save).place(x=180,y=30)
    Label(frame3,text='Upload X-Ray image to diagnose...', bg='#000000', fg='yellow').place(x=20,y=5)

    #Fourth Frame

    frame4=Frame(root,bd=3,bg='#000000',width=330,height=100,relief=GROOVE)
    frame4.place(x=360, y=370)

    Button(frame4,text='Diagnose', width=10, height=2, font='arial 14 bold',command=diagnose).place(x=20,y=30)
    #Button(frame4,text='Show Data', width=10, height=2, font='arial 14 bold',command=Show).place(x=180,y=30)
    Label(frame4,text='Diagnose X-Ray to Generate Report', bg='#000000', fg='yellow').place(x=20,y=5)



    root.mainloop()

run()
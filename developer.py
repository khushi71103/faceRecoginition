from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition Sysem")

        title_lbl=Label(self.root,text="DEVELOPER",font=("times new roman",35,"bold"),bg="white",fg="darkblue")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        imgT=Image.open(r"C:\Users\Khushi Chhetri\OneDrive\Desktop\Face recognition system\images\vivid-color-pattern-grafiti-draws-doodle-art-pattern-halloween-for-textiles-children-s-clothing-cool-background-vector.webp")
        imgT=imgT.resize((1530,720),Image.ANTIALIAS)
        self.photoimgT=ImageTk.PhotoImage(imgT)

        f_lbl=Label(self.root,image=self.photoimgT)
        f_lbl.place(x=0,y=55,width=1530,height=720)

        main_frame=Frame(f_lbl,bd=2,bg="white")
        main_frame.place(x=1000,y=0,width=500,height=600)

        imgT1=Image.open(r"C:\Users\Khushi Chhetri\OneDrive\Desktop\Face recognition system\images\kuku.jpg")
        imgT1=imgT1.resize((350,350),Image.ANTIALIAS)
        self.photoimgT1=ImageTk.PhotoImage(imgT1)

        f_lbl=Label(main_frame,image=self.photoimgT1)
        f_lbl.place(x=300,y=0,width=200,height=200)

        #developer info
        dev_label=Label(main_frame,text="Hello I am Khushi Chhetri",font=("times new roman",20,"bold"),bg="white")
        dev_label.place(x=0,y=5)

        dev_label=Label(main_frame,text="I am a student :)",font=("times new roman",20,"bold"),bg="white")
        dev_label.place(x=0,y=40)
        





if __name__=="__main__":
    root=Tk()
    obj=developer(root)
    root.mainloop()

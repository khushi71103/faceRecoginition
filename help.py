from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class help:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition Sysem")

        title_lbl=Label(self.root,text="HELP DESK",font=("times new roman",35,"bold"),bg="white",fg="darkblue")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        imgT=Image.open(r"C:\Users\Khushi Chhetri\OneDrive\Desktop\Face recognition system\images\vivid-color-pattern-grafiti-draws-doodle-art-pattern-halloween-for-textiles-children-s-clothing-cool-background-vector.webp")
        imgT=imgT.resize((1530,720),Image.ANTIALIAS)
        self.photoimgT=ImageTk.PhotoImage(imgT)

        f_lbl=Label(self.root,image=self.photoimgT)
        f_lbl.place(x=0,y=55,width=1530,height=720)

    
        #info
        dev_label=Label(f_lbl,text="@khushi71103@gmail.com",font=("times new roman",20,"bold"),bg="white")
        dev_label.place(x=600,y=350)

        
        





if __name__=="__main__":
    root=Tk()
    obj=help(root)
    root.mainloop()

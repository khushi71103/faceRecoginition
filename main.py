from tkinter import*
from tkinter import ttk
import tkinter
from PIL import Image,ImageTk
from student import student
from train import Train
from attendance import Attendance
from developer import developer
from help import help
from time import strftime
from datetime import datetime
import os
from faceie_recognition import Face_recognization

class Face_recognition_system:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1280x800+0+0")
        self.root.title("Face Recognition Sysem")

        #image1
        imgn=Image.open(r"C:\Users\Khushi Chhetri\OneDrive\Desktop\Face recognition system\images\2548730.jpg")
        imgn=imgn.resize((500,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(imgn)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)


        #image2
        img1=Image.open(r"C:\Users\Khushi Chhetri\OneDrive\Desktop\Face recognition system\images\2548730.jpg")
        img1=img1.resize((500,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=500,height=130)


        #image3
        img2=Image.open(r"C:\Users\Khushi Chhetri\OneDrive\Desktop\Face recognition system\images\2548730.jpg")
        img2=img2.resize((600,130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=530,height=130)

        #bgimage
        img3=Image.open(r"C:\Users\Khushi Chhetri\OneDrive\Desktop\Face recognition system\images\___still.webp")
        img3=img3.resize((1530,790),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=790)

        title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        #time
        def time():
            string=strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000,time)

        lbl=Label(title_lbl,font=('times new roman',14,'bold'),background='white',foreground='blue')
        lbl.place(x=0,y=0,width=110,height=50)
        time()


        #student button
        img4=Image.open(r"C:\Users\Khushi Chhetri\OneDrive\Desktop\Face recognition system\images\students-button.png")
        img4=img4.resize((220,220),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=200,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Student details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="black",fg="white")
        b1_1.place(x=200,y=300,width=220,height=40)

        #detect face button
        img5=Image.open(r"C:\Users\Khushi Chhetri\OneDrive\Desktop\Face recognition system\images\2490124.png")
        img5=img5.resize((220,220),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_data)
        b1.place(x=500,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Face detector",cursor="hand2",font=("times new roman",15,"bold"),bg="black",fg="white",command=self.face_data)
        b1_1.place(x=500,y=300,width=220,height=40)

        #atendance face button
        img6=Image.open(r"C:\Users\Khushi Chhetri\OneDrive\Desktop\Face recognition system\images\s-l400.jpg")
        img6=img6.resize((220,220),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.attendance_data)
        b1.place(x=800,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Attendance",cursor="hand2",command=self.attendance_data,font=("times new roman",15,"bold"),bg="black",fg="white")
        b1_1.place(x=800,y=300,width=220,height=40)

        #help button
        img7=Image.open(r"C:\Users\Khushi Chhetri\OneDrive\Desktop\Face recognition system\images\360_F_2309760_44oi2CWLA7eTZtQ13shEGE2iXUSP0u.jpg")
        img7=img7.resize((220,220),Image.ANTIALIAS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b1=Button(bg_img,image=self.photoimg7,command=self.help_data,cursor="hand2")
        b1.place(x=1100,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Help Desk",cursor="hand2",command=self.help_data,font=("times new roman",15,"bold"),bg="black",fg="white")
        b1_1.place(x=1100,y=300,width=220,height=40)


        #train face button
        img8=Image.open(r"C:\Users\Khushi Chhetri\OneDrive\Desktop\Face recognition system\images\download.jfif")
        img8=img8.resize((220,220),Image.ANTIALIAS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b1=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.train_data)
        b1.place(x=200,y=380,width=220,height=220)

        b1_1=Button(bg_img,text="Train data",cursor="hand2",font=("times new roman",15,"bold"),bg="black",fg="white",command=self.train_data)
        b1_1.place(x=200,y=580,width=220,height=40)

        #photo face button
        img9=Image.open(r"C:\Users\Khushi Chhetri\OneDrive\Desktop\Face recognition system\images\images.png")
        img9=img9.resize((220,220),Image.ANTIALIAS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b1=Button(bg_img,image=self.photoimg9,command=self.open_img,cursor="hand2")
        b1.place(x=500,y=380,width=220,height=220)

        b1_1=Button(bg_img,text="Photos",cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="black",fg="white")
        b1_1.place(x=500,y=580,width=220,height=40)

        #developer face button
        img10=Image.open(r"C:\Users\Khushi Chhetri\OneDrive\Desktop\Face recognition system\images\images.jfif")
        img10=img10.resize((220,220),Image.ANTIALIAS)
        self.photoimg10=ImageTk.PhotoImage(img10)

        b1=Button(bg_img,image=self.photoimg10,command=self.developer_data,cursor="hand2")
        b1.place(x=800,y=380,width=220,height=220)

        b1_1=Button(bg_img,text="Developer",command=self.developer_data,cursor="hand2",font=("times new roman",15,"bold"),bg="black",fg="white")
        b1_1.place(x=800,y=580,width=220,height=40)


        #exit face button
        img11=Image.open(r"C:\Users\Khushi Chhetri\OneDrive\Desktop\Face recognition system\images\360_F_31637290_L5oi4GGVWhQBNHYV3D8Xnnqk6STLNCVY.jpg")
        img11=img11.resize((220,220),Image.ANTIALIAS)
        self.photoimg11=ImageTk.PhotoImage(img11)

        b1=Button(bg_img,image=self.photoimg11,command=self.i_exit,cursor="hand2")
        b1.place(x=1100,y=380,width=220,height=220)

        b1_1=Button(bg_img,text="Exit",cursor="hand2",command=self.i_exit,font=("times new roman",15,"bold"),bg="black",fg="white")
        b1_1.place(x=1100,y=580,width=220,height=40)

    def open_img(self):
        os.startfile(r"C:\Users\Khushi Chhetri\OneDrive\Desktop\Face recognition system\data")
    
    def i_exit(self):
        self.i_exit=tkinter.messagebox.askyesno("Face Recognition","Are you sure to exit this project",parent=self.root)
        if self.i_exit>0:
            self.root.destroy()
        else:
            return 


        #function button

    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=student(self.new_window)

    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_recognization(self.new_window)

    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)
    
    def developer_data(self):
        self.new_window=Toplevel(self.root)
        self.app=developer(self.new_window)

    def help_data(self):
        self.new_window=Toplevel(self.root)
        self.app=help(self.new_window)
        







if __name__=="__main__":
    root=Tk()
    obj=Face_recognition_system(root)
    root.mainloop()
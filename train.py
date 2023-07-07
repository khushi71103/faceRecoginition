from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
from matplotlib import pyplot as plt
import numpy as np
import os

class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition Sysem")



        title_lbl=Label(self.root,text="TRAIN DATA SET",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        #image1
        img_t1=Image.open(r"C:\Users\Khushi Chhetri\OneDrive\Desktop\Face recognition system\images\2548730.jpg")
        img_t1=img_t1.resize((500,130),Image.ANTIALIAS)
        self.photoimg_t1=ImageTk.PhotoImage(img_t1)

        f_lbl=Label(self.root,image=self.photoimg_t1)
        f_lbl.place(x=0,y=45,width=500,height=130)


        #image2
        imgt1=Image.open(r"C:\Users\Khushi Chhetri\OneDrive\Desktop\Face recognition system\images\2548730.jpg")
        imgt1=imgt1.resize((500,130),Image.ANTIALIAS)
        self.photoimgt1=ImageTk.PhotoImage(imgt1)

        f_lbl=Label(self.root,image=self.photoimgt1)
        f_lbl.place(x=500,y=45,width=500,height=130)


        #image3
        imgtt2=Image.open(r"C:\Users\Khushi Chhetri\OneDrive\Desktop\Face recognition system\images\2548730.jpg")
        imgtt2=imgtt2.resize((600,130),Image.ANTIALIAS)
        self.photoimgt2=ImageTk.PhotoImage(imgtt2)

        f_lbl=Label(self.root,image=self.photoimgt2)
        f_lbl.place(x=1000,y=45,width=530,height=130)

        #bg_image
        img3t=Image.open(r"C:\Users\Khushi Chhetri\OneDrive\Desktop\Face recognition system\images\vivid-color-pattern-grafiti-draws-doodle-art-pattern-halloween-for-textiles-children-s-clothing-cool-background-vector.webp")
        img3t=img3t.resize((1530,790),Image.ANTIALIAS)
        self.photoimg3t=ImageTk.PhotoImage(img3t)

        bg_imgtimg3t=Label(self.root,image=self.photoimg3t)
        bg_imgtimg3t.place(x=0,y=130,width=1530,height=790)

        #title_lbl=Label(bg_img,text="STUDENT MANAGMENT SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="darkgreen")
        #title_lbl.place(x=0,y=0,width=1530,height=45)

        #main_frametimg3t=Frame(bg_imgtimg3t,bd=2)
        #main_frametimg3t.place(x=10,y=55,width=1500,height=600)
        b1_1=Button(self.root,text="TRAIN DATA",command=self.train_classifier,cursor="hand2",font=("times new roman",30,"bold"),bg="black",fg="white")
        b1_1.place(x=0,y=380,width=1530,height=60)

    def train_classifier(self):
        data_dir=(r"C:\Users\Khushi Chhetri\OneDrive\Desktop\Face recognition system\data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        facer=[]
        ids=[]

        for image in path:
            imgu=Image.open(image).convert('L')   #gray scale image
            imageNp=np.array(imgu,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            facer.append(imageNp)
            ids.append(id)
            cv2.imshow("training",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)

        #trainiing
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(facer,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Results","Training datasets completed!")


            





    
if __name__=="__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime
import cv2
from matplotlib import pyplot as plt
import numpy as np
import os

class Face_recognization:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition Sysem")

        title_lbl=Label(self.root,text="FACE RECOGNITION",font=("times new roman",35,"bold"),bg="white",fg="green")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        
        #bg_image
        img3t=Image.open(r"C:\Users\Khushi Chhetri\OneDrive\Desktop\Face recognition system\images\vivid-color-pattern-grafiti-draws-doodle-art-pattern-halloween-for-textiles-children-s-clothing-cool-background-vector.webp")
        img3t=img3t.resize((1530,790),Image.ANTIALIAS)
        self.photoimg3t=ImageTk.PhotoImage(img3t)

        bg_imgtimg3t=Label(self.root,image=self.photoimg3t)
        bg_imgtimg3t.place(x=0,y=45,width=1530,height=790)

        #button
        b1_1=Button(self.root,text="FACE RECOGNITION",cursor="hand2",font=("times new roman",30,"bold"),bg="black",fg="white",command=self.face_re)
        b1_1.place(x=0,y=380,width=1530,height=60)


#attendance
    def mark_attendance(self,ide,nu,r,d):
        with open(r"C:\Users\Khushi Chhetri\OneDrive\Desktop\Face recognition system\at.csv","r+",newline="\n") as f:
            mydatalist=f.readlines()
            name_list=[]
            for line in mydatalist:
                entry=line.split((','))
                name_list.append(entry[0])
            if((ide not in name_list)and(nu not in name_list)and(r not in name_list)and(d not in name_list)):
                now=datetime.now()
                d1=now.strftime('%D/%M/%Y')
                dtstring=now.strftime('%H:%M:%S')
                f.writelines(f"\n{ide},{nu},{r},{d},{dtstring},{d1},Present")
        name_list.sort()
                
                






    def face_re(self):
        def draw_boundary(img,classifier,scaleFactor,minneighbor,colorsi,textsi,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minneighbor)

            coord=[]

            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))

                conn=mysql.connector.connect(host="localhost",username="root",password="khushichhetri",database="facerec")
                my_cursor=conn.cursor()

                my_cursor.execute("select ID from student where ID="+str(id))
                ide=my_cursor.fetchone()
                ide="+".join(ide)

                my_cursor.execute("select Name from student where ID="+str(id))
                nu=my_cursor.fetchone()
                nu="+".join(nu)
                

                my_cursor.execute("select Roll from student where ID="+str(id))
                r=my_cursor.fetchone()
                r="+".join(r)
                

                my_cursor.execute("select Dep from student where ID="+str(id))
                d=my_cursor.fetchone()
                d="+".join(d)
                
                
                if confidence>77:
                    cv2.putText(img,f"ID:{ide}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Roll:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Name:{nu}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Department:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    self.mark_attendance(ide,nu,r,d)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                coord=[x,y,w,h]
            return coord
        
        def recon(img,clf,faceCascade):
            coord=draw_boundary(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img
        

        faceCascade=cv2.CascadeClassifier(r"C:\Users\Khushi Chhetri\AppData\Local\Programs\Python\Python38\Lib\site-packages\cv2\data\haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap=cv2.VideoCapture(0)

        while True:
            ret,img=video_cap.read()
            img=recon(img,clf,faceCascade)
            cv2.imshow("Welcome to face recognization",img)

            if cv2.waitKey(1)==13:
                break
        video_cap.release()
        cv2.destroyAllWindows()







if __name__=="__main__":
    root=Tk()
    obj=Face_recognization(root)
    root.mainloop()
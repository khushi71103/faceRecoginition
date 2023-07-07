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
import csv
from tkinter import filedialog

mydata=[]
class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition Sysem")

        #variables
        self.var_atten_id=StringVar()
        self.var_atten_roll=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_dep=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_data=StringVar()
        self.var_atten_att=StringVar()


        #image1
        img=Image.open(r"C:\Users\Khushi Chhetri\OneDrive\Desktop\Face recognition system\images\2548730.jpg")
        img=img.resize((500,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        table_frame=Label(self.root,image=self.photoimg)
        table_frame.place(x=0,y=0,width=500,height=130)


        #image2
        img1=Image.open(r"C:\Users\Khushi Chhetri\OneDrive\Desktop\Face recognition system\images\2548730.jpg")
        img1=img1.resize((500,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        table_frame=Label(self.root,image=self.photoimg1)
        table_frame.place(x=500,y=0,width=500,height=130)


        #image3
        img2=Image.open(r"C:\Users\Khushi Chhetri\OneDrive\Desktop\Face recognition system\images\2548730.jpg")
        img2=img2.resize((600,130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        table_frame=Label(self.root,image=self.photoimg2)
        table_frame.place(x=1000,y=0,width=530,height=130)

        #bgimage
        img3=Image.open(r"C:\Users\Khushi Chhetri\OneDrive\Desktop\Face recognition system\images\___still.webp")
        img3=img3.resize((1530,790),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=790)

        title_lbl=Label(bg_img,text="ATTENDANCE MANAGMENT SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="darkgreen")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        main_frame=Frame(bg_img,bd=2)
        main_frame.place(x=10,y=55,width=1500,height=600)

        #left label frame
        left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student attendance details",font=("times new roman",12,"bold"))
        left_frame.place(x=10,y=10,width=730,height=580)

        img_l=Image.open(r"C:\Users\Khushi Chhetri\OneDrive\Desktop\Face recognition system\images\many-students-reading-books-in-library-vector-19724920.jpg")
        img_l=img_l.resize((720,130),Image.ANTIALIAS)
        self.photoimg_l=ImageTk.PhotoImage(img_l)

        table_frame=Label(left_frame,image=self.photoimg_l)
        table_frame.place(x=5,y=0,width=720,height=130)

        left_inside_frame=Frame(left_frame,bd=2,relief=RIDGE,bg='white')
        left_inside_frame.place(x=0,y=135,width=720,height=370)

        #labeled entry

        #attendance id
        studentid_label=Label(left_inside_frame,text="Attendance ID:",font=("times new roman",12,"bold"),bg="white")
        studentid_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        studentid_combo= ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_id,font=("helvetica",13,"bold"))
        studentid_combo.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        #roll
        n_label=Label(left_inside_frame,text="Roll:",font=("times new roman",12,"bold"),bg="white")
        n_label.grid(row=0,column=2,padx=4,pady=8)

        n_combo= ttk.Entry(left_inside_frame,width=22,textvariable=self.var_atten_roll,font=("helvetica",13,"bold"))
        n_combo.grid(row=0,column=3,pady=8)

        #name
        d_label=Label(left_inside_frame,text="Name:",font=("times new roman",12,"bold"),bg="white")
        d_label.grid(row=1,column=0)

        d_combo= ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_name,font=("helvetica",13,"bold"))
        d_combo.grid(row=1,column=1,pady=8)

        #dep
        dep_label=Label(left_inside_frame,text="Department:",font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=1,column=2)

        dep_combo= ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_dep,font=("helvetica",13,"bold"))
        dep_combo.grid(row=1,column=3,pady=8)

        #time
        t_label=Label(left_inside_frame,text="Time:",font=("times new roman",12,"bold"),bg="white")
        t_label.grid(row=2,column=0)

        t_combo= ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_time,font=("helvetica",13,"bold"))
        t_combo.grid(row=2,column=1,pady=8)

        #date
        dat_label=Label(left_inside_frame,text="Date:",font=("times new roman",12,"bold"),bg="white")
        dat_label.grid(row=2,column=2)

        dat_combo= ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_data,font=("helvetica",13,"bold"))
        dat_combo.grid(row=2,column=3,pady=8)


        #attendance
        at_label=Label(left_inside_frame,text="Attendance status",font=("times new roman",12,"bold"),bg="white")
        at_label.grid(row=3,column=0)

        at_combo= ttk.Combobox(left_inside_frame,textvariable=self.var_atten_att,width=20,font=("helvetica",13,"bold"),state='readonly')
        at_combo['values'] = ("Status","Present","Absent")
        at_combo.current(0)
        at_combo.grid(row=3,column=1,pady=8)

        #buttons

        btn_frame=Frame(left_inside_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=300,width=715,height=35)
        
        save_btn=Button(btn_frame,text="Import csv",command=self.importCsv,width=17,font=("times new roman",13,"bold"),bg="blue")
        save_btn.grid(row=0,column=0)

        up_btn=Button(btn_frame,text="Export csv",command=self.exportCsv,width=17,font=("times new roman",13,"bold"),bg="blue")
        up_btn.grid(row=0,column=1)

        del_btn=Button(btn_frame,text="Update",width=17,font=("times new roman",13,"bold"),bg="blue")
        del_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=17,font=("times new roman",13,"bold"),bg="blue")
        reset_btn.grid(row=0,column=3)









        #right label frame
        right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Attendance details",font=("times new roman",12,"bold"))
        right_frame.place(x=750,y=10,width=720,height=580)

        #table
        table_frame=Frame(right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=5,y=5,width=700,height=455)

        scrii_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scrii_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.attendance_table=ttk.Treeview(table_frame,column=("ID","Roll","Name","Dep","Time","date","attendance"),xscrollcommand=scrii_x.set,yscrollcommand=scrii_y.set)

        scrii_x.pack(side=BOTTOM,fill=X)
        scrii_y.pack(side=RIGHT,fill=Y)
        scrii_x.config(command=self.attendance_table.xview)
        scrii_y.config(command=self.attendance_table.yview)

        self.attendance_table.heading("ID",text="ID")
        self.attendance_table.heading("Roll",text="Roll")
        self.attendance_table.heading("Name",text="Name")
        self.attendance_table.heading("Dep",text="Department")
        self.attendance_table.heading("Time",text="Time")
        self.attendance_table.heading("date",text="Date")
        self.attendance_table.heading("attendance",text="Attendance")

        
        self.attendance_table["show"]="headings"

        self.attendance_table.column("ID",width=100)
        self.attendance_table.column("Roll",width=100)
        self.attendance_table.column("Name",width=100)
        self.attendance_table.column("Dep",width=100)
        self.attendance_table.column("Time",width=100)
        self.attendance_table.column("date",width=100)
        self.attendance_table.column("attendance",width=100)
        
        self.attendance_table.pack(fill=BOTH,expand=1)

        self.attendance_table.bind("<ButtonRelease>",self.get_cursor)

        #fetch data
    def fetchdata(self,rows):
        self.attendance_table.delete(*self.attendance_table.get_children())
        for i in rows:
            self.attendance_table.insert("",END,values=i)

    #import
    def importCsv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="open csv",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchdata(mydata)

    #export
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No data found to export",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="open csv",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your data exported to "+os.path.basename(fln)+"Successfully")
        except Exception as es:
            messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)

    def get_cursor(self,event=""):
        cursor_row=self.attendance_table.focus()
        content=self.attendance_table.item(cursor_row)
        roes=content['values']
        self.var_atten_id.set(roes[0])
        self.var_atten_roll.set(roes[1])
        self.var_atten_name.set(roes[2])
        self.var_atten_dep.set(roes[3])
        self.var_atten_time.set(roes[4])
        self.var_atten_data.set(roes[5])
        self.var_atten_att.set(roes[6])


    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_data.set("")
        self.var_atten_att.set("")







    


        
        



if __name__=="__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()
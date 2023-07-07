from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
from matplotlib import pyplot as plt
import numpy as np

class student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition Sysem")


        #variables
        self.var_Dep=StringVar()
        self.var_Course=StringVar()
        self.var_Year=StringVar()
        self.var_Sem=StringVar()
        self.var_ID=StringVar()
        self.var_Name=StringVar()
        self.var_Div=StringVar()
        self.var_Roll=StringVar()
        self.var_Gender=StringVar()
        self.var_DOB=StringVar()
        self.var_Email=StringVar()
        self.var_Phone=StringVar()
        self.var_Address=StringVar()
        self.var_Teacher=StringVar()
        
        

        #image1
        img=Image.open(r"C:\Users\Khushi Chhetri\OneDrive\Desktop\Face recognition system\images\2548730.jpg")
        img=img.resize((500,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

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

        title_lbl=Label(bg_img,text="STUDENT MANAGMENT SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="darkgreen")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        main_frame=Frame(bg_img,bd=2)
        main_frame.place(x=10,y=55,width=1500,height=600)

        #left label frame
        left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student details",font=("times new roman",12,"bold"))
        left_frame.place(x=10,y=10,width=730,height=580)

        img_l=Image.open(r"C:\Users\Khushi Chhetri\OneDrive\Desktop\Face recognition system\images\many-students-reading-books-in-library-vector-19724920.jpg")
        img_l=img_l.resize((720,130),Image.ANTIALIAS)
        self.photoimg_l=ImageTk.PhotoImage(img_l)

        f_lbl=Label(left_frame,image=self.photoimg_l)
        f_lbl.place(x=5,y=0,width=720,height=130)

        #current course
        current_course=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Current course",font=("times new roman",12,"bold"))
        current_course.place(x=5,y=135,width=720,height=125)


        #department
        dep_label=Label(current_course,text="Department",font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10,sticky=W)

        dep_combo= ttk.Combobox(current_course,textvariable=self.var_Dep,font=("helvetica",13,"bold"),state='readonly')
        dep_combo['values'] = ("Select Department","Computer","IT","Civil", "Mechanical")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)


        #course
        course_label=Label(current_course,text="Course",font=("times new roman",12,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=10,sticky=W)

        course_combo= ttk.Combobox(current_course,textvariable=self.var_Course,font=("helvetica",13,"bold"),state='readonly')
        course_combo['values'] = ("Select Course","FE","SE","TE", "BE")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)


        #Year
        year_label=Label(current_course,text="Year",font=("times new roman",12,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10,sticky=W)

        year_combo= ttk.Combobox(current_course,textvariable=self.var_Year,font=("helvetica",13,"bold"),state='readonly')
        year_combo['values'] = ("Select Year","2020-21","2021-22","2022-23", "2023-24")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        #semester
        semester_label=Label(current_course,text="Semester",textvariable=self.var_Sem,font=("times new roman",12,"bold"),bg="white")
        semester_label.grid(row=1,column=2,padx=10,sticky=W)

        semester_combo= ttk.Combobox(current_course,textvariable=self.var_Sem,font=("helvetica",13,"bold"),state='readonly')
        semester_combo['values'] = ("Select Semester","Semester-1","Semester-2","Semester-3","Semester-4","Semester-5","Semester-6","Semester-7","Semester-8")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)



        #class student info
        class_student=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Class Student",font=("times new roman",12,"bold"))
        class_student.place(x=5,y=250,width=720,height=300)


        #student id
        studentid_label=Label(class_student,text="Student ID:",font=("times new roman",12,"bold"),bg="white")
        studentid_label.grid(row=0,column=0,padx=10,sticky=W)

        studentid_combo= ttk.Entry(class_student,textvariable=self.var_ID,width=20,font=("helvetica",13,"bold"))
        studentid_combo.grid(row=0,column=1,padx=10,sticky=W)


        #student name
        studentname_label=Label(class_student,text="Student Name:",font=("times new roman",12,"bold"),bg="white")
        studentname_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        studentname_combo= ttk.Entry(class_student,textvariable=self.var_Name,width=20,font=("helvetica",13,"bold"))
        studentname_combo.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        #class division
        studentdivi_label=Label(class_student,text="Class Division:",font=("times new roman",12,"bold"),bg="white")
        studentdivi_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        studentdivi_combo= ttk.Entry(class_student,textvariable=self.var_Div,width=20,font=("helvetica",13,"bold"))
        studentdivi_combo.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        #roll no
        studentdr_label=Label(class_student,text="Roll no::",font=("times new roman",12,"bold"),bg="white")
        studentdr_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        studentdr_combo= ttk.Entry(class_student,textvariable=self.var_Roll,width=20,font=("helvetica",13,"bold"))
        studentdr_combo.grid(row=1,column=3,padx=10,pady=5,sticky=W)


        #gemder
        studentdg_label=Label(class_student,text="Gender:",font=("times new roman",12,"bold"),bg="white")
        studentdg_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        gen_combo= ttk.Combobox(class_student,textvariable=self.var_Gender,font=("helvetica",13,"bold"),state='readonly')
        gen_combo['values'] = ("Gender","Male","Female","Other")
        gen_combo.current(0)
        gen_combo.grid(row=2,column=1,padx=2,pady=5,sticky=W)


        #dob
        studentdob_label=Label(class_student,text="Date of birth:",font=("times new roman",12,"bold"),bg="white")
        studentdob_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        studentdob_combo= ttk.Entry(class_student,textvariable=self.var_DOB,width=20,font=("helvetica",13,"bold"))
        studentdob_combo.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        #email
        studente_label=Label(class_student,text="Email:",font=("times new roman",12,"bold"),bg="white")
        studente_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        studente_combo= ttk.Entry(class_student,textvariable=self.var_Email,width=20,font=("helvetica",13,"bold"))
        studente_combo.grid(row=3,column=1,padx=10,pady=5,sticky=W)

        #phoneno
        studentp_label=Label(class_student,text="Phone no:",font=("times new roman",12,"bold"),bg="white")
        studentp_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        studentp_combo= ttk.Entry(class_student,textvariable=self.var_Phone,width=20,font=("helvetica",13,"bold"))
        studentp_combo.grid(row=3,column=3,padx=10,pady=5,sticky=W)


        #address
        studentda_label=Label(class_student,text="Address:",font=("times new roman",12,"bold"),bg="white")
        studentda_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)

        studentda_combo= ttk.Entry(class_student,textvariable=self.var_Address,width=20,font=("helvetica",13,"bold"))
        studentda_combo.grid(row=4,column=1,padx=10,pady=5,sticky=W)


        #teacher name
        studentdt_label=Label(class_student,text="Teacher's name:",font=("times new roman",12,"bold"),bg="white")
        studentdt_label.grid(row=4,column=2,padx=10,pady=5,sticky=W)

        studentdt_combo= ttk.Entry(class_student,textvariable=self.var_Teacher,width=20,font=("helvetica",13,"bold"))
        studentdt_combo.grid(row=4,column=3,padx=10,pady=5,sticky=W)

        #radio button
        self.var_radi1=StringVar()
        rad1=ttk.Radiobutton(class_student,text="Take photo sample",variable=self.var_radi1,width=20,value="Yes")
        rad1.grid(row=6,column=0)

        rad2=ttk.Radiobutton(class_student,variable=self.var_radi1,width=20,text="No photo sample",value="No")
        rad2.grid(row=6,column=1)

        #button frame
        btn_frame=Frame(class_student,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=200,width=715,height=35)
        
        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=17,font=("times new roman",13,"bold"),bg="blue")
        save_btn.grid(row=0,column=0)

        up_btn=Button(btn_frame,text="Update",command=self.update_data,width=17,font=("times new roman",13,"bold"),bg="blue")
        up_btn.grid(row=0,column=1)

        del_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=17,font=("times new roman",13,"bold"),bg="blue")
        del_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=17,font=("times new roman",13,"bold"),bg="blue")
        reset_btn.grid(row=0,column=3)

        btn_frame1=Frame(class_student,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=0,y=235,width=715,height=35)

        t_p=Button(btn_frame1,text="Take photo sample",command=self.gen_dataset,width=35,font=("times new roman",13,"bold"),bg="blue")
        t_p.grid(row=0,column=0)

        t_u=Button(btn_frame1,text="Update photo Sample",width=35,font=("times new roman",13,"bold"),bg="blue")
        t_u.grid(row=0,column=1)


        #right label frame
        right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student details",font=("times new roman",12,"bold"))
        right_frame.place(x=750,y=10,width=720,height=580)

        img_r=Image.open(r"C:\Users\Khushi Chhetri\OneDrive\Desktop\Face recognition system\images\360_F_197450000_4bOSZVkzeXCV4SBDhS1EvbqaM7zgMhWG.jpg")
        img_r=img_r.resize((720,130),Image.ANTIALIAS)
        self.photoimg_r=ImageTk.PhotoImage(img_r)

        f_lbl=Label(right_frame,image=self.photoimg_r)
        f_lbl.place(x=5,y=0,width=720,height=130)

        #search sys

        search_student=LabelFrame(right_frame,bd=2,bg="white",relief=RIDGE,text="Search system",font=("times new roman",12,"bold"))
        search_student.place(x=5,y=135,width=710,height=70)

        search_label=Label(search_student,text="Search by:",font=("times new roman",15,"bold"),bg="red",fg="white")
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        search_combo= ttk.Combobox(search_student,font=("helvetica",13,"bold"),state='readonly',width=15)
        search_combo['values'] = ("Select","Roll-no","Phone-no")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        studente_entry= ttk.Entry(search_student,width=15,font=("helvetica",13,"bold"))
        studente_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)


        ser_btn=Button(search_student,text="Search",width=12,font=("times new roman",13,"bold"),bg="blue")
        ser_btn.grid(row=0,column=3,padx=4)

        show_btn=Button(search_student,text="Show All",width=12,font=("times new roman",13,"bold"),bg="blue")
        show_btn.grid(row=0,column=4,padx=4)

        #table
        tab_student=Frame(right_frame,bd=2,bg="white",relief=RIDGE)
        tab_student.place(x=5,y=210,width=710,height=350)

        scr_x=ttk.Scrollbar(tab_student,orient=HORIZONTAL)
        scr_y=ttk.Scrollbar(tab_student,orient=VERTICAL)

        self.stu_table=ttk.Treeview(tab_student,column=("Dep","Course","Year","Sem","ID","Name","Division","Roll","Gender","DOB","Email","Phone","Address","Teacher","Photo"),xscrollcommand=scr_x.set,yscrollcommand=scr_y.set)

        scr_x.pack(side=BOTTOM,fill=X)
        scr_y.pack(side=RIGHT,fill=Y)
        scr_x.config(command=self.stu_table.xview)
        scr_y.config(command=self.stu_table.yview)

        self.stu_table.heading("Dep",text="Department")
        self.stu_table.heading("Course",text="Course")
        self.stu_table.heading("Year",text="Year")
        self.stu_table.heading("Sem",text="Sem")
        self.stu_table.heading("ID",text="ID")
        self.stu_table.heading("Name",text="Name")
        self.stu_table.heading("Division",text="Division")
        self.stu_table.heading("Roll",text="Roll-no")
        self.stu_table.heading("Gender",text="Gender")
        self.stu_table.heading("DOB",text="DOB")
        self.stu_table.heading("Email",text="Email")
        self.stu_table.heading("Phone",text="Phone-no")
        self.stu_table.heading("Address",text="Address")
        self.stu_table.heading("Teacher",text="Teacher")
        self.stu_table.heading("Photo",text="Photosamplestatus")
        self.stu_table["show"]="headings"

        self.stu_table.column("Dep",width=100)
        self.stu_table.column("Course",width=100)
        self.stu_table.column("Year",width=100)
        self.stu_table.column("Sem",width=100)
        self.stu_table.column("ID",width=100)
        self.stu_table.column("Name",width=100)
        self.stu_table.column("Division",width=100)
        self.stu_table.column("Roll",width=100)
        self.stu_table.column("Gender",width=100)
        self.stu_table.column("DOB",width=100)
        self.stu_table.column("Email",width=100)
        self.stu_table.column("Phone",width=100)
        self.stu_table.column("Address",width=100)
        self.stu_table.column("Teacher",width=100)
        self.stu_table.column("Photo",width=150)
        self.stu_table["show"]="headings"

        self.stu_table.pack(fill=BOTH,expand=1)
        self.stu_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()


        #function
    def add_data(self):
        if self.var_Dep.get()=="Select Deparment" or self.var_ID.get()=="" or self.var_Name.get()=="":
                messagebox.showerror("Error","All feilds are required!",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="khushichhetri",database="facerec")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                                self.var_Dep.get(),
                                                                                                                self.var_Course.get(),
                                                                                                                self.var_Year.get(),
                                                                                                                self.var_Sem.get(),
                                                                                                                self.var_ID.get(),
                                                                                                                self.var_Name.get(),
                                                                                                                self.var_Div.get(),
                                                                                                                self.var_Roll.get(),
                                                                                                                self.var_Gender.get(),
                                                                                                                self.var_DOB.get(),
                                                                                                                self.var_Email.get(),
                                                                                                                self.var_Phone.get(),
                                                                                                            self.var_Address.get(),
                                                                                                            self.var_Teacher.get(),
                                                                                                            self.var_radi1.get()
                                                                                                        
                                                                                                                                     ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student details has been added Sucessfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)

    #fetch
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="khushichhetri",database="facerec")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.stu_table.delete(*self.stu_table.get_children())
            for i in data:
                self.stu_table.insert("",END,values=i)
            conn.commit
        conn.close()
    
    #get
    def get_cursor(self,event=""):
        cursor_focus=self.stu_table.focus()
        content=self.stu_table.item(cursor_focus)
        data=content["values"]

        self.var_Dep.set(data[0]),
        self.var_Course.set(data[1]),
        self.var_Year.set(data[2]),
        self.var_Sem.set(data[3]),
        self.var_ID.set(data[4]),
        self.var_Name.set(data[5]),
        self.var_Div.set(data[6]),
        self.var_Roll.set(data[7]),
        self.var_Gender.set(data[8]),
        self.var_DOB.set(data[9]),
        self.var_Email.set(data[10]),
        self.var_Phone.set(data[11]),
        self.var_Address.set(data[12]),
        self.var_Teacher.set(data[13]),
        self.var_radi1.set(data[14])

    #update
    def update_data(self):
        if self.var_Dep.get()=="Select Deparment" or self.var_ID.get()=="" or self.var_Name.get()=="":
                messagebox.showerror("Error","All feilds are required!",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to update this student details",parent=self.root)
                if Update>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="khushichhetri",database="facerec")
                    my_cursor=conn.cursor()
                    sq="UPDATE student set Dep=%s,Course=%s,Year=%s,Sem=%s,Name=%s,Divison=%s,Roll=%s,Gender=%s,DOB=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,Photo=%s where ID=%s"
                    my_cursor.execute(sq,(self.var_Dep.get(),self.var_Course.get(),self.var_Year.get(),self.var_Sem.get(),self.var_Name.get(),self.var_Div.get(),self.var_Roll.get(),self.var_Gender.get(),self.var_DOB.get(),self.var_Email.get(),self.var_Phone.get(),self.var_Address.get(),self.var_Teacher.get(),self.var_radi1.get(),self.var_ID.get()))
                    
                else:
                    if not Update:
                        return
                
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Sucess","Student details update completed",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

    

    #delete
    def delete_data(self):
        if self.var_ID.get()=="":
                messagebox.showerror("Error","Student ID required!",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student delete page","Do you want to delete this student details",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="khushichhetri",database="facerec")
                    my_cursor=conn.cursor()
                    sql="delete from student where ID=%s"
                    val=(self.var_ID.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Sucessfully deleted student details",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)


    #reset
    def reset_data(self):
        self.var_Dep.set("Select Department"),
        self.var_Course.set("Select Course"),
        self.var_Year.set("Select Year"),
        self.var_Sem.set("Select Semester"),
        self.var_ID.set(""),
        self.var_Name.set(""),
        self.var_Div.set(""),
        self.var_Roll.set(""),
        self.var_Gender.set("Gender"),
        self.var_DOB.set(""),
        self.var_Email.set(""),
        self.var_Phone.set(""),
        self.var_Address.set(""),
        self.var_Teacher.set(""),
        self.var_radi1.set("")



    #photo samples
    def gen_dataset(self):
        if self.var_Dep.get()=="Select Deparment" or self.var_ID.get()=="" or self.var_Name.get()=="":
                messagebox.showerror("Error","All feilds are required!",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="khushichhetri",database="facerec")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                sq="UPDATE student set Dep=%s,Course=%s,Year=%s,Sem=%s,Name=%s,Divison=%s,Roll=%s,Gender=%s,DOB=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,Photo=%s where ID=%s"
                my_cursor.execute(sq,(self.var_Dep.get(),self.var_Course.get(),self.var_Year.get(),self.var_Sem.get(),self.var_Name.get(),self.var_Div.get(),self.var_Roll.get(),self.var_Gender.get(),self.var_DOB.get(),self.var_Email.get(),self.var_Phone.get(),self.var_Address.get(),self.var_Teacher.get(),self.var_radi1.get(),self.var_ID.get()==id+1))

                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()


                #load predefined

                face_classifier=cv2.CascadeClassifier(r"C:\Users\Khushi Chhetri\AppData\Local\Programs\Python\Python38\Lib\site-packages\cv2\data\haarcascade_frontalface_default.xml")
                
                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)

                    for(x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face= cv2.cvtColor(face,cv2.COLOR_BGR2RGB)
                        file_name_path="C:\\Users\Khushi Chhetri\\OneDrive\\Desktop\\Face recognition system\\data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2,cv2.LINE_AA)
                        cv2.imshow("Cropped Face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating data sets completed!!!")
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)








        





if __name__=="__main__":
    root=Tk()
    obj=student(root)
    root.mainloop()
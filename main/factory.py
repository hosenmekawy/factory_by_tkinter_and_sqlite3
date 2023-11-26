from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
from tkinter import font
from db import DataBase
from tkcalendar import Calendar
from datetime import datetime
import logging


class factory:
    def __init__(self, root):
        # Variables_employees
        self.db = DataBase("Elmekawy.db")

        self.name = StringVar()
        self.id_number = StringVar()
        self.phone = StringVar()
        self.days = StringVar()
        self.months = StringVar()
        self.years = StringVar()
        self.job = StringVar()
        self.gender = StringVar()
        self.now = datetime.now()
        # end variables_employees

        self.root = root
        self.root.state("zoomed")
        self.root.title("المكاوي")
        self.root.configure(background=white)
        self.root.resizable(TRUE, TRUE)

        # left side
        self.left_frame = Frame(self.root, bg=dark_black, width=240, height=800)
        self.left_frame.place(x=1, y=0)

        # upper
        self.Upper1_frame = Frame(self.root, bg=white, width=1285, height=120)
        self.Upper1_frame.place(x=246, y=0)

        # frame to show function name
        self.Upper1_frame_show_data = Frame(
            self.Upper1_frame, bg=dark_grey, width=1285, height=50
        )
        self.Upper1_frame_show_data.place(x=0, y=70)

        # self.add_image(
        #     r"backgrounds\background_show_edit.png", 1285, 100, 0, 20, self.Upper1_frame, white
        # )
        # center
        self.Upper_frame = Frame(self.root, bg=white, width=1285, height=700)
        self.Upper_frame.place(x=246, y=120)

        # line separator
        self.line1_frame = Frame(self.root, bg=whitey, width=1283, height=5)
        self.line1_frame.place(x=246, y=120)
        self.leftside_frame()

    def add_image(self, img, w, h, x1, y1, loc, cl):
        logo_pic_main = Image.open(img)
        resized = logo_pic_main.resize((w, h))
        logo_pic_mainB = ImageTk.PhotoImage(resized)
        logo_pic_main_A = Label(loc, image=logo_pic_mainB, bg=cl)
        logo_pic_main_A.image = logo_pic_mainB
        logo_pic_main_A.place(x=x1, y=y1)

    def getdata_employees(self, event):
        self.selected_row = self.tv.focus()
        self.data = self.tv.item(self.selected_row)
        global row
        row = self.data["values"]
        self.address_txt.delete(1.0, END)
        self.address_txt.insert(END, row[9])
        self.gender.set(row[8])
        self.job.set(row[7])
        self.years.set(row[6])
        self.months.set(row[5])
        self.days.set(row[4])
        self.phone.set(row[3])
        self.id_number.set(row[2])
        self.name.set(row[1])

    def delete_employees(self):
        if (
            self.name_entry.get() == ""
            or self.id_entry.get() == ""
            or self.phone_entry.get() == ""
            or self.job_entry.get() == ""
            or self.gender_combobox.get() == ""
            or self.address_txt.get(1.0, END) == ""
        ):
            messagebox.showerror(
                "ERROR",
                " لا يمكن حذف بسبب عدم وجود بيانات في الجدول متشابه مع الخانات او الخانات فاضيه",
            )
        else:
            messagebox.showerror("تم الحذف", "تم حذف الموظف بنجاح")
            self.db.remove_employee(row[0])
            self.clear_employees()
            self.displayAll_employees()

    def displayAll_employees(self):
        self.tv.delete(*self.tv.get_children())
        for row in self.db.fetch_employees():
            self.tv.insert("", END, values=row)

    def clear_employees(self):
        self.name_entry.delete(0, END)
        self.id_entry.delete(0, END)
        self.phone_entry.delete(0, END)
        self.days_combobox.set("")
        self.months_combobox.set("")
        self.year_entry.delete(0, END)
        self.job_entry.delete(0, END)
        self.gender_combobox.set("")
        self.address_txt.delete("1.0", END)

    def add_employee(self):
        if (
            self.name_entry.get() == ""
            or self.id_entry.get() == ""
            or self.phone_entry.get() == ""
            or self.job_entry.get() == ""
            or self.gender_combobox.get() == ""
            or self.address_txt.get(1.0, END) == ""
        ):
            messagebox.showerror("ERROR", "من فضلك لا تترك حقل فارغ")
        else:
            employee_id_num = self.id_entry.get()
            existing_employee = self.db.fetch_by_id_num(employee_id_num)

            if existing_employee:
                messagebox.showerror("Error", "الموظف موجود بالفعل في قاعدة البيانات")
            else:
                self.db.insert_employee(
                    self.name_entry.get(),
                    self.id_entry.get(),
                    self.phone_entry.get(),
                    self.days_combobox.get(),
                    self.months_combobox.get(),
                    self.year_entry.get(),
                    self.job_entry.get(),
                    self.gender_combobox.get(),
                    self.address_txt.get(1.0, END),
                )
                messagebox.showinfo(
                    "تم الحفظ بنجاح", "تم إضافة موظف جديد إلى قاعدة البيانات"
                )
                self.clear_employees()
                self.displayAll_employees()

    def update_employees(self):
        if (
            self.name_entry.get() == ""
            or self.id_entry.get() == ""
            or self.phone_entry.get() == ""
            or self.job_entry.get() == ""
            or self.gender_combobox.get() == ""
            or self.address_txt.get(1.0, END) == ""
        ):
            messagebox.showerror("ERROR", "من فضلك لا تترك حقل فارغ")
        else:
            self.db.update_employee(
                row[0],
                self.name_entry.get(),
                self.id_entry.get(),
                self.phone_entry.get(),
                self.days_combobox.get(),
                self.months_combobox.get(),
                self.year_entry.get(),
                self.job_entry.get(),
                self.gender_combobox.get(),
                self.address_txt.get(1.0, END),
            )

            messagebox.showinfo("تحتديث البيانات", "تم تحديث البيانات")
            self.clear_employees()
            self.displayAll_employees()

    def exit1(self):
        result = messagebox.askyesno("خروج", "هل انت متأكد")
        if result:
            root.destroy()

    def leftside_frame(self):
        self.left_frame_overlay = Frame(
            self.left_frame, bg=dark_black, width=240, height=800
        )
        self.left_frame_overlay.place(x=0, y=0)

        try:
            # adding logo to the left side
            logo_pic_main = Image.open(
                "logo\Screenshot_2023-07-24_202157-removebg-preview.png"
            )
            resized = logo_pic_main.resize((200, 80))
            logo_pic_mainB = ImageTk.PhotoImage(resized)
            logo_pic_main_A = Label(
                self.left_frame_overlay, image=logo_pic_mainB, bg=dark_black
            )
            logo_pic_main_A.image = logo_pic_mainB
            logo_pic_main_A.place(x=20, y=0)

        except Exception as e:
            print(f"An error occurred: {e}")

            # add buttons to the left side

        # add images at first position

        logo_pic_main = Image.open(r"button_images\Home.png")
        resized = logo_pic_main.resize((25, 25))
        logo_pic_mainB = ImageTk.PhotoImage(resized)
        logo_pic_main_A = Label(
            self.left_frame_overlay, image=logo_pic_mainB, bg=dark_black
        )
        logo_pic_main_A.image = logo_pic_mainB
        logo_pic_main_A.place(x=30, y=150)

        logo_pic_main = Image.open(r"button_images\warehouse.png")
        resized = logo_pic_main.resize((25, 25))
        logo_pic_mainB = ImageTk.PhotoImage(resized)
        logo_pic_main_A = Label(
            self.left_frame_overlay, image=logo_pic_mainB, bg=dark_black
        )
        logo_pic_main_A.image = logo_pic_mainB
        logo_pic_main_A.place(x=30, y=200)

        logo_pic_main = Image.open(r"button_images\mwowazfeen.png")
        resized = logo_pic_main.resize((25, 25))
        logo_pic_mainB = ImageTk.PhotoImage(resized)
        logo_pic_main_A = Label(
            self.left_frame_overlay, image=logo_pic_mainB, bg=dark_black
        )
        logo_pic_main_A.image = logo_pic_mainB
        logo_pic_main_A.place(x=30, y=250)

        logo_pic_main = Image.open(r"button_images\bank el cut.png")
        resized = logo_pic_main.resize((25, 25))
        logo_pic_mainB = ImageTk.PhotoImage(resized)
        logo_pic_main_A = Label(
            self.left_frame_overlay, image=logo_pic_mainB, bg=dark_black
        )
        logo_pic_main_A.image = logo_pic_mainB
        logo_pic_main_A.place(x=30, y=300)

        logo_pic_main = Image.open(r"button_images\masba8a.png")
        resized = logo_pic_main.resize((25, 25))
        logo_pic_mainB = ImageTk.PhotoImage(resized)
        logo_pic_main_A = Label(
            self.left_frame_overlay, image=logo_pic_mainB, bg=dark_black
        )
        logo_pic_main_A.image = logo_pic_mainB
        logo_pic_main_A.place(x=30, y=350)

        logo_pic_main = Image.open(r"button_images\ttreez.png")
        resized = logo_pic_main.resize((25, 25))
        logo_pic_mainB = ImageTk.PhotoImage(resized)
        logo_pic_main_A = Label(
            self.left_frame_overlay, image=logo_pic_mainB, bg=dark_black
        )
        logo_pic_main_A.image = logo_pic_mainB
        logo_pic_main_A.place(x=30, y=400)

        logo_pic_main = Image.open(r"button_images\t4teb da5ly.png")
        resized = logo_pic_main.resize((25, 25))
        logo_pic_mainB = ImageTk.PhotoImage(resized)
        logo_pic_main_A = Label(
            self.left_frame_overlay, image=logo_pic_mainB, bg=dark_black
        )
        logo_pic_main_A.image = logo_pic_mainB
        logo_pic_main_A.place(x=30, y=450)

        logo_pic_main = Image.open(r"button_images\t4teb 5arygy.png")
        resized = logo_pic_main.resize((25, 25))
        logo_pic_mainB = ImageTk.PhotoImage(resized)
        logo_pic_main_A = Label(
            self.left_frame_overlay, image=logo_pic_mainB, bg=dark_black
        )
        logo_pic_main_A.image = logo_pic_mainB
        logo_pic_main_A.place(x=30, y=500)

        logo_pic_main = Image.open(r"images\icons8-partner-50.png")
        resized = logo_pic_main.resize((25, 25))
        logo_pic_mainB = ImageTk.PhotoImage(resized)
        logo_pic_main_A = Label(
            self.left_frame_overlay, image=logo_pic_mainB, bg=dark_black
        )
        logo_pic_main_A.image = logo_pic_mainB
        logo_pic_main_A.place(x=30, y=550)

        logo_pic_main = Image.open(r"button_images\settings white.png")
        resized = logo_pic_main.resize((25, 25))
        logo_pic_mainB = ImageTk.PhotoImage(resized)
        logo_pic_main_A = Label(
            self.left_frame_overlay, image=logo_pic_mainB, bg=dark_black
        )
        logo_pic_main_A.image = logo_pic_mainB
        logo_pic_main_A.place(x=30, y=700)

        logo_pic_main = Image.open(r"button_images\exit.png")
        resized = logo_pic_main.resize((25, 25))
        logo_pic_mainB = ImageTk.PhotoImage(resized)
        logo_pic_main_A = Label(
            self.left_frame_overlay, image=logo_pic_mainB, bg=dark_black
        )
        logo_pic_main_A.image = logo_pic_mainB
        logo_pic_main_A.place(x=30, y=750)

        #  add buttons with labels
        home_btn = Button(
            self.left_frame_overlay,
            text="الصفحه الرئيسيه",
            bd=0,
            bg=dark_black,
            fg=white,
            font=("", 15),
        )
        home_btn.place(x=60, y=148)

        warehouse_btn = Button(
            self.left_frame_overlay,
            text=" المخزن",
            bd=0,
            bg=dark_black,
            fg=white,
            font=("", 15),
            command=self.warehouse_page,
        )
        warehouse_btn.place(x=60, y=198)

        employee_btn = Button(
            self.left_frame_overlay,
            text=" الموظفين",
            bd=0,
            bg=dark_black,
            fg=white,
            font=("", 15),
            command=self.employee_page,
        )
        employee_btn.place(x=60, y=248)

        cutting_table_btn = Button(
            self.left_frame_overlay,
            text=" مكتب القص",
            bd=0,
            bg=dark_black,
            fg=white,
            font=("", 15),
            command=self.cutting_table,
        )
        cutting_table_btn.place(x=60, y=298)

        colring_btn = Button(
            self.left_frame_overlay,
            text="المصبغه",
            bd=0,
            bg=dark_black,
            fg=white,
            font=("", 15),
        )
        colring_btn.place(x=60, y=348)

        colring_btn = Button(
            self.left_frame_overlay,
            text="التطريز",
            bd=0,
            bg=dark_black,
            fg=white,
            font=("", 15),
        )
        colring_btn.place(x=60, y=398)

        colring_btn = Button(
            self.left_frame_overlay,
            text="التشطيب الداخلي",
            bd=0,
            bg=dark_black,
            fg=white,
            font=("", 15),
        )
        colring_btn.place(x=60, y=448)

        colring_btn = Button(
            self.left_frame_overlay,
            text="التشطيب الخارجي",
            bd=0,
            bg=dark_black,
            fg=white,
            font=("", 15),
        )
        colring_btn.place(x=60, y=498)

        colring_btn = Button(
            self.left_frame_overlay,
            text="الصنايعيه ",
            bd=0,
            bg=dark_black,
            fg=white,
            font=("", 15),
            command=self.partners,
        )
        colring_btn.place(x=60, y=548)

        colring_btn = Button(
            self.left_frame_overlay,
            text=" الاعدادات",
            bd=0,
            bg=dark_black,
            fg=white,
            font=("", 15),
            command=self.settings,
        )
        colring_btn.place(x=60, y=698)

        colring_btn = Button(
            self.left_frame_overlay,
            text="الخروج",
            bd=0,
            bg=dark_black,
            fg=white,
            font=("", 15),
            command=self.exit1,
        )
        colring_btn.place(x=60, y=748)

    def employee_page(self):
        self.employee_frame = Frame(self.Upper_frame, bg=white, width=1285, height=700)
        self.employee_frame.place(x=0, y=1)

        frame_cover_label = Frame(
            self.Upper1_frame_show_data, bg=dark_grey, width=1285, height=40
        ).place(x=0, y=0)
        lbl_employee = Label(
            self.Upper1_frame_show_data,
            text="الموظفين",
            font=("Bold", 25),
            bg=dark_grey,
            fg=white,
        ).place(x=600, y=3)

        self.rightside_employee_frame = Frame(
            self.employee_frame, bg=dark_yellow, width=280, height=700
        )
        self.rightside_employee_frame.place(x=1003, y=1)

        txt_mowazfeen_lbl = Label(
            self.rightside_employee_frame,
            text="الموظفين",
            font=("Bold", 25),
            justify="right",
            bg=dark_yellow,
            fg=dark_black,
        )
        txt_mowazfeen_lbl.place(x=95, y=10)

        # add image in bottom

        logo_pic_main = Image.open(r"images\employee1_cuted.png")
        resized = logo_pic_main.resize((268, 200))
        logo_pic_mainB = ImageTk.PhotoImage(resized)
        logo_pic_main_A = Label(
            self.rightside_employee_frame, image=logo_pic_mainB, bg=dark_yellow
        )
        logo_pic_main_A.image = logo_pic_mainB
        logo_pic_main_A.place(x=4, y=480)

        # labels for the form fields

        name_label = Label(
            self.rightside_employee_frame,
            text="الأسم",
            font=10,
            bg=dark_yellow,
            fg=dark_black,
            justify="right",
        ).place(x=230, y=80)

        id_label = Label(
            self.rightside_employee_frame,
            text="الرقم القومي",
            font=10,
            bg=dark_yellow,
            fg=dark_black,
            justify="right",
        ).place(x=190, y=130)

        phone_label = Label(
            self.rightside_employee_frame,
            text="رقم الهاتف",
            font=10,
            bg=dark_yellow,
            fg=dark_black,
            justify="right",
        ).place(x=200, y=180)

        date_label = Label(
            self.rightside_employee_frame,
            text="تاريخ الميلاد",
            font=10,
            bg=dark_yellow,
            fg=dark_black,
            justify="right",
        ).place(x=190, y=230)

        days_label = Label(
            self.rightside_employee_frame,
            text=" D",
            bg=dark_yellow,
            fg=dark_black,
            justify="right",
        ).place(x=12, y=210)

        months_label = Label(
            self.rightside_employee_frame,
            text=" M",
            bg=dark_yellow,
            fg=dark_black,
            justify="right",
        ).place(x=72, y=210)

        years_label = Label(
            self.rightside_employee_frame,
            text="Y ",
            bg=dark_yellow,
            fg=dark_black,
            justify="right",
        ).place(x=139, y=210)

        jop_label = Label(
            self.rightside_employee_frame,
            text="التخصص",
            font=10,
            bg=dark_yellow,
            fg=dark_black,
            justify="right",
        ).place(x=210, y=280)

        gender_label = Label(
            self.rightside_employee_frame,
            text="النوع",
            font=10,
            bg=dark_yellow,
            fg=dark_black,
            justify="right",
        ).place(x=240, y=330)

        address_label = Label(
            self.rightside_employee_frame,
            text=": العنوان",
            font=10,
            bg=dark_yellow,
            fg=dark_black,
            justify="right",
        ).place(x=217, y=380)

        # add entries behind labels

        self.name_entry = Entry(
            self.rightside_employee_frame,
            textvariable=self.name,
            width=20,
            font=("ca-bold", 11),
            justify="right",
        )
        self.name_entry.place(x=10, y=83)

        self.id_entry = Entry(
            self.rightside_employee_frame,
            textvariable=self.id_number,
            width=20,
            font=("ca-bold", 11),
            justify="right",
        )
        self.id_entry.place(x=10, y=133)

        self.phone_entry = Entry(
            self.rightside_employee_frame,
            textvariable=self.phone,
            width=20,
            font=("ca-bold", 11),
            justify="right",
        )
        self.phone_entry.place(x=10, y=183)

        self.days_combobox = ttk.Combobox(
            self.rightside_employee_frame,
            textvariable=self.days,
            state="readonly",
            width=3,
            font=("ca-bold", 11),
            justify="right",
        )
        self.days_combobox["values"] = (
            "1",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
            "10",
            "11",
            "12",
            "13",
            "14",
            "15",
            "16",
            "17",
            "18",
            "19",
            "20",
            "21",
            "22",
            "23",
            "24",
            "25",
            "26",
            "27",
            "28",
            "29",
            "30",
            "31",
        )
        self.days_combobox.place(x=10, y=233)

        self.months_combobox = ttk.Combobox(
            self.rightside_employee_frame,
            textvariable=self.months,
            state="readonly",
            width=3,
            font=("ca-bold", 11),
            justify="right",
        )
        self.months_combobox["values"] = (
            "1",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
            "10",
            "11",
            "12",
        )
        self.months_combobox.place(x=70, y=233)

        self.year_entry = Entry(
            self.rightside_employee_frame,
            textvariable=self.years,
            width=4,
            font=("ca-bold", 11),
            justify="left",
        )
        self.year_entry.place(x=130, y=233)

        self.job_entry = Entry(
            self.rightside_employee_frame,
            textvariable=self.job,
            width=20,
            font=("ca-bold", 11),
            justify="right",
        )
        self.job_entry.place(x=10, y=283)

        self.gender_combobox = ttk.Combobox(
            self.rightside_employee_frame,
            state="readonly",
            width=18,
            textvariable=self.gender,
            font=("ca-bold", 11),
            justify="right",
        )
        self.gender_combobox["values"] = ("ذكر", "أنثي")
        self.gender_combobox.place(x=10, y=333)

        self.address_txt = Text(
            self.rightside_employee_frame, width=20, height=3, font=("ca-bold", 11)
        )
        self.address_txt.place(x=10, y=383)

        # add buttons for save , update , remove , clear

        self.save_btn = Button(
            self.rightside_employee_frame,
            font=("", 20),
            bg=blue,
            text="حفظ",
            justify="right",
            fg=white,
            bd=0,
            command=self.add_employee,
        )
        self.save_btn.place(x=10, y=450)

        self.delete_btn = Button(
            self.rightside_employee_frame,
            font=("", 20),
            bg=false_red,
            text="حذف",
            justify="right",
            fg=white,
            bd=0,
            command=self.delete_employees,
        )
        self.delete_btn.place(x=85, y=450)

        self.update_btn = Button(
            self.rightside_employee_frame,
            font=("", 20),
            bg=light_blue,
            text="تحديث",
            justify="right",
            fg=white,
            bd=0,
            command=self.update_employees,
        )
        self.update_btn.place(x=165, y=450)

        self.clear_btn = Button(
            self.rightside_employee_frame,
            font=("", 10),
            bg=false_red,
            text="C",
            justify="right",
            fg=white,
            bd=0,
            command=self.clear_employees,
        )
        self.clear_btn.place(x=263, y=0)

        # let's add the main page that display the list of data

        #  add the frame
        self.frame_list = Frame(self.employee_frame, bg=white)
        self.frame_list.place(x=0, y=0, width=1000, height=700)

        self.style = ttk.Style()
        self.style.configure(
            "mystyle.Treeview",
            font=("Calibri", 15),
            background="#D3D3D3",
            foreground="black",
            rowheight=25,
            fieldbackground="#D3D3D3",
        )
        self.style.configure(
            "mystyle.Treeview.Heading",
            font=("Calibri", 15),
        )

        self.tv = ttk.Treeview(
            self.frame_list,
            columns=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10),
            style="mystyle.Treeview",
        )
        # Reverse the order of column headings and their corresponding data
        self.tv.heading("10", text="العنوان")
        self.tv.column("10", width=250)

        self.tv.heading("9", text="النوع")
        self.tv.column("9", width=50)

        self.tv.heading("8", text="التخصص")
        self.tv.column("8", width=100)

        self.tv.heading("7", text="السنين")
        self.tv.column("7", width=50)

        self.tv.heading("6", text="الشهر")
        self.tv.column("6", width=40)

        self.tv.heading("5", text="اليوم")
        self.tv.column("5", width=40)

        self.tv.heading("4", text="رقم الهاتف")
        self.tv.column("4", width=100)

        self.tv.heading("3", text="رقم القومي")
        self.tv.column("3", width=200)

        self.tv.heading("2", text="الأسم")
        self.tv.column("2", width=100)

        self.tv.heading("1", text="الرقم التسلسلي")
        self.tv.column("1", width=100)

        self.tv["show"] = "headings"
        self.tv.bind("<ButtonRelease-1>", self.getdata_employees)
        self.tv.place(x=0, y=0, height=800)
        self.displayAll_employees()

    def show_selected_warehouse(self, event):
        selected_warehouse = self.name_combobox_add_warehouse.get()

        # Fetch data for the selected warehouse from the database
        warehouse_data = self.db.fetch_warehouse_by_name(selected_warehouse)

        # Populate the entry fields with the retrieved data
        if warehouse_data:
            self.officer_entry_add_warehouse2.delete(0, "end")
            # Assuming officer's name is at index 1 in the retrieved data
            self.officer_entry_add_warehouse2.insert(0, warehouse_data[1])
            self.phone_entry_add_warehouse2.delete(0, "end")
            # Assuming phone number is at index 2 in the retrieved data
            self.phone_entry_add_warehouse2.insert(0, warehouse_data[2])
            self.address_entry_add_warehouse2.delete(0, "end")
            # Assuming address is at index 3 in the retrieved data
            self.address_entry_add_warehouse2.insert(0, warehouse_data[3])

    def clear_warehouse_adding(self):
        self.name_entry_add_warehouse.delete(0, "end")
        self.address_entry_add_warehouse.delete(0, "end")
        self.officer_entry_add_warehouse.delete(0, "end")
        self.phone_entry_add_warehouse.delete(0, "end")

    def add_warehouse_db(self):
        if (
            self.name_entry_add_warehouse.get() == ""
            or self.phone_entry_add_warehouse.get() == ""
            or self.officer_entry_add_warehouse.get() == ""
            or self.address_entry_add_warehouse.get() == ""
        ):
            messagebox.showerror("ERROR", "من فضلك لا تترك حقل فارغ")
        else:
            id_warehouse = self.name_entry_add_warehouse.get()
            existing_warehouse = self.db.fetch_by_id_num_warehouse(id_warehouse)

            if existing_warehouse:
                messagebox.showerror("Error", "المخزن موجود بالفعل في قاعدة البيانات")
            else:
                self.db.insert_warehouse(
                    self.name_entry_add_warehouse.get(),
                    self.address_entry_add_warehouse.get(),
                    self.officer_entry_add_warehouse.get(),
                    self.phone_entry_add_warehouse.get(),
                )
                messagebox.showinfo(
                    "تم الحفظ بنجاح", "تم إضافة مخزن جديد إلى قاعدة البيانات"
                )
                self.populate_warehouse_combobox()
                self.clear_warehouse_adding()

    def clear_warehouse_ediding(self):
        self.name_combobox_add_warehouse.set("")
        self.address_entry_add_warehouse2.delete(
            0, "end"
        )  # Clear the content of the Entry
        self.address_entry_add_warehouse2.delete(0, "end")
        self.officer_entry_add_warehouse2.delete(0, "end")
        self.phone_entry_add_warehouse2.delete(0, "end")

    def update_warehouse_db(self):
        if (
            self.name_combobox_add_warehouse.get() == ""
            or self.phone_entry_add_warehouse2.get() == ""
            or self.officer_entry_add_warehouse2.get() == ""
            or self.address_entry_add_warehouse2.get() == ""
        ):
            messagebox.showerror("ERROR", "من فضلك لا تترك حقل فارغ")
        else:
            self.db.update_warehouse(
                self.name_combobox_add_warehouse.get(),
                self.name_combobox_add_warehouse.get(),
                self.address_entry_add_warehouse2.get(),
                self.officer_entry_add_warehouse2.get(),
                self.phone_entry_add_warehouse2.get(),
            )

            messagebox.showinfo("تحتديث البيانات", "تم تحديث البيانات")
            self.clear_warehouse_ediding()

    def delete_warehouse_db(self):
        if (
            self.name_combobox_add_warehouse.get() == ""
            or self.phone_entry_add_warehouse2.get() == ""
            or self.officer_entry_add_warehouse2.get() == ""
            or self.address_entry_add_warehouse2.get() == ""
        ):
            messagebox.showerror(
                "ERROR",
                " لا يمكن حذف بسبب عدم وجود بيانات في الجدول متشابه مع الخانات او الخانات فاضيه",
            )
        else:
            messagebox.showerror("تم الحذف", "تم حذف الموظف بنجاح")
            self.db.remove_warehouse(self.name_combobox_add_warehouse.get())
            self.clear_warehouse_ediding()
            self.populate_warehouse_combobox()

    def populate_warehouse_combobox(self):
        warehouses = self.db.fetch_warehouse()
        warehouse_names = [warehouse[0] for warehouse in warehouses]
        # Replace this with the actual attribute name of your combobox

        self.name_combobox_add_warehouse["values"] = warehouse_names

    def populate_warehouse_combobox_in_product(self):
        warehouses = self.db.fetch_warehouse()
        warehouse_names = [warehouse[0] for warehouse in warehouses]
        # Replace this with the actual attribute name of your combobox
        self.entry_warehouse_add_product["values"] = warehouse_names

    def warehouse_page(self):
        self.warehouse_frame = Frame(self.Upper_frame, bg=white, width=1285, height=700)
        self.warehouse_frame.place(x=0, y=1)

        frame_cover_label = Frame(
            self.Upper1_frame_show_data, bg=dark_grey, width=1285, height=40
        ).place(x=0, y=0)
        lbl_show_name = Label(
            self.Upper1_frame_show_data,
            text="  المخزن",
            font=("Bold", 25),
            bg=dark_grey,
            fg=white,
        ).place(x=600, y=3)

        self.btn_all_products = Button(
            self.warehouse_frame,
            text="جميع المنتجات",
            bd=0,
            bg=white,
            fg=dark_grey,
            font=("", 15),
        )
        self.btn_all_products.place(x=30, y=20)

        self.btn_add_warehouse = Button(
            self.warehouse_frame,
            text="أضافه مخزن ",
            bd=0,
            bg=white,
            fg=dark_grey,
            font=("", 15),
            command=self.add_warehouse,
        )
        self.btn_add_warehouse.place(x=180, y=20)

        self.btn_add_product = Button(
            self.warehouse_frame,
            text=" أضافه منتج",
            bd=0,
            bg=white,
            fg=dark_grey,
            font=("", 15),
            command=self.add_product,
        )
        self.btn_add_product.place(x=330, y=20)

        self.btn_edit_product = Button(
            self.warehouse_frame,
            text=" تعديل علي منتج",
            bd=0,
            bg=white,
            fg=dark_grey,
            font=("", 15),
            command=self.edit_product,
        )
        self.btn_edit_product.place(x=480, y=20)

        self.btn_from_to = Button(
            self.warehouse_frame,
            text=" أذن تحويل",
            bd=0,
            bg=white,
            fg=dark_grey,
            font=("", 15),
            command=self.change_warehouse_product,
        )
        self.btn_from_to.place(x=630, y=20)

        # add frame to cut the page
        frame_cut_page = Frame(
            self.warehouse_frame, width=1200, height=2, bg=whitey
        ).place(x=30, y=75)

    def add_warehouse(self):
        self.add_warehouse_frame = Frame(
            self.warehouse_frame, bg=white, width=1285, height=600
        )
        self.add_warehouse_frame.place(x=0, y=77)

        self.frame1_add_warehouse = Frame(
            self.add_warehouse_frame, bg=whitey, width=550, height=300
        )
        self.frame1_add_warehouse.place(x=40, y=20)

        self.frame2_add_warehouse = Frame(
            self.add_warehouse_frame, bg=whitey, width=550, height=300
        )
        self.frame2_add_warehouse.place(x=670, y=20)

        logo_pic_main = Image.open(r"images\8615007.jpg")
        resized = logo_pic_main.resize((1200, 300))
        logo_pic_mainB = ImageTk.PhotoImage(resized)
        logo_pic_main_A = Label(
            self.add_warehouse_frame, image=logo_pic_mainB, bg=white
        )
        logo_pic_main_A.image = logo_pic_mainB
        logo_pic_main_A.place(x=20, y=300)

        # add images before labels

        logo_pic_main = Image.open(r"images\icons8-warehouse-48.png")
        resized = logo_pic_main.resize((30, 30))
        logo_pic_mainB = ImageTk.PhotoImage(resized)
        logo_pic_main_A = Label(
            self.frame1_add_warehouse, image=logo_pic_mainB, bg=whitey
        )
        logo_pic_main_A.image = logo_pic_mainB
        logo_pic_main_A.place(x=510, y=25)

        logo_pic_main = Image.open(r"images\icons8-address-48.png")
        resized = logo_pic_main.resize((30, 30))
        logo_pic_mainB = ImageTk.PhotoImage(resized)
        logo_pic_main_A = Label(
            self.frame1_add_warehouse, image=logo_pic_mainB, bg=whitey
        )
        logo_pic_main_A.image = logo_pic_mainB
        logo_pic_main_A.place(x=510, y=70)

        logo_pic_main = Image.open(r"images\icons8-person-48.png")
        resized = logo_pic_main.resize((30, 30))
        logo_pic_mainB = ImageTk.PhotoImage(resized)
        logo_pic_main_A = Label(
            self.frame1_add_warehouse, image=logo_pic_mainB, bg=whitey
        )
        logo_pic_main_A.image = logo_pic_mainB
        logo_pic_main_A.place(x=510, y=125)

        logo_pic_main = Image.open(r"images\icons8-phone-100.png")
        resized = logo_pic_main.resize((30, 30))
        logo_pic_mainB = ImageTk.PhotoImage(resized)
        logo_pic_main_A = Label(
            self.frame1_add_warehouse, image=logo_pic_mainB, bg=whitey
        )
        logo_pic_main_A.image = logo_pic_mainB
        logo_pic_main_A.place(x=510, y=175)

        # add_labels

        lbl_warehouse_name = Label(
            self.frame1_add_warehouse,
            text="أسم المخزن ",
            bg=whitey,
            fg=dark_black,
            font=("", 15, "bold"),
        )
        lbl_warehouse_name.place(x=410, y=30)

        lbl_warehouse_address = Label(
            self.frame1_add_warehouse,
            text="عنوان المخزن ",
            bg=whitey,
            fg=dark_black,
            font=("", 15, "bold"),
        )
        lbl_warehouse_address.place(x=400, y=80)

        lbl_warehouse_officer = Label(
            self.frame1_add_warehouse,
            text="أسم مسؤل المخازن ",
            bg=whitey,
            fg=dark_black,
            font=("", 15, "bold"),
        )
        lbl_warehouse_officer.place(x=370, y=130)

        lbl_warehouse_phone = Label(
            self.frame1_add_warehouse,
            text="رقم الهاتف  ",
            bg=whitey,
            fg=dark_black,
            font=("", 15, "bold"),
        )
        lbl_warehouse_phone.place(x=420, y=180)

        # add entrys

        self.name_entry_add_warehouse = Entry(
            self.frame1_add_warehouse, width=35, font=("ca-bold", 11), justify="right"
        )
        self.name_entry_add_warehouse.place(x=20, y=33)

        self.address_entry_add_warehouse = Entry(
            self.frame1_add_warehouse, width=35, font=("ca-bold", 11), justify="right"
        )
        self.address_entry_add_warehouse.place(x=20, y=87)

        self.officer_entry_add_warehouse = Entry(
            self.frame1_add_warehouse, width=35, font=("ca-bold", 11), justify="right"
        )
        self.officer_entry_add_warehouse.place(x=20, y=141)

        self.phone_entry_add_warehouse = Entry(
            self.frame1_add_warehouse, width=35, font=("ca-bold", 11), justify="right"
        )
        self.phone_entry_add_warehouse.place(x=20, y=190)

        # add buttons

        self.btn_add_warehouse = Button(
            self.frame1_add_warehouse,
            bg=green_fa23,
            fg=white,
            text="أضافه المخزن",
            font=("Arial", 15, "bold"),
            bd=0,
            command=self.add_warehouse_db,
        )
        self.btn_add_warehouse.place(x=225, y=230)

        # ------------------------------------------------------ edit (2) ------------------------------------------------

        # add images before labels

        logo_pic_main = Image.open(r"images\icons8-warehouse-48.png")
        resized = logo_pic_main.resize((30, 30))
        logo_pic_mainB = ImageTk.PhotoImage(resized)
        logo_pic_main_A = Label(
            self.frame2_add_warehouse, image=logo_pic_mainB, bg=whitey
        )
        logo_pic_main_A.image = logo_pic_mainB
        logo_pic_main_A.place(x=510, y=25)

        logo_pic_main = Image.open(r"images\icons8-address-48.png")
        resized = logo_pic_main.resize((30, 30))
        logo_pic_mainB = ImageTk.PhotoImage(resized)
        logo_pic_main_A = Label(
            self.frame2_add_warehouse, image=logo_pic_mainB, bg=whitey
        )
        logo_pic_main_A.image = logo_pic_mainB
        logo_pic_main_A.place(x=510, y=70)

        logo_pic_main = Image.open(r"images\icons8-person-48.png")
        resized = logo_pic_main.resize((30, 30))
        logo_pic_mainB = ImageTk.PhotoImage(resized)
        logo_pic_main_A = Label(
            self.frame2_add_warehouse, image=logo_pic_mainB, bg=whitey
        )
        logo_pic_main_A.image = logo_pic_mainB
        logo_pic_main_A.place(x=510, y=125)

        logo_pic_main = Image.open(r"images\icons8-phone-100.png")
        resized = logo_pic_main.resize((30, 30))
        logo_pic_mainB = ImageTk.PhotoImage(resized)
        logo_pic_main_A = Label(
            self.frame2_add_warehouse, image=logo_pic_mainB, bg=whitey
        )
        logo_pic_main_A.image = logo_pic_mainB
        logo_pic_main_A.place(x=510, y=175)

        # add_labels

        lbl_warehouse_name = Label(
            self.frame2_add_warehouse,
            text="أسم المخزن ",
            bg=whitey,
            fg=dark_black,
            font=("", 15, "bold"),
        )
        lbl_warehouse_name.place(x=410, y=30)

        lbl_warehouse_address = Label(
            self.frame2_add_warehouse,
            text="عنوان المخزن ",
            bg=whitey,
            fg=dark_black,
            font=("", 15, "bold"),
        )
        lbl_warehouse_address.place(x=400, y=80)

        lbl_warehouse_officer = Label(
            self.frame2_add_warehouse,
            text="أسم مسؤل المخازن ",
            bg=whitey,
            fg=dark_black,
            font=("", 15, "bold"),
        )
        lbl_warehouse_officer.place(x=370, y=130)

        lbl_warehouse_phone = Label(
            self.frame2_add_warehouse,
            text="رقم الهاتف  ",
            bg=whitey,
            fg=dark_black,
            font=("", 15, "bold"),
        )
        lbl_warehouse_phone.place(x=420, y=180)

        # add entrys

        # self.name_entry_add_warehouse = Entry(self.frame2_add_warehouse, width=35, font=(
        #     'ca-bold', 11), justify='right')
        # self.name_entry_add_warehouse.place(x=50, y=43)

        self.name_combobox_add_warehouse = ttk.Combobox(
            self.frame2_add_warehouse,
            state="readonly",
            width=35,
            font=("ca-bold", 11),
            justify="right",
        )
        self.name_combobox_add_warehouse.place(x=20, y=33)

        self.officer_entry_add_warehouse2 = Entry(
            self.frame2_add_warehouse, width=35, font=("ca-bold", 11), justify="right"
        )
        self.officer_entry_add_warehouse2.place(x=20, y=87)

        self.phone_entry_add_warehouse2 = Entry(
            self.frame2_add_warehouse, width=35, font=("ca-bold", 11), justify="right"
        )
        self.phone_entry_add_warehouse2.place(x=20, y=141)

        self.address_entry_add_warehouse2 = Entry(
            self.frame2_add_warehouse, width=35, font=("ca-bold", 11), justify="right"
        )
        self.address_entry_add_warehouse2.place(x=20, y=190)

        self.btn_edit_warehouse = Button(
            self.frame2_add_warehouse,
            bg=light_blue,
            fg=white,
            text="تعديل و حفظ",
            font=("Arial", 15, "bold"),
            bd=0,
            command=self.update_warehouse_db,
        )
        self.btn_edit_warehouse.place(x=180, y=230)

        self.btn_delete_warehouse = Button(
            self.frame2_add_warehouse,
            bg=false_red,
            fg=white,
            text="حذف المخزن",
            font=("Arial", 15, "bold"),
            bd=0,
            command=self.delete_warehouse_db,
        )
        self.btn_delete_warehouse.place(x=325, y=230)

        self.populate_warehouse_combobox()
        self.name_combobox_add_warehouse.bind(
            "<<ComboboxSelected>>", self.show_selected_warehouse
        )

    def clear_form_product(self):
        self.entry_name_add_product.delete(0, "end")
        self.entry_code_add_product.delete(0, "end")
        self.entry_warehouse_add_product.set("")
        self.entry_kind_add_product.delete(0, "end")
        self.entry_department_add_product.set("")
        self.entry_color_add_product.delete(0, "end")
        self.days_combobox_add_product.set("يوم")
        self.months_combobox_add_product.set("شهر")
        self.year_entry_add_product.delete(0, "end")
        self.year_entry_add_product.insert(0, "سنه")
        self.days_combobox_add_product2.set("يوم")
        self.months_combobox_add_product2.set("شهر")
        self.year_entry_add_product2.delete(0, "end")
        self.year_entry_add_product2.insert(0, "سنه")
        self.entry_quantity_add_product.delete(1, "end")
        self.entry_quantity_type_add_product.delete(0, "end")
        self.entry_quantity_type_add_product.set("متر")
        self.combobox_size_add_product.delete(0, "end")
        self.entry_price_add_product.delete(0, "end")
        self.txtbox_description_add_product.delete("1.0", END)
        self.txtbox_comment_add_product.delete("1.0", END)

    def insert_data_to_db_add_product(self):
        if (
            self.entry_kind_add_product.get() == ""
            or self.entry_warehouse_add_product.get() == ""
            or self.entry_code_add_product.get() == ""
            or self.entry_name_add_product.get() == ""
            or self.entry_quantity_add_product.get() == ""
            or self.entry_department_add_product.get() == ""
            or self.entry_quantity_type_add_product.get() == "----------"
        ):
            messagebox.showerror("ERROR", "من فضلك لا تترك حقل فارغ")
        else:
            product_id_num = self.entry_code_add_product.get()
            existing_employee = self.db.fetch_add_product_by_id(product_id_num)

            if existing_employee:
                messagebox.showerror("Error", "المنتج موجود بالفعل في قاعدة البيانات")
            else:
                result = messagebox.askyesno("تأكيد", "هل انت متأكد")
                if result:
                    self.db.insert_add_product(
                        self.entry_name_add_product.get(),
                        self.entry_code_add_product.get(),
                        self.entry_warehouse_add_product.get(),
                        self.entry_kind_add_product.get(),
                        self.entry_department_add_product.get(),
                        self.entry_color_add_product.get(),
                        self.days_combobox_add_product.get(),
                        self.months_combobox_add_product.get(),
                        self.year_entry_add_product.get(),
                        self.days_combobox_add_product2.get(),
                        self.months_combobox_add_product2.get(),
                        self.year_entry_add_product2.get(),
                        self.entry_quantity_add_product.get(),
                        self.entry_quantity_type_add_product.get(),
                        self.combobox_size_add_product.get(),
                        self.entry_price_add_product.get(),
                        self.txtbox_description_add_product.get(1.0, END),
                        self.txtbox_comment_add_product.get(1.0, END),
                    )
                    messagebox.showinfo(
                        "تم الحفظ بنجاح", "تم إضافة منتج جديد إلى قاعدة البيانات"
                    )

                    self.clear_form_product()

    def validate_input(self, P):
        if P == "" or P == "." or P.replace(".", "", 1).isdigit():
            return True
        else:
            return False

    def poplute_size(self):
        product_name = self.db.fetch_size()
        product_names = [size[1] for size in product_name]
        # Replace this with the actual attribute name of your combobox

        self.combobox_size_add_product["values"] = product_names

    def add_product(self):
        # frames
        self.add_product_frame = Frame(
            self.warehouse_frame, bg=white, width=1285, height=600
        )
        self.add_product_frame.place(x=0, y=77)

        self.add_product_form = Frame(
            self.add_product_frame, bg=whitey, width=1200, height=550
        )
        self.add_product_form.place(x=30, y=20)

        frame_quantity = LabelFrame(
            self.add_product_form,
            background=whitey,
            width=400,
            height=100,
            text="الكميه",
            relief=tk.SOLID,
            borderwidth=0.6,
        ).place(x=400, y=115)

        # to make some fildes dont recieve any type exept numbers and . only
        validate_input_cmd = self.add_product_form.register(self.validate_input)

        # labels for form fields

        lbl_name = Label(
            self.add_product_form,
            text="*الأسم",
            font=("Arial", 15, "bold"),
            bg=whitey,
            fg=black,
            justify="right",
        ).place(x=1120, y=20)
        lbl_code = Label(
            self.add_product_form,
            text="*الكود",
            font=("Arial", 15, "bold"),
            bg=whitey,
            fg=black,
        ).place(x=920, y=20)
        lbl_warehouse = Label(
            self.add_product_form,
            text="*المخزن",
            font=("Arial", 15, "bold"),
            bg=whitey,
            fg=black,
        ).place(x=720, y=20)
        lbl_kind = Label(
            self.add_product_form,
            text="*النوع",
            font=("Arial", 15, "bold"),
            bg=whitey,
            fg=black,
        ).place(x=520, y=20)
        lbl_department = Label(
            self.add_product_form,
            text="*القسم",
            font=("Arial", 15, "bold"),
            bg=whitey,
            fg=black,
        ).place(x=320, y=20)
        lbl_color = Label(
            self.add_product_form,
            text="اللون",
            font=("Arial", 15, "bold"),
            bg=whitey,
            fg=black,
        ).place(x=120, y=20)
        lbl_date_enter = Label(
            self.add_product_form,
            text="التاريخ",
            font=("Arial", 15, "bold"),
            bg=whitey,
            fg=black,
        ).place(x=1120, y=130)
        lbl_expire_date = Label(
            self.add_product_form,
            text="انتهاء التاريخ",
            font=("Arial", 15, "bold"),
            bg=whitey,
            fg=black,
        ).place(x=880, y=130)
        lbl_Quantity = Label(
            self.add_product_form,
            text="*العدد",
            font=("Arial", 15, "bold"),
            bg=whitey,
            fg=black,
            justify="right",
        ).place(x=720, y=130)
        lbl_Quantity_type = Label(
            self.add_product_form,
            text="*وحده العدد",
            font=("Arial", 15, "bold"),
            bg=whitey,
            fg=black,
        ).place(x=520, y=130)
        lbl_weight = Label(
            self.add_product_form,
            text="المقاس",
            font=("Arial", 15, "bold"),
            bg=whitey,
            fg=black,
        ).place(x=270, y=130)
        lbl_price = Label(
            self.add_product_form,
            text="السعر",
            font=("Arial", 15, "bold"),
            bg=whitey,
            fg=black,
        ).place(x=120, y=130)
        lbl_discription = Label(
            self.add_product_form,
            text=": الوصف",
            font=("Arial", 15, "bold"),
            bg=whitey,
            fg=black,
        ).place(x=1120, y=280)
        lbl_comments = Label(
            self.add_product_form,
            text=": ملاحظات",
            font=("Arial", 15, "bold"),
            bg=whitey,
            fg=black,
        ).place(x=720, y=280)

        # add entry to product page

        self.entry_name_add_product = ttk.Entry(
            self.add_product_form, width=15, font=("Arial", 15, "bold"), justify="right"
        )
        self.entry_name_add_product.place(x=1000, y=55)

        self.entry_code_add_product = ttk.Entry(
            self.add_product_form, width=15, font=("Arial", 15, "bold"), justify="right"
        )
        self.entry_code_add_product.place(x=800, y=55)

        self.entry_warehouse_add_product = ttk.Combobox(
            self.add_product_form,
            width=14,
            font=("Arial", 15, "bold"),
            justify="right",
            state="readonly",
        )
        self.entry_warehouse_add_product.place(x=600, y=55)

        self.entry_kind_add_product = ttk.Entry(
            self.add_product_form, width=15, font=("Arial", 15, "bold"), justify="right"
        )
        self.entry_kind_add_product.place(x=400, y=55)

        self.entry_department_add_product = ttk.Combobox(
            self.add_product_form,
            width=14,
            state="readonly",
            font=("ca-bold", 15),
            justify="right",
        )
        self.entry_department_add_product.place(x=200, y=55)

        # department things
        self.entry_department_add_product["values"] = (
            "قماش",
            "اكسسوار",
            "بنطلون",
            "قميص",
            "تيشرت",
            "ماكينات",
            "أخري",
        )

        self.entry_color_add_product = ttk.Entry(
            self.add_product_form, width=15, font=("Arial", 15, "bold"), justify="right"
        )
        self.entry_color_add_product.place(x=10, y=55)

        # taree5 el 2ntag
        self.days_combobox_add_product = ttk.Combobox(
            self.add_product_form,
            state="readonly",
            width=3,
            font=("ca-bold", 11),
            justify="right",
        )
        self.days_combobox_add_product["values"] = (
            "1",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
            "10",
            "11",
            "12",
            "13",
            "14",
            "15",
            "16",
            "17",
            "18",
            "19",
            "20",
            "21",
            "22",
            "23",
            "24",
            "25",
            "26",
            "27",
            "28",
            "29",
            "30",
            "31",
        )
        self.days_combobox_add_product.place(x=1010, y=175)

        self.months_combobox_add_product = ttk.Combobox(
            self.add_product_form,
            state="readonly",
            width=3,
            font=("ca-bold", 11),
            justify="right",
        )
        self.months_combobox_add_product["values"] = (
            "1",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
            "10",
            "11",
            "12",
        )
        self.months_combobox_add_product.place(x=1070, y=175)

        self.year_entry_add_product = ttk.Entry(
            self.add_product_form,
            width=4,
            font=("ca-bold", 11),
            justify="left",
            validate="key",
            validatecommand=(validate_input_cmd, "%P"),
        )
        self.year_entry_add_product.place(x=1130, y=175)

        # taree5 el 2nthaa2

        self.days_combobox_add_product2 = ttk.Combobox(
            self.add_product_form,
            state="readonly",
            width=3,
            font=("ca-bold", 11),
            justify="right",
        )
        self.days_combobox_add_product2["values"] = (
            "1",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
            "10",
            "11",
            "12",
            "13",
            "14",
            "15",
            "16",
            "17",
            "18",
            "19",
            "20",
            "21",
            "22",
            "23",
            "24",
            "25",
            "26",
            "27",
            "28",
            "29",
            "30",
            "31",
        )
        self.days_combobox_add_product2.place(x=810, y=175)

        self.months_combobox_add_product2 = ttk.Combobox(
            self.add_product_form,
            state="readonly",
            width=3,
            font=("ca-bold", 11),
            justify="right",
        )
        self.months_combobox_add_product2["values"] = (
            "1",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
            "10",
            "11",
            "12",
        )
        self.months_combobox_add_product2.place(x=870, y=175)

        self.year_entry_add_product2 = ttk.Entry(
            self.add_product_form,
            width=4,
            font=("ca-bold", 11),
            justify="left",
            validate="key",
            validatecommand=(validate_input_cmd, "%P"),
        )
        self.year_entry_add_product2.place(x=930, y=175)

        self.entry_quantity_add_product = Spinbox(
            self.add_product_form,
            width=7,
            font=("Arial", 15, "bold"),
            justify="center",
            from_=0,
            to=99999,
            validate="key",
            validatecommand=(validate_input_cmd, "%P"),
        )
        self.entry_quantity_add_product.place(x=680, y=175)

        self.entry_quantity_type_add_product = ttk.Combobox(
            self.add_product_form, width=13, font=("Arial", 15, "bold"), justify="right"
        )
        self.entry_quantity_type_add_product.place(x=430, y=175)

        # quantity type things

        self.entry_quantity_type_add_product.set("متر")
        self.entry_quantity_type_add_product["values"] = (
            "ملي متر",
            "سنتيمتر",
            "متر",
            "كيلومتر",
            "----------",
            "قطعه",
            "دسته",
            "----------",
            "ميلي جرام",
            "جرام",
            "كيلو",
            "طن",
            "----------",
            "طوب",
        )

        # end

        self.combobox_size_add_product = ttk.Combobox(
            self.add_product_form,
            width=14,
            state="readonly",
            font=("ca-bold", 15),
            justify="right",
        )
        self.combobox_size_add_product.place(x=200, y=175)

        self.entry_price_add_product = ttk.Entry(
            self.add_product_form,
            width=15,
            font=("Arial", 15, "bold"),
            justify="right",
            validate="key",
            validatecommand=(validate_input_cmd, "%P"),
        )
        self.entry_price_add_product.place(x=10, y=175)

        # text box
        self.txtbox_description_add_product = Text(
            self.add_product_form, width=30, height=10, font=("ca-bold", 11), bd=0
        )
        self.txtbox_description_add_product.place(x=850, y=290)

        self.txtbox_comment_add_product = Text(
            self.add_product_form, width=30, height=10, font=("ca-bold", 11), bd=0
        )
        self.txtbox_comment_add_product.place(x=450, y=290)

        # add Button

        self.btn_add_product = tk.Button(
            self.add_product_form,
            bg=light_blue,
            fg=white,
            relief="flat",
            text="أضافه المنتج",
            font=("Arial", 15, "bold"),
            bd=1,
            command=self.insert_data_to_db_add_product,
        )
        self.btn_add_product.place(x=20, y=500)

        self.btn_clear_product = tk.Button(
            self.add_product_form,
            bg=false_red,
            fg=white,
            relief="flat",
            text="أخلاء الخانات",
            font=("Arial", 15, "bold"),
            bd=1,
            command=self.clear_form_product,
        )
        self.btn_clear_product.place(x=150, y=500)

        #  add image

        logo_pic_main = Image.open(r"images\icons8-product-100.png")
        resized = logo_pic_main.resize((250, 200))
        logo_pic_mainB = ImageTk.PhotoImage(resized)
        logo_pic_main_A = Label(self.add_product_form, image=logo_pic_mainB, bg=whitey)
        logo_pic_main_A.image = logo_pic_mainB
        logo_pic_main_A.place(x=80, y=250)

        self.entry_warehouse_add_product.bind(
            "<<ComboboxSelected>>", self.show_selected_warehouse
        )
        self.populate_warehouse_combobox_in_product()
        self.poplute_size()

        # edit some stuff
        self.days_combobox_add_product.set("يوم")
        self.months_combobox_add_product.set("شهر")

        self.year_entry_add_product.insert(0, "2023")
        self.days_combobox_add_product2.set("يوم")
        self.months_combobox_add_product2.set("شهر")

        self.year_entry_add_product2.insert(0, "2024")

    def populate_product_name_combobox(self):
        product_name = self.db.fetch_add_product()
        product_names = [add_product[0] for add_product in product_name]
        # Replace this with the actual attribute name of your combobox

        self.combobox_name_product["values"] = product_names

    def populate_product_name_combobox_in_product(self):
        product_name = self.db.fetch_add_product()
        product_names = [add_product[0] for add_product in product_name]
        # Replace this with the actual attribute name of your combobox
        self.combobox_name_product["values"] = product_names

    def populate_product_id_combobox(self):
        product_name = self.db.fetch_add_product()
        product_names = [add_product[1] for add_product in product_name]
        # Replace this with the actual attribute name of your combobox

        self.combobox_id_product["values"] = product_names

    def populate_product_id_combobox_in_product(self):
        product_name = self.db.fetch_add_product()
        product_names = [add_product[1] for add_product in product_name]
        # Replace this with the actual attribute name of your combobox
        self.combobox_id_product["values"] = product_names

    def delete_edit_product(self):
        try:
            result = messagebox.askyesno("تأكيد", "هل انت متأكد")
            if result:
                messagebox.showerror("تم الحذف", "تم حذف المنتج بنجاح")
                self.db.remove_product(self.entry_id_edit_product.get())
                self.clear_edit_values()

        except Exception as e:
            # Handle the exception here (e.g., print an error message)
            print("An error occurred:", e)

    def show_by_name_product(self):
        try:
            selected_product = self.combobox_name_product.get()

            # Fetch data for the selected warehouse from the database
            product_data_name = self.db.fetch_add_product_by_name(selected_product)

            # Populate the entry fields with the retrieved data
            if product_data_name:
                self.frame_3azel.destroy()
                self.entry_name_edit_product.delete(0, "end")
                self.entry_name_edit_product.insert(0, product_data_name[0])

                self.entry_id_edit_product.delete(0, "end")
                self.entry_id_edit_product.configure(state="normal")
                self.entry_id_edit_product.delete(0, "end")
                self.entry_id_edit_product.insert(0, product_data_name[1])
                self.entry_id_edit_product.configure(state="readonly")

                self.entry_warehouse_edit_product.delete(0, "end")
                self.entry_warehouse_edit_product.configure(state="normal")
                self.entry_warehouse_edit_product.delete(0, "end")
                self.entry_warehouse_edit_product.insert(0, product_data_name[2])
                self.entry_warehouse_edit_product.configure(state="readonly")

                self.entry_kind_edit_product.delete(0, "end")
                self.entry_kind_edit_product.insert(0, product_data_name[3])

                self.entry_department_edit_product.delete(0, "end")
                self.entry_department_edit_product.insert(0, product_data_name[4])

                self.entry_color_edit_product.delete(0, "end")
                self.entry_color_edit_product.insert(0, product_data_name[5])

                self.entry_weight_edit_product.delete(0, "end")
                self.entry_weight_edit_product.insert(0, product_data_name[-4])

                self.entry_price_edit_product.delete(0, "end")
                self.entry_price_edit_product.insert(0, product_data_name[-3])

                self.combobox_name_product.set("الاسم")

            else:
                messagebox.showerror(
                    "An error occurred",
                    "لا تترك الحقل فاضي او كلمه الأسم ظاهره من فضلك اختار ",
                )
        except Exception as e:
            # Handle the exception here (e.g., print an error message)
            print("An error occurred:", e)

    def show_by_id_product(self):
        try:
            selected_product = self.combobox_id_product.get()

            # Fetch data for the selected warehouse from the database
            product_data_name = self.db.fetch_add_product_by_id(selected_product)

            # Populate the entry fields with the retrieved data
            if product_data_name:
                self.frame_3azel.destroy()

                self.entry_name_edit_product.delete(0, "end")
                self.entry_name_edit_product.insert(0, product_data_name[0])

                self.entry_id_edit_product.delete(0, "end")
                self.entry_id_edit_product.configure(state="normal")
                self.entry_id_edit_product.delete(0, "end")
                self.entry_id_edit_product.insert(0, product_data_name[1])
                self.entry_id_edit_product.configure(state="readonly")

                self.entry_warehouse_edit_product.delete(0, "end")
                self.entry_warehouse_edit_product.configure(state="normal")
                self.entry_warehouse_edit_product.delete(0, "end")
                self.entry_warehouse_edit_product.insert(0, product_data_name[2])
                self.entry_warehouse_edit_product.configure(state="readonly")

                self.entry_kind_edit_product.delete(0, "end")
                self.entry_kind_edit_product.insert(0, product_data_name[3])

                self.entry_department_edit_product.delete(0, "end")
                self.entry_department_edit_product.insert(0, product_data_name[4])

                self.entry_color_edit_product.delete(0, "end")
                self.entry_color_edit_product.insert(0, product_data_name[5])

                self.entry_weight_edit_product.delete(0, "end")
                self.entry_weight_edit_product.insert(0, product_data_name[-4])

                self.entry_price_edit_product.delete(0, "end")
                self.entry_price_edit_product.insert(0, product_data_name[-3])

                self.combobox_id_product.set("كود")

            else:
                messagebox.showerror(
                    "An error occurred",
                    "لا تترك الحقل فاضي او كلمه كود ظاهره من فضلك اختار ",
                )
        except Exception as e:
            # Handle the exception here (e.g., print an error message)
            print("An error occurred:", e)

    def clear_edit_values(self):
        self.entry_name_edit_product.delete(0, "end")

        self.entry_id_edit_product.config(state="normal")
        self.entry_id_edit_product.delete(0, "end")
        self.entry_id_edit_product.config(state="readonly")

        self.entry_warehouse_edit_product.config(state="normal")
        self.entry_warehouse_edit_product.delete(0, "end")
        self.entry_warehouse_edit_product.config(state="readonly")

        self.entry_kind_edit_product.delete(0, "end")

        self.entry_department_edit_product.delete(0, "end")

        self.entry_color_edit_product.delete(0, "end")

        self.entry_weight_edit_product.delete(0, "end")

        self.entry_price_edit_product.delete(0, "end")

        self.combobox_id_product.set("كود")
        self.combobox_name_product.set("الاسم")

    def update_product_from_edit(self):
        if (
            self.entry_id_edit_product.get() == ""
            or self.entry_name_edit_product.get() == ""
            or self.entry_warehouse_edit_product.get() == ""
        ):
            messagebox.showerror("ERROR", "من فضلك لا تترك حقل فارغ")
        else:
            result = messagebox.askyesno("تأكيد", "هل انت متأكد")
            if result:
                self.db.update_add_product(
                    self.entry_id_edit_product.get(),
                    self.entry_name_edit_product.get(),
                    self.entry_id_edit_product.get(),
                    self.entry_warehouse_edit_product.get(),
                    self.entry_kind_edit_product.get(),
                    self.entry_department_edit_product.get(),
                    self.entry_color_edit_product.get(),
                    self.entry_weight_edit_product.get(),
                    self.entry_price_edit_product.get(),
                )

                messagebox.showinfo("تحتديث البيانات", "تم تحديث البيانات")
                self.clear_edit_values()

    def edit_product(self):
        # frames
        self.edit_product_frame = Frame(
            self.warehouse_frame, bg=white, width=1285, height=600
        )
        self.edit_product_frame.place(x=0, y=77)

        self.frame1_edit_product_frame = Frame(
            self.edit_product_frame, bg=whitey, width=360, height=550
        )
        self.frame1_edit_product_frame.place(x=40, y=20)

        self.frame2_edit_product_frame = Frame(
            self.edit_product_frame, bg=whitey, width=360, height=550
        )
        self.frame2_edit_product_frame.place(x=455, y=20)

        self.frame3_edit_product_frame = Frame(
            self.edit_product_frame, bg=whitey, width=360, height=550
        )
        self.frame3_edit_product_frame.place(x=870, y=20)

        # search BY NAME :

        lbl_name = Label(
            self.frame1_edit_product_frame,
            text="بحث بالأسم",
            font=("Arial", 15, "bold"),
            bg=whitey,
            fg=black,
            justify="right",
        ).place(x=150, y=20)

        logo_pic_main = Image.open(r"images\icons8-aliexpress-48.png")
        resized = logo_pic_main.resize((30, 30))
        logo_pic_mainB = ImageTk.PhotoImage(resized)
        logo_pic_main_A = Label(
            self.frame1_edit_product_frame, image=logo_pic_mainB, bg=whitey
        )
        logo_pic_main_A.image = logo_pic_mainB
        logo_pic_main_A.place(x=230, y=18)

        self.combobox_name_product = ttk.Combobox(
            self.frame1_edit_product_frame,
            width=25,
            font=("Arial", 15, "bold"),
            justify="right",
            state="readonly",
        )
        self.combobox_name_product.place(x=25, y=100)
        self.combobox_name_product.set("الاسم")

        self.btn_editbyname = tk.Button(
            self.frame1_edit_product_frame,
            text="بحث ثم التعديل",
            bg=blue,
            fg=white,
            relief="flat",
            font=(
                "Arial",
                15,
            ),
            bd=0,
            command=self.show_by_name_product,
        )

        self.btn_editbyname.place(x=120, y=200)

        logo_pic_main = Image.open(r"images\icons8-product-94.png")
        resized = logo_pic_main.resize((200, 200))
        logo_pic_mainB = ImageTk.PhotoImage(resized)
        logo_pic_main_A = Label(
            self.frame1_edit_product_frame, image=logo_pic_mainB, bg=whitey
        )
        logo_pic_main_A.image = logo_pic_mainB
        logo_pic_main_A.place(x=80, y=340)

        # search BY id :

        lbl_name = Label(
            self.frame2_edit_product_frame,
            text="بحث بالكود",
            font=("Arial", 15, "bold"),
            bg=whitey,
            fg=black,
            justify="right",
        ).place(x=150, y=20)

        logo_pic_main = Image.open(r"images\icons8-add-48.png")
        resized = logo_pic_main.resize((30, 30))
        logo_pic_mainB = ImageTk.PhotoImage(resized)
        logo_pic_main_A = Label(
            self.frame2_edit_product_frame, image=logo_pic_mainB, bg=whitey
        )
        logo_pic_main_A.image = logo_pic_mainB
        logo_pic_main_A.place(x=230, y=18)

        self.combobox_id_product = ttk.Combobox(
            self.frame2_edit_product_frame,
            width=25,
            font=("Arial", 15, "bold"),
            justify="right",
            state="readonly",
        )
        self.combobox_id_product.place(x=25, y=100)
        self.combobox_id_product.set("كود")

        self.btn_editbyid = tk.Button(
            self.frame2_edit_product_frame,
            text="بحث ثم التعديل",
            bg=blue,
            fg=white,
            relief="flat",
            font=(
                "Arial",
                15,
            ),
            bd=0,
            command=self.show_by_id_product,
        )

        self.btn_editbyid.place(x=120, y=200)

        logo_pic_main = Image.open(r"images\icons8-product-96.png")
        resized = logo_pic_main.resize((200, 200))
        logo_pic_mainB = ImageTk.PhotoImage(resized)
        logo_pic_main_A = Label(
            self.frame2_edit_product_frame, image=logo_pic_mainB, bg=whitey
        )
        logo_pic_main_A.image = logo_pic_mainB
        logo_pic_main_A.place(x=60, y=340)

        self.populate_product_id_combobox_in_product()
        self.populate_product_name_combobox_in_product()

        # ---------------------------------

        # edit values for product:

        lbl_name = Label(
            self.frame3_edit_product_frame,
            text="تعديل منتج ",
            font=("Arial", 15, "bold"),
            bg=whitey,
            fg=black,
            justify="right",
        ).place(x=150, y=20)

        logo_pic_main = Image.open(r"images\icons8-edit-48.png")
        resized = logo_pic_main.resize((30, 30))
        logo_pic_mainB = ImageTk.PhotoImage(resized)
        logo_pic_main_A = Label(
            self.frame3_edit_product_frame, image=logo_pic_mainB, bg=whitey
        )
        logo_pic_main_A.image = logo_pic_mainB
        logo_pic_main_A.place(x=230, y=18)

        self.entry_name_edit_product = ttk.Entry(
            self.frame3_edit_product_frame,
            width=15,
            font=("Arial", 15, "bold"),
            justify="right",
        )
        self.entry_name_edit_product.place(x=5, y=100)

        self.entry_id_edit_product = ttk.Entry(
            self.frame3_edit_product_frame,
            width=15,
            state="readonly",
            font=("Arial", 15, "bold"),
            justify="right",
        )
        self.entry_id_edit_product.place(x=185, y=100)

        self.entry_warehouse_edit_product = ttk.Entry(
            self.frame3_edit_product_frame,
            width=15,
            font=("Arial", 15, "bold"),
            justify="right",
        )
        self.entry_warehouse_edit_product.config(state="readonly")
        self.entry_warehouse_edit_product.place(x=5, y=200)

        self.entry_kind_edit_product = ttk.Entry(
            self.frame3_edit_product_frame,
            width=15,
            font=("Arial", 15, "bold"),
            justify="right",
        )
        self.entry_kind_edit_product.place(x=185, y=200)

        self.entry_department_edit_product = ttk.Entry(
            self.frame3_edit_product_frame,
            width=15,
            font=("Arial", 15, "bold"),
            justify="right",
        )
        self.entry_department_edit_product.place(x=5, y=300)

        self.entry_color_edit_product = ttk.Entry(
            self.frame3_edit_product_frame,
            width=15,
            font=("Arial", 15, "bold"),
            justify="right",
        )
        self.entry_color_edit_product.place(x=185, y=300)

        self.entry_weight_edit_product = ttk.Entry(
            self.frame3_edit_product_frame,
            width=15,
            font=("Arial", 15, "bold"),
            justify="right",
        )
        self.entry_weight_edit_product.place(x=5, y=400)

        self.entry_price_edit_product = ttk.Entry(
            self.frame3_edit_product_frame,
            width=15,
            font=("Arial", 15, "bold"),
            justify="right",
        )
        self.entry_price_edit_product.place(x=185, y=400)

        # add labels in part 3 for entries
        lbl_id = Label(
            self.frame3_edit_product_frame,
            text="*الكود",
            font=("Arial", 15, "bold"),
            bg=whitey,
            fg=black,
            justify="right",
        ).place(x=300, y=60)
        lbl_name = Label(
            self.frame3_edit_product_frame,
            text="*الأسم",
            font=("Arial", 15, "bold"),
            bg=whitey,
            fg=black,
            justify="right",
        ).place(x=128, y=60)
        lbl_kind = Label(
            self.frame3_edit_product_frame,
            text="النوع",
            font=("Arial", 15, "bold"),
            bg=whitey,
            fg=black,
            justify="right",
        ).place(x=300, y=160)
        lbl_warehouse = Label(
            self.frame3_edit_product_frame,
            text="المخزن",
            font=("Arial", 15, "bold"),
            bg=whitey,
            fg=black,
            justify="right",
        ).place(x=128, y=160)
        lbl_color = Label(
            self.frame3_edit_product_frame,
            text="اللون",
            font=("Arial", 15, "bold"),
            bg=whitey,
            fg=black,
            justify="right",
        ).place(x=300, y=260)
        lbl_department = Label(
            self.frame3_edit_product_frame,
            text="القسم",
            font=("Arial", 15, "bold"),
            bg=whitey,
            fg=black,
            justify="right",
        ).place(x=128, y=260)

        lbl_price = Label(
            self.frame3_edit_product_frame,
            text="السعر",
            font=("Arial", 15, "bold"),
            bg=whitey,
            fg=black,
            justify="right",
        ).place(x=300, y=360)
        lbl_weight = Label(
            self.frame3_edit_product_frame,
            text="المقاس",
            font=("Arial", 15, "bold"),
            bg=whitey,
            fg=black,
            justify="right",
        ).place(x=128, y=360)

        self.btn_save = tk.Button(
            self.frame3_edit_product_frame,
            text="حفظ و تعديل",
            bg=blue,
            fg=white,
            relief="flat",
            font=(
                "Arial",
                15,
            ),
            bd=0,
            command=self.update_product_from_edit,
        )

        self.btn_save.place(x=100, y=500)

        self.btn_delete_product = tk.Button(
            self.frame3_edit_product_frame,
            text="حذف",
            bg=false_red,
            fg=white,
            relief="flat",
            font=(
                "Arial",
                15,
            ),
            bd=0,
            command=self.delete_edit_product,
        )

        self.btn_delete_product.place(x=300, y=500)

        self.frame_3azel = Frame(
            self.frame3_edit_product_frame, width=600, height=600, bg=white
        )
        self.frame_3azel.place(x=0, y=0)

    def poplute_warehouse(self):
        product_name = self.db.fetch_add_product_change()
        product_names = [add_product[0] for add_product in product_name]
        # Replace this with the actual attribute name of your combobox
        self.combobox_warehouse_change_1["values"] = product_names

    def update_product_combobox(self, event):
        selected_warehouse = self.combobox_warehouse_change_1.get()

        # Fetch products related to the selected warehouse from your database
        related_products = self.db.fetch_values_for_column(selected_warehouse)

        # Extract product names from the fetched data
        product_names = [product[0] for product in related_products]

        # Update the values in self.combobox_product_change_1
        self.combobox_product_change_1["values"] = product_names

    def show_quantity(self):
        name = self.combobox_product_change_1.get()
        product_quantity = self.db.fetch_values_for_change_quantity(name)

        if isinstance(product_quantity, int):
            # Handle the case where product_quantity is an integer (e.g., quantity)
            quantity = product_quantity
            quantity_type = "0"  # Set to an empty string or another default value

        elif isinstance(product_quantity, tuple) and len(product_quantity) == 2:
            # Assuming product_quantity is a (quantity, quantity_type) tuple
            quantity, quantity_type = product_quantity
        else:
            # Handle other cases (e.g., product not found)
            quantity = 0
            quantity_type = "اختر منتج لمعرفه الكميه"  # Set to a default value

        display_text = f"الكميه: {quantity} {quantity_type}"

        # Update the self.txt_quantity_and_quantity_type widget with the fetched information
        self.txt_quantity_and_quantity_type.config(text=display_text)

    def change_warehouse_product(self):
        self.change_warehouse_frame = Frame(
            self.warehouse_frame, bg=white, width=1285, height=600
        )
        self.change_warehouse_frame.place(x=0, y=77)

        self.frame1_warehouse_change_frame = Frame(
            self.change_warehouse_frame, bg=whitey, width=360, height=550
        )
        self.frame1_warehouse_change_frame.place(x=40, y=20)

        self.frame2_warehouse_change_frame = Frame(
            self.change_warehouse_frame, bg=whitey, width=360, height=550
        )
        self.frame2_warehouse_change_frame.place(x=455, y=20)

        self.frame3_warehouse_change_frame = Frame(
            self.change_warehouse_frame, bg=whitey, width=360, height=550
        )
        self.frame3_warehouse_change_frame.place(x=870, y=20)

        self.frame_hide2 = Frame(
            self.frame2_warehouse_change_frame, bg=white, width=360, height=550
        )
        self.frame_hide2.place(x=0, y=0)

        self.frame_hide3 = Frame(
            self.frame3_warehouse_change_frame, bg=white, width=360, height=550
        )
        self.frame_hide3.place(x=0, y=0)

        self.combobox_warehouse_change_1 = ttk.Combobox(
            self.frame1_warehouse_change_frame,
            width=25,
            font=("Arial", 15, "bold"),
            justify="right",
            state="readonly",
        )
        self.combobox_warehouse_change_1.place(x=25, y=100)
        self.combobox_warehouse_change_1.set("المخزن")
        # Bind an event handler to the ComboboxSelected event of self.combobox_warehouse_change_1
        self.combobox_warehouse_change_1.bind(
            "<<ComboboxSelected>>", self.update_product_combobox
        )

        self.combobox_product_change_1 = ttk.Combobox(
            self.frame1_warehouse_change_frame,
            width=25,
            font=("Arial", 15, "bold"),
            justify="right",
            state="readonly",
        )
        self.combobox_product_change_1.place(x=25, y=150)
        self.combobox_product_change_1.set("المنتج")

        self.poplute_warehouse()
        self.txt_quantity_and_quantity_type = Label(
            self.frame1_warehouse_change_frame,
            font=("Arial", 15, "bold"),
            text="1",
            bg=whitey,
        )
        self.txt_quantity_and_quantity_type.place(x=130, y=200)
        self.combobox_warehouse_change_1.bind(
            "<<ComboboxSelected>>", self.update_product_combobox
        )
        self.combobox_product_change_1.bind(
            "<<ComboboxSelected>>", lambda event: self.show_quantity()
        )
        self.show_quantity()

        frame_for_buttons = Frame(self.frame1_warehouse_change_frame, bg=whitey)
        frame_for_buttons.place(x=50, y=250, width=250, height=400)

        btn_change_quantity = tk.Button(
            frame_for_buttons,
            text="تغير الكميه",
            highlightbackground=blue,
            cursor="hand2",
            background=blue,
            foreground=white,
            activebackground=white,
            activeforeground=blue,
            highlightthickness=2,
            highlightcolor=blue,
            width=13,
            height=2,
            border=0,
            font=("Arial", 16, "bold"),
            command=self.quantitysolve,
        )
        btn_change_quantity.place(x=45, y=10)

        btn_change_quantity = tk.Button(
            frame_for_buttons,
            text="تحويل المنتج بالكامل",
            highlightbackground=green_fa23,
            cursor="hand2",
            background=green_fa23,
            foreground=white,
            activebackground=white,
            activeforeground=green_fa23,
            highlightthickness=2,
            highlightcolor=green_fa23,
            width=13,
            height=2,
            border=0,
            font=("Arial", 16, "bold"),
        )
        btn_change_quantity.place(x=45, y=80)

        btn_change_quantity = tk.Button(
            frame_for_buttons,
            text="تحويل المنتج جزئي",
            highlightbackground=dark_yellow,
            cursor="hand2",
            background=dark_yellow,
            foreground=white,
            activebackground=white,
            activeforeground=dark_yellow,
            highlightthickness=2,
            highlightcolor=dark_yellow,
            width=13,
            height=2,
            border=0,
            font=("Arial", 16, "bold"),
        )
        btn_change_quantity.place(x=45, y=150)

        btn_change_quantity = tk.Button(
            frame_for_buttons,
            text="تفريغ الاختيارات",
            highlightbackground=false_red,
            cursor="hand2",
            background=false_red,
            foreground=white,
            activebackground=white,
            activeforeground=false_red,
            highlightthickness=2,
            highlightcolor=false_red,
            width=13,
            height=2,
            border=0,
            font=("Arial", 16, "bold"),
        )
        btn_change_quantity.place(x=45, y=220)

        logo_pic_main = Image.open(r"images\5631.jpg")
        resized = logo_pic_main.resize((400, 80))
        logo_pic_mainB = ImageTk.PhotoImage(resized)
        logo_pic_main_A = Label(
            self.frame1_warehouse_change_frame, image=logo_pic_mainB, bg=whitey
        )
        logo_pic_main_A.image = logo_pic_mainB
        logo_pic_main_A.place(x=-2, y=0)

    def save_quantity(self):
        q1 = self.new_quantity.get()
        qt1 = self.new_quantity_type.get()
        name = self.combobox_product_change_1.get()
        if name == "" or name == "المنتج" or q1 == "" or qt1 == "":
            messagebox.showerror("خطا", "لا تترك حقل فاضي")
        else:
            self.db.update_quantity(name, q1, qt1)
            messagebox.showinfo("تم بنجاح", "تم الحفظ بنجاح")

    def quantitysolve(self):
        name = self.combobox_product_change_1.get()
        if name == "" or name == "المنتج":
            messagebox.showerror("خطا", "لا تترك حقل فاضي")

        else:
            value1 = self.db.fetch_value_num(name)
            value2 = self.db.fetch_value_num_type(name)

            self.frame_hide2.config(bg=whitey)

            txt_quantity = Label(
                self.frame_hide2, font=("Arial", 15, "bold"), text=" : العدد", bg=whitey
            )
            txt_quantity.place(x=300, y=20)

            self.static_quantity = ttk.Entry(
                self.frame_hide2, width=6, font=("Arial", 15, "bold"), justify="right"
            )
            self.static_quantity.insert(0, value1)
            self.static_quantity.config(state="readonly")
            self.static_quantity.place(x=220, y=20)

            self.static_quantity_type = ttk.Entry(
                self.frame_hide2, width=12, font=("Arial", 15, "bold"), justify="right"
            )
            self.static_quantity_type.insert(0, value2)
            self.static_quantity_type.config(state="readonly")
            self.static_quantity_type.place(x=80, y=20)

            txt_quantity = Label(
                self.frame_hide2,
                font=("Arial", 15, "bold"),
                text=" : الجديد",
                bg=whitey,
            )
            txt_quantity.place(x=295, y=100)

            self.new_quantity = ttk.Entry(
                self.frame_hide2, width=6, font=("Arial", 15, "bold"), justify="right"
            )
            self.new_quantity.place(x=220, y=100)

            self.new_quantity_type = ttk.Combobox(
                self.frame_hide2, width=12, font=("Arial", 15, "bold"), justify="right"
            )
            self.new_quantity_type["values"] = (
                "ملي متر",
                "سنتيمتر",
                "متر",
                "كيلومتر",
                "----------",
                "قطعه",
                "دسته",
                "----------",
                "ميلي جرام",
                "جرام",
                "كيلو",
                "طن",
            )
            self.new_quantity_type.insert(0, value2)
            self.new_quantity_type.place(x=63, y=100)

            self.btn_save_new_quantity = tk.Button(
                self.frame_hide2,
                text="تعديل و حفظ",
                highlightbackground=blue,
                cursor="hand2",
                background=blue,
                foreground=white,
                activebackground=white,
                activeforeground=blue,
                highlightthickness=2,
                highlightcolor=blue,
                width=13,
                height=2,
                border=0,
                font=("Arial", 16, "bold"),
                command=self.save_quantity,
            )
            self.btn_save_new_quantity.place(x=95, y=220)

            logo_pic_main = Image.open(r"images\icons8-quantity-64.png")
            resized = logo_pic_main.resize((200, 200))
            logo_pic_mainB = ImageTk.PhotoImage(resized)
            logo_pic_main_A = Label(self.frame_hide2, image=logo_pic_mainB, bg=whitey)
            logo_pic_main_A.image = logo_pic_mainB
            logo_pic_main_A.place(x=75, y=330)

    def cutting_table(self):
        self.cutting_table_main_frame = Frame(
            self.Upper_frame, bg=white, width=1285, height=700
        )
        self.cutting_table_main_frame.place(x=0, y=1)

        self.cutting_table_pages = Frame(
            self.Upper_frame, bg=white, width=1285, height=600
        )
        self.cutting_table_pages.place(x=0, y=80)

        self.btn_all_data = Button(
            self.cutting_table_main_frame,
            text="جميع القصات",
            bd=0,
            bg=white,
            fg=dark_grey,
            font=("", 15),
        )
        self.btn_all_data.place(x=30, y=20)

        self.btn_create_model = Button(
            self.cutting_table_main_frame,
            text="أنشاء قصه",
            bd=0,
            bg=white,
            fg=dark_grey,
            font=("", 15),
            command=self.create_model,
        )
        self.btn_create_model.place(x=180, y=20)

        self.btn_add_data = Button(
            self.cutting_table_main_frame,
            text="أضافه بينات لقصه",
            bd=0,
            bg=white,
            fg=dark_grey,
            font=("", 15),
            command=self.add_to_model,
        )
        self.btn_add_data.place(x=330, y=20)

        self.btn_finsh_model = Button(
            self.cutting_table_main_frame,
            text="انتهاء من قصه",
            bd=0,
            bg=white,
            fg=dark_grey,
            font=("", 15),
            command=self.finish_model,
        )
        self.btn_finsh_model.place(x=480, y=20)

        # add frame to cut the page
        frame_cut_page = Frame(
            self.cutting_table_main_frame, width=1200, height=2, bg=whitey
        ).place(x=30, y=75)

    def create_model(self):
        self.main_create = Frame(
            self.cutting_table_pages, width=1285, height=600, bg=white
        )
        self.main_create.place(x=0, y=0)
        # dah el background 😉
        self.add_image(
            r"backgrounds\create_table.png", 1285, 600, 0, 0, self.main_create, white
        )

        self.code_model = ttk.Entry(
            self.main_create,
            width=10,
            font=("Arial", 15, "bold"),
        )
        self.code_model.place(x=950, y=130)

        self.employee_create_cutting = ttk.Combobox(
            self.main_create,
            state="readonly",
            width=14,
            font=("ca-bold", 14),
            justify="right",
        )
        self.employee_create_cutting.place(x=500, y=135)

        self.days_combobox_add_product = ttk.Combobox(
            self.main_create,
            state="readonly",
            width=3,
            font=("ca-bold", 11),
            justify="right",
        )
        self.days_combobox_add_product["values"] = (
            "1",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
            "10",
            "11",
            "12",
            "13",
            "14",
            "15",
            "16",
            "17",
            "18",
            "19",
            "20",
            "21",
            "22",
            "23",
            "24",
            "25",
            "26",
            "27",
            "28",
            "29",
            "30",
            "31",
        )
        self.days_combobox_add_product.place(x=210, y=135)

        self.months_combobox_add_product = ttk.Combobox(
            self.main_create,
            state="readonly",
            width=3,
            font=("ca-bold", 11),
            justify="right",
        )
        self.months_combobox_add_product["values"] = (
            "1",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
            "10",
            "11",
            "12",
        )
        self.months_combobox_add_product.place(x=270, y=135)

        self.year_entry_add_product = ttk.Entry(
            self.main_create,
            width=4,
            font=("ca-bold", 11),
            justify="left",
        )
        self.year_entry_add_product.place(x=330, y=135)

        self.code_model = ttk.Entry(
            self.main_create,
            width=10,
            font=("Arial", 15, "bold"),
        )
        self.code_model.place(x=950, y=275)

        self.code_model = ttk.Entry(
            self.main_create,
            width=10,
            font=("Arial", 15, "bold"),
        )
        self.code_model.place(x=540, y=275)

        self.employee_create_cutting = ttk.Combobox(
            self.main_create,
            state="readonly",
            width=14,
            font=("ca-bold", 14),
            justify="right",
        )
        self.employee_create_cutting.place(x=200, y=275)

        # add buttons

        self.btn_editbyid = tk.Button(
            self.main_create,
            text="حفظ",
            bg=blue_canva,
            fg=white,
            relief="flat",
            font=(
                "Arial",
                15,
            ),
            bd=0,
        )

        self.btn_editbyid.place(x=185, y=495)

    def add_to_model(self):
        self.main_add_to_model = Frame(
            self.cutting_table_pages, width=1285, height=600, bg=white
        )
        self.main_add_to_model.place(x=0, y=0)
        # dah el background 😉
        self.add_image(
            r"backgrounds\add_data_to_model.png",
            1285,
            600,
            0,
            0,
            self.main_add_to_model,
            white,
        )

    def finish_model(self):
        self.main_finish_model = Frame(
            self.cutting_table_pages, width=1285, height=600, bg=white
        )
        self.main_finish_model.place(x=0, y=0)
        # dah el background 😉
        self.add_image(
            r"backgrounds\finish_model_f1.png",
            1285,
            600,
            0,
            0,
            self.main_finish_model,
            white,
        )

        self.btn_next_to_finsh = Button(
            self.main_finish_model,
            bg=blue_fat7_canva,
            fg=white,
            text="التالي",
            font=("Arial", 15, "bold"),
            bd=0,
            command=self.finish_model_f2,
        )
        self.btn_next_to_finsh.place(x=1030, y=485)

    def finish_model_f2(self):
        self.main_finish_model_f2 = Frame(
            self.cutting_table_pages, width=1285, height=600, bg=white
        )
        self.main_finish_model_f2.place(x=0, y=0)
        # dah el background 😉
        self.add_image(
            r"backgrounds\finish_model_f2.png",
            1285,
            600,
            0,
            0,
            self.main_finish_model_f2,
            white,
        )

    def clear_add_partners(self):
        self.name_entry_add_partener.delete(0, "end")
        self.code_entry_add_partener.delete(0, "end")
        self.kind_service_combobox_add_partener.set("نوع الخدمه")
        self.phone_entry_add_partener.delete(0, "end")

    def partners(self):
        self.partner_main_frame = Frame(
            self.Upper_frame, bg=white, width=1285, height=700
        )
        self.partner_main_frame.place(x=0, y=1)

        self.partner_pages = Frame(self.Upper_frame, bg=white, width=1285, height=600)
        self.partner_pages.place(x=0, y=80)

        self.btn_all_partners = Button(
            self.partner_main_frame,
            text="جميع الصنايعيه",
            bd=0,
            bg=white,
            fg=dark_grey,
            font=("", 15),
        )
        self.btn_all_partners.place(x=30, y=20)

        self.btn_add_partners = Button(
            self.partner_main_frame,
            text="أضافه صنايعي ",
            bd=0,
            bg=white,
            fg=dark_grey,
            font=("", 15),
            command=self.add_partners,
        )
        self.btn_add_partners.place(x=180, y=20)

        self.btn_send_partner = Button(
            self.partner_main_frame,
            text=" ارسال للصنايعي",
            bd=0,
            bg=white,
            fg=dark_grey,
            font=("", 15),
            command=self.send_to_partener,
        )
        self.btn_send_partner.place(x=330, y=20)

        self.btn_recive_partner = Button(
            self.partner_main_frame,
            text=" استلام من صنايعي",
            bd=0,
            bg=white,
            fg=dark_grey,
            font=("", 15),
            command=self.recive_from_partner,
        )
        self.btn_recive_partner.place(x=480, y=20)

        self.btn_from_to = Button(
            self.partner_main_frame,
            text="تعديل بيانات صانيعي",
            bd=0,
            bg=white,
            fg=dark_grey,
            font=("", 15),
            command=self.edit_product,
        )
        self.btn_from_to.place(x=630, y=20)

        # add frame to cut the page
        frame_cut_page = Frame(
            self.partner_main_frame, width=1200, height=2, bg=whitey
        ).place(x=30, y=75)

    def populate_service_kind_combobox(self):
        product_name = self.db.fetch_service_change()
        product_names = [kind_service[1] for kind_service in product_name]
        # Replace this with the actual attribute name of your combobox
        self.kind_service_combobox_add_partener["values"] = product_names
        self.combo_partner_service_update["values"] = product_names

    def populate_id_add_partner_combobox(self):
        product_name = self.db.fetch_add_partner_all()
        product_names = [id_add_partner[0] for id_add_partner in product_name]
        # Replace this with the actual attribute name of your combobox
        self.combo_partner_code_update["values"] = product_names

    def show_selected_add_partner(self, event):
        selected_partner = self.combo_partner_code_update.get()
        partner_data = self.db.fetch_by_id_add_partner(selected_partner)

        if partner_data:
            self.Entry_partner_name_update.delete(0, "end")
            self.Entry_partner_name_update.insert(0, partner_data[1])

            if hasattr(self.combo_partner_service_update, "set"):
                self.combo_partner_service_update.set(partner_data[2])

            self.Entry_partner_phone_update.delete(0, "end")
            self.Entry_partner_phone_update.insert(0, partner_data[3])
        else:
            print("Partner data not found.")
            print(selected_partner)

    def clear_edit_partners(self):
        self.combo_partner_code_update.set("")
        self.Entry_partner_name_update.delete(0, "end")
        self.combo_partner_service_update.set("")
        self.Entry_partner_phone_update.delete(0, "end")

    def update_add_partners(self):
        try:
            if (
                self.Entry_partner_name_update.get() == ""
                or self.combo_partner_service_update.get() == ""
                or self.Entry_partner_phone_update.get() == ""
                or self.combo_partner_code_update.get() == ""
            ):
                messagebox.showerror("ERROR", "من فضلك لا تترك حقل فارغ")
            else:
                result = messagebox.askyesno("تأكيد", "هل انت متأكد")
                if result:
                    self.db.update_add_partner(
                        self.combo_partner_code_update.get(),
                        self.Entry_partner_name_update.get(),
                        self.combo_partner_service_update.get(),
                        self.Entry_partner_phone_update.get(),
                    )

                    messagebox.showinfo("تحتديث البيانات", "تم تحديث البيانات")
                    self.clear_edit_partners()
                else:
                    print("error")
        except Exception as e:
            # Handle the exception here (e.g., print an error message)
            print("An error occurred:", e)

    def remove_partner(self):
        try:
            if (
                self.combo_partner_code_update.get() == ""
                or self.Entry_partner_name_update.get() == ""
                or self.combo_partner_service_update.get() == ""
                or self.Entry_partner_phone_update.get() == ""
            ):
                messagebox.showerror("ERROR", "من فضلك لا تترك حقل فارغ")
            else:
                result = messagebox.askyesno("تأكيد", "هل انت متأكد")
                if result:
                    messagebox.showerror("تم الحذف", "تم حذف المنتج بنجاح")
                    self.db.remove_add_partner(self.Entry_partner_name_update.get())
                    self.clear_edit_partners()
                    self.populate_id_add_partner_combobox()

        except Exception as e:
            # Handle the exception here (e.g., print an error message)
            print("An error occurred:", e)

    def add_partner_db_insert(self):
        if (
            self.name_entry_add_partener.get() == ""
            or self.code_entry_add_partener.get() == ""
            or self.kind_service_combobox_add_partener.get() == ""
            or self.phone_entry_add_partener.get() == ""
        ):
            messagebox.showerror("ERROR", "من فضلك لا تترك حقل فارغ")
        else:
            id_warehouse = self.code_entry_add_partener.get()
            existing_warehouse = self.db.fetch_by_id_add_partner(id_warehouse)

            if existing_warehouse:
                messagebox.showerror("Error", "الصنايعي موجود بالفعل في قاعدة البيانات")
            else:
                self.db.insert_add_partner(
                    self.name_entry_add_partener.get(),
                    self.code_entry_add_partener.get(),
                    self.kind_service_combobox_add_partener.get(),
                    self.phone_entry_add_partener.get(),
                )
                messagebox.showinfo(
                    "تم الحفظ بنجاح", "تم إضافة صنايعي جديد إلى قاعدة البيانات"
                )
                self.clear_add_partners()
                self.populate_service_kind_combobox()
                self.populate_id_add_partner_combobox()

    def add_partners(self):
        self.add_partener_frame = Frame(
            self.partner_pages, width=1285, height=600, bg=white
        )
        self.add_partener_frame.place(x=0, y=0)

        self.frame1_add_partener = Frame(
            self.add_partener_frame, bg=whitey, width=550, height=300
        )
        self.frame1_add_partener.place(x=40, y=20)

        self.frame2_add_partener = Frame(
            self.add_partener_frame, bg=whitey, width=550, height=300
        )
        self.frame2_add_partener.place(x=670, y=20)

        # --------------------- 1 ------------------

        lbl_partener_name = Label(
            self.frame1_add_partener,
            text="أسم الصنايعي ",
            bg=whitey,
            fg=dark_black,
            font=("", 15, "bold"),
        )
        lbl_partener_name.place(x=410, y=30)

        lbl_partener_address = Label(
            self.frame1_add_partener,
            text="كود الصنايعي ",
            bg=whitey,
            fg=dark_black,
            font=("", 15, "bold"),
        )
        lbl_partener_address.place(x=400, y=80)

        lbl_partener_officer = Label(
            self.frame1_add_partener,
            text="نوع الخدمه",
            bg=whitey,
            fg=dark_black,
            font=("", 15, "bold"),
        )
        lbl_partener_officer.place(x=420, y=130)

        lbl_partener_phone = Label(
            self.frame1_add_partener,
            text="رقم الهاتف  ",
            bg=whitey,
            fg=dark_black,
            font=("", 15, "bold"),
        )
        lbl_partener_phone.place(x=420, y=180)

        # add entrys

        self.name_entry_add_partener = Entry(
            self.frame1_add_partener, width=35, font=("ca-bold", 11), justify="right"
        )
        self.name_entry_add_partener.place(x=20, y=33)

        self.code_entry_add_partener = Entry(
            self.frame1_add_partener, width=35, font=("ca-bold", 11), justify="right"
        )
        self.code_entry_add_partener.place(x=20, y=87)

        self.kind_service_combobox_add_partener = ttk.Combobox(
            self.frame1_add_partener,
            state="readonly",
            width=29,
            font=("ca-bold", 12),
            justify="right",
        )
        self.kind_service_combobox_add_partener.place(x=20, y=138)

        self.phone_entry_add_partener = Entry(
            self.frame1_add_partener, width=35, font=("ca-bold", 11), justify="right"
        )
        self.phone_entry_add_partener.place(x=20, y=190)

        # add buttons

        self.btn_add_partener = Button(
            self.frame1_add_partener,
            bg=green_fa23,
            fg=white,
            text="أضافه صنايعي",
            font=("Arial", 15, "bold"),
            bd=0,
            command=self.add_partner_db_insert,
        )
        self.btn_add_partener.place(x=225, y=230)

        # -----------------------2-------------------------
        lbl_partner_id_update = Label(
            self.frame2_add_partener,
            text="الكود",
            bg=whitey,
            fg=dark_black,
            font=("", 15, "bold"),
        )
        lbl_partner_id_update.place(x=420, y=30)

        lbl_partner_name_update = Label(
            self.frame2_add_partener,
            text=" الأسم ",
            bg=whitey,
            fg=dark_black,
            font=("", 15, "bold"),
        )
        lbl_partner_name_update.place(x=420, y=80)

        lbl_partner_service_update = Label(
            self.frame2_add_partener,
            text="نوع الخدمه",
            bg=whitey,
            fg=dark_black,
            font=("", 15, "bold"),
        )
        lbl_partner_service_update.place(x=420, y=130)

        lbl_partner_phone_update = Label(
            self.frame2_add_partener,
            text="رقم الهاتف  ",
            bg=whitey,
            fg=dark_black,
            font=("", 15, "bold"),
        )
        lbl_partner_phone_update.place(x=420, y=180)

        # add entrys

        self.combo_partner_code_update = ttk.Combobox(
            self.frame2_add_partener,
            state="readonly",
            width=29,
            font=("ca-bold", 12),
            justify="right",
        )
        self.combo_partner_code_update.place(x=20, y=33)

        self.Entry_partner_name_update = Entry(
            self.frame2_add_partener, width=35, font=("ca-bold", 11), justify="right"
        )
        self.Entry_partner_name_update.place(x=20, y=87)

        self.combo_partner_service_update = ttk.Combobox(
            self.frame2_add_partener,
            state="readonly",
            width=29,
            font=("ca-bold", 12),
            justify="right",
        )
        self.combo_partner_service_update.place(x=20, y=141)

        self.Entry_partner_phone_update = Entry(
            self.frame2_add_partener, width=35, font=("ca-bold", 11), justify="right"
        )
        self.Entry_partner_phone_update.place(x=20, y=190)

        self.btn_edit_partner = Button(
            self.frame2_add_partener,
            bg=light_blue,
            fg=white,
            text="تعديل و حفظ",
            font=("Arial", 15, "bold"),
            bd=0,
            command=self.update_add_partners,
        )
        self.btn_edit_partner.place(x=180, y=230)

        self.btn_delete_partner = Button(
            self.frame2_add_partener,
            bg=false_red,
            fg=white,
            text="حذف الصنايعي",
            font=("Arial", 15, "bold"),
            bd=0,
            command=self.remove_partner,
        )
        self.btn_delete_partner.place(x=325, y=230)

        self.add_image(
            r"images\rag-doll-with-checklist-others-with-briefcase.jpg",
            1300,
            400,
            0,
            300,
            self.add_partener_frame,
            cl=white,
        )
        self.kind_service_combobox_add_partener.set("نوع الخدمه")
        self.combo_partner_code_update.bind(
            "<<ComboboxSelected>>", self.show_selected_add_partner
        )

        self.populate_service_kind_combobox()
        self.populate_id_add_partner_combobox()

    def poplute_name_of_products_and_size(self):
        product_name = self.db.fetch_add_product()
        size_name = self.db.fetch_size()
        partner_names = self.db.fetch_add_partner_all()
        product_names = [id_add_partner[0] for id_add_partner in product_name]
        # Replace this with the actual attribute name of your combobox
        self.name_of_product["values"] = product_names

        product_names_size = [size[1] for size in size_name]
        # Replace this with the actual attribute name of your combobox

        self.size_of_send["values"] = product_names_size

        partner_name_loop = [partner[1] for partner in partner_names]
        # Replace this with the actual attribute name of your combobox

        self.name_of_partner["values"] = partner_name_loop

    def send_to_partener_insert(self):
        if (
            self.quantity_of_send.get() == ""
            or self.code_of_send.get() == ""
            or self.name_of_product.get() == ""
            or self.name_of_partner.get() == ""
        ):
            messagebox.showerror("ERROR", "من فضلك لا تترك حقل فارغ")
        else:
            id_warehouse = self.code_of_send.get()
            # TODO: make function for this in db.py
            existing_warehouse = self.db.fetch_by_id_send_partner(id_warehouse)

            if existing_warehouse:
                messagebox.showerror(
                    "Error", "هذا المنتج موجود بالفعل في قاعدة البيانات"
                )
            else:
                product_name = self.name_of_product.get()
                product_quantity = int(self.quantity_of_send.get())

                productdata = self.db.fetch_add_product_by_name(product_name)

                quantity_of_product_in_add_product = productdata[12]
                quantity_type_of_product_in_add_product = productdata[13]
                new_quantity = quantity_of_product_in_add_product - product_quantity

                if new_quantity < 0:
                    messagebox.showerror(
                        "Error",
                        "لا يوجد مخزون كفايه مخزونك : "
                        + str(quantity_of_product_in_add_product)
                        + (quantity_type_of_product_in_add_product),
                    )

                else:
                    self.db.update_add_product_just_quantity(new_quantity, product_name)

                    self.db.insert_send_partner(
                        self.name_of_partner.get(),
                        self.name_of_product.get(),
                        self.code_of_send.get(),
                        self.quantity_of_send.get(),
                        self.size_of_send.get(),
                        self.days_combobox_date_partner.get(),
                        self.months_combobox_date_partner.get(),
                        self.year_entry_date_partner.get(),
                        self.txtbox_comment_send_partner.get("1.0", "end"),
                    )

                    self.db.insert_send_partner_copy(
                        self.name_of_partner.get(),
                        self.name_of_product.get(),
                        self.code_of_send.get(),
                        self.quantity_of_send.get(),
                        self.size_of_send.get(),
                        self.days_combobox_date_partner.get(),
                        self.months_combobox_date_partner.get(),
                        self.year_entry_date_partner.get(),
                        self.txtbox_comment_send_partner.get("1.0", "end"),
                    )
                    messagebox.showinfo("تم الحفظ بنجاح", "تم إرسال المنتج  بنجاح ")

                    self.poplute_name_of_products_and_size()

    def send_to_partener(self):
        self.send_partener_frame = Frame(
            self.partner_pages, width=1285, height=600, bg=white
        )
        self.send_partener_frame.place(x=0, y=0)

        self.add_image(
            r"images\background.png", 1285, 600, 0, -10, self.send_partener_frame, white
        )

        self.frame_send_options = Frame(
            self.send_partener_frame, width=300, height=500, bg=whitey
        )
        self.frame_send_options.place(x=520, y=80)

        # labels for send to partners

        lbl_name_partner = Label(
            self.frame_send_options,
            text="*أسم الصنايعي",
            font=("Arial", 15, "bold"),
            bg=whitey,
            fg=black,
        ).place(x=200, y=20)

        lbl_name_product = Label(
            self.frame_send_options,
            text="*أسم المنتج",
            font=("Arial", 15, "bold"),
            bg=whitey,
            fg=black,
            justify="right",
        ).place(x=200, y=70)

        lbl_code = Label(
            self.frame_send_options,
            text="*الكود",
            font=("Arial", 15, "bold"),
            bg=whitey,
            fg=black,
            justify="right",
        ).place(x=200, y=120)

        lbl_quantity = Label(
            self.frame_send_options,
            text="*العدد",
            font=("Arial", 15, "bold"),
            bg=whitey,
            fg=black,
            justify="right",
        ).place(x=200, y=170)

        lbl_sizes = Label(
            self.frame_send_options,
            text="المقاس",
            font=("Arial", 15, "bold"),
            bg=whitey,
            fg=black,
            justify="right",
        ).place(x=200, y=220)

        lbl_date = Label(
            self.frame_send_options,
            text="التاريخ",
            font=("Arial", 15, "bold"),
            bg=whitey,
            fg=black,
            justify="right",
        ).place(x=200, y=270)

        lbl_comments = Label(
            self.frame_send_options,
            text="ملاحظات",
            font=("Arial", 15, "bold"),
            bg=whitey,
            fg=black,
            justify="right",
        ).place(x=200, y=320)

        # add entries for send \
        self.name_of_partner = ttk.Combobox(
            self.frame_send_options,
            state="readonly",
            width=14,
            font=("ca-bold", 15),
            justify="right",
        )
        self.name_of_partner.place(x=20, y=20)

        self.name_of_product = ttk.Combobox(
            self.frame_send_options,
            state="readonly",
            width=14,
            font=("ca-bold", 15),
            justify="right",
        )
        self.name_of_product.place(x=20, y=70)

        self.code_of_send = ttk.Entry(
            self.frame_send_options,
            width=15,
            font=("Arial", 15, "bold"),
            justify="right",
        )
        self.code_of_send.place(x=20, y=120)

        self.quantity_of_send = ttk.Entry(
            self.frame_send_options,
            width=15,
            font=("Arial", 15, "bold"),
            justify="right",
        )
        self.quantity_of_send.place(x=20, y=170)

        self.size_of_send = ttk.Combobox(
            self.frame_send_options,
            state="readonly",
            width=14,
            font=("ca-bold", 15),
            justify="right",
        )
        self.size_of_send.place(x=20, y=220)

        self.days_combobox_date_partner = ttk.Combobox(
            self.frame_send_options,
            state="readonly",
            width=3,
            font=("ca-bold", 11),
            justify="right",
        )

        self.days_combobox_date_partner["values"] = (
            "1",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
            "10",
            "11",
            "12",
            "13",
            "14",
            "15",
            "16",
            "17",
            "18",
            "19",
            "20",
            "21",
            "22",
            "23",
            "24",
            "25",
            "26",
            "27",
            "28",
            "29",
            "30",
            "31",
        )
        self.days_combobox_date_partner.place(x=40, y=270)

        self.months_combobox_date_partner = ttk.Combobox(
            self.frame_send_options,
            state="readonly",
            width=3,
            font=("ca-bold", 11),
            justify="right",
        )
        self.months_combobox_date_partner["values"] = (
            "1",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
            "10",
            "11",
            "12",
        )
        self.months_combobox_date_partner.place(x=90, y=270)

        self.year_entry_date_partner = ttk.Entry(
            self.frame_send_options,
            width=5,
            font=("ca-bold", 11),
            justify="left",
        )
        self.year_entry_date_partner.place(x=140, y=270)

        self.add_image(
            r"images\buttonblue.png", 200, 200, 50, 350, self.frame_send_options, whitey
        )

        self.txtbox_comment_send_partner = Text(
            self.frame_send_options, width=20, height=4, font=("ca-bold", 11), bd=0
        )
        self.txtbox_comment_send_partner.place(x=20, y=320)

        self.btn_editbyid = tk.Button(
            self.frame_send_options,
            text="حفظ",
            bg=blue,
            fg=white,
            relief="flat",
            font=(
                "Arial",
                15,
            ),
            bd=0,
            command=self.send_to_partener_insert,
        )

        self.btn_editbyid.place(x=135, y=435)

        # btns for the lft side

        self.btn_all_send_data = tk.Button(
            self.send_partener_frame,
            text="جميع بيانات الأرسال",
            highlightbackground=blue,
            cursor="hand2",
            background=blue,
            foreground=white,
            activebackground=white,
            activeforeground=blue,
            highlightthickness=2,
            highlightcolor=blue,
            width=30,
            height=5,
            border=0,
            font=("Arial", 16, "bold"),
        )
        self.btn_all_send_data.place(x=860, y=40)

        self.btn_edit_send_data = tk.Button(
            self.send_partener_frame,
            text="تعديل علي البينات",
            highlightbackground=blue,
            cursor="hand2",
            background=blue,
            foreground=white,
            activebackground=white,
            activeforeground=blue,
            highlightthickness=2,
            highlightcolor=blue,
            width=30,
            height=5,
            border=0,
            font=("Arial", 16, "bold"),
        )
        self.btn_edit_send_data.place(x=860, y=240)

        self.btn_add_partner = tk.Button(
            self.send_partener_frame,
            text="أضافه صنايعي",
            highlightbackground=blue,
            cursor="hand2",
            background=blue,
            foreground=white,
            activebackground=white,
            activeforeground=blue,
            highlightthickness=2,
            highlightcolor=blue,
            width=30,
            height=5,
            border=0,
            font=("Arial", 16, "bold"),
            command=self.add_partners,
        )
        self.btn_add_partner.place(x=860, y=440)

        self.poplute_name_of_products_and_size()

    def poplute_partner_warehouse_code_recive(self):
        # Fetch all partner names from the database
        partner_names = self.db.fetch_add_partner_all()

        # Extract partner names from the fetched data
        partner_name_loop = [partner[1] for partner in partner_names]

        # Replace this with the actual attribute name of your combobox
        self.name_of_partner_recive["values"] = partner_name_loop

        # Fetch all partner names from the database
        warehouse = self.db.fetch_warehouse()

        # Extract partner names from the fetched data
        warehouse_loop = [partner[0] for partner in warehouse]

        # Replace this with the actual attribute name of your combobox
        self.warehouse_of_partner_recive["values"] = warehouse_loop

    def poplute_id(self, event):
        selected_warehouse = self.name_of_partner_recive.get()

        # Fetch products related to the selected warehouse from your database
        related_products = self.db.fetch_values_for_recive_columns(selected_warehouse)

        # Extract product names from the fetched data
        product_names = [product[0] for product in related_products]

        # Update the values in self.combobox_product_change_1
        self.code_of_partner_recive["values"] = product_names

    def receive_from_partener_insert(self):
        if (
            self.name_of_partner_recive.get() == ""
            or self.code_of_partner_recive.get() == ""
            or self.quantity_of_recive.get() == ""
            or self.warehouse_of_partner_recive.get() == ""
        ):
            messagebox.showerror("ERROR", "من فضلك لا تترك حقل فارغ")
        else:
            id_warehouse = self.code_of_partner_recive.get()

            existing_warehouse = self.db.fetch_by_id_receiver_partner(id_warehouse)

            if existing_warehouse:
                messagebox.showerror(
                    "Error", "هذا المنتج موجود بالفعل في قاعدة البيانات"
                )
            else:
                code = self.code_of_partner_recive.get()
                send_data = self.db.fetch_by_id_send_partner(code)
                product_name = send_data[3]
                real_quantity = int(send_data[4])
                past_comments = send_data[8]
                size = send_data[2]
                old_y = send_data[5]
                old_m = send_data[6]
                old_d = send_data[7]
                old_real_year = int(send_data[9])
                old_real_month = int(send_data[10])
                old_real_day = int(send_data[11])
                old_real_hour = int(send_data[12])
                old_real_minute = int(send_data[13])

                current_quantity = int(self.quantity_of_recive.get())
                warehouse = self.warehouse_of_partner_recive.get()
                partner_name = self.name_of_partner_recive.get()
                forget = self.quantity_of_recive_proplem.get()
                current_year_unreal = self.year_entry_date_partner_recive.get()
                current_month_unreal = self.months_combobox_date_partner_recive.get()
                current_day_unreal = self.days_combobox_date_partner_recive.get()
                new_comments = self.txtbox_comment_recive_partner.get("1.0", "end")

                current_year = int(self.now.year)
                current_month = int(self.now.month)
                current_day = int(self.now.day)
                current_hour = int(self.now.hour)
                current_minute = int(self.now.minute)

                # time operation

                total_year = int(current_year - old_real_year)
                total_month = int(current_month - old_real_month)
                total_days = int(current_day - old_real_day)
                total_hours = int(current_hour - old_real_hour)
                total_minutes = float(current_minute - old_real_minute)

                total_year_in_minutes = int(total_year * 12 * 30 * 24 * 60)
                total_months_in_minutes = int(total_month * 30 * 24 * 60)
                total_days_in_minutes = int(total_days * 24 * 60)
                total_hours_in_minutes = int(total_hours * 60)

                total_time_in_minutes = float(
                    total_year_in_minutes
                    + total_months_in_minutes
                    + total_days_in_minutes
                    + total_hours_in_minutes
                    + total_minutes
                )
                total_time_in_hours = float(total_time_in_minutes / 60)
                total_time_days = float(total_time_in_hours / 24)

                # end of time operation

                # proplem_quantity

                proplem_quantity = real_quantity - current_quantity

                # end of proplem_quantity

                #  partner_name, product_name, code , quantity ,new_quantity, problem_quantity , forget_quantity, size , s_unreal_day , s_unreal_month , s_unreal_year , R_unreal_day , R_unreal_month , R_unreal_year , s_comments, R_comments, real_total_days , taken_total_days,  ):

                self.db.receive_from_partner_insert(
                    partner_name,
                    product_name,
                    code,
                    real_quantity,
                    current_quantity,
                    proplem_quantity,
                    forget,
                    size,
                    old_d,
                    old_m,
                    old_y,
                    current_day_unreal,
                    current_month_unreal,
                    current_year_unreal,
                    past_comments,
                    new_comments,
                    total_time_in_minutes,
                    total_time_days,
                    warehouse,
                )

                self.db.receive_from_partner_insert_copy(
                    partner_name,
                    product_name,
                    code,
                    real_quantity,
                    current_quantity,
                    proplem_quantity,
                    forget,
                    size,
                    old_d,
                    old_m,
                    old_y,
                    current_day_unreal,
                    current_month_unreal,
                    current_year_unreal,
                    past_comments,
                    new_comments,
                    total_time_in_minutes,
                    total_time_days,
                    warehouse,
                )

                self.db.remove_send(code)

                frame_send_t0_warehouse = Frame(
                    self.recive_partener_frame, width=300, height=400, bg=white
                )
                frame_send_t0_warehouse.pack()

                self.add_image(
                    "backgrounds/send_to_warehouse.png",
                    300,
                    400,
                    0,
                    0,
                    frame_send_t0_warehouse,
                    white,
                )

                messagebox.showinfo("تم الحفظ بنجاح", "تم إرسال المنتج  بنجاح ")

    def update_the_entries(self):
        code = self.code_of_partner_recive.get()
        send_data = self.db.fetch_by_id_send_partner(code)
        print(send_data)
        try:
            product_name = send_data[3]
            real_quantity = int(send_data[4])
            past_comments = send_data[8]
            size = send_data[2]
            old_y = send_data[5]
            old_m = send_data[6]
            old_d = send_data[7]
            old_real_year = int(send_data[9])
            old_real_month = int(send_data[10])
            old_real_day = int(send_data[11])
            old_real_hour = int(send_data[12])
            old_real_minute = int(send_data[13])

            current_quantity = int(self.quantity_of_recive.get())
            warehouse = self.warehouse_of_partner_recive.get()
            partner_name = self.name_of_partner_recive.get()
            forget = self.quantity_of_recive_proplem.get()
            current_year_unreal = self.year_entry_date_partner_recive.get()
            current_month_unreal = self.months_combobox_date_partner_recive.get()
            current_day_unreal = self.days_combobox_date_partner_recive.get()
            new_comments = self.txtbox_comment_recive_partner.get("1.0", "end")

            current_year = int(self.now.year)
            current_month = int(self.now.month)
            current_day = int(self.now.day)
            current_hour = int(self.now.hour)
            current_minute = int(self.now.minute)

            # time operation

            total_year = int(current_year - old_real_year)
            total_month = int(current_month - old_real_month)
            total_days = int(current_day - old_real_day)
            total_hours = int(current_hour - old_real_hour)
            total_minutes = float(current_minute - old_real_minute)

            total_year_in_minutes = int(total_year * 12 * 30 * 24 * 60)
            total_months_in_minutes = int(total_month * 30 * 24 * 60)
            total_days_in_minutes = int(total_days * 24 * 60)
            total_hours_in_minutes = int(total_hours * 60)

            total_time_in_minutes = float(
                total_year_in_minutes
                + total_months_in_minutes
                + total_days_in_minutes
                + total_hours_in_minutes
                + total_minutes
            )
            total_time_in_hours = float(total_time_in_minutes / 60)
            total_time_days = float(total_time_in_hours / 24)

            # end of time operation

            # proplem_quantity

            proplem_quantity = real_quantity - current_quantity

            # end of proplem_quantity

            date = f" {old_real_year} / {old_real_month} / {old_real_day} / {old_real_hour} / {old_real_minute}  "

            self.quantity_send_inrecive_page.config(state="normal")
            self.quantity_send_inrecive_page.delete(0, tk.END)
            self.quantity_send_inrecive_page.insert(0, real_quantity)
            self.quantity_send_inrecive_page.config(state="readonly")

            self.size_of_product_in_recive.config(state="normal")
            self.size_of_product_in_recive.delete(0, tk.END)
            self.size_of_product_in_recive.insert(0, size)
            self.size_of_product_in_recive.config(state="readonly")

            self.date_of_send_in_recive.config(state="normal")
            self.date_of_send_in_recive.delete(0, tk.END)
            self.date_of_send_in_recive.insert(0, date)
            self.date_of_send_in_recive.config(state="readonly")

            self.comments_of_send_in_recive.config(state="normal")
            self.comments_of_send_in_recive.delete(0, tk.END)
            self.comments_of_send_in_recive.insert(0, past_comments)
            self.comments_of_send_in_recive.config(state="readonly")

            self.el3gz_of_send_in_recive.config(state="normal")
            self.el3gz_of_send_in_recive.delete(0, tk.END)
            self.el3gz_of_send_in_recive.insert(0, proplem_quantity)
            self.el3gz_of_send_in_recive.config(state="readonly")

            self.days_of_send_in_recive.config(state="normal")
            self.days_of_send_in_recive.delete(0, tk.END)
            self.days_of_send_in_recive.insert(0, total_time_in_minutes)
            self.days_of_send_in_recive.config(state="readonly")

            self.name_of_product_of_send_in_recive.config(state="normal")
            self.name_of_product_of_send_in_recive.delete(0, tk.END)
            self.name_of_product_of_send_in_recive.insert(0, send_data[3])
            self.name_of_product_of_send_in_recive.config(state="readonly")
        except Exception as e:
            logging.error(e)
            return []

    def fill_entries(self):
        code = self.code_of_partner_recive.get()
        current_quantity = self.quantity_of_recive.get()
        warehouse = self.warehouse_of_partner_recive.get()
        partner_name = self.name_of_partner_recive.get()
        forget = self.quantity_of_recive_proplem.get()
        current_year_unreal = self.year_entry_date_partner_recive.get()
        current_month_unreal = self.months_combobox_date_partner_recive.get()
        current_day_unreal = self.days_combobox_date_partner_recive.get()
        new_comments = self.txtbox_comment_recive_partner.get("1.0", "end")

        self.quantity_send_inrecive_page.config(state="normal")
        self.quantity_send_inrecive_page.insert(0, "current_quantity")
        self.quantity_send_inrecive_page.config(state="readonly")

        self.size_of_product_in_recive.insert(0, "code")

        self.date_of_send_in_recive.insert(0, "warehouse")

        self.comments_of_send_in_recive.insert(0, "partner_name")

        self.el3gz_of_send_in_recive.insert(0, "forget")

        self.days_of_send_in_recive.insert(0, "current_year_unreal")

        self.name_of_product_of_send_in_recive.insert(0, "current_day_unreal")

    def recive_from_partner(self):
        self.recive_partener_frame = Frame(
            self.partner_pages, width=1285, height=600, bg=white
        )
        self.recive_partener_frame.place(x=0, y=0)
        self.add_image(
            r"images\recieve_background.png",
            1285,
            600,
            0,
            -10,
            self.recive_partener_frame,
            white,
        )

        self.frame_recive_options = Frame(
            self.recive_partener_frame, width=390, height=480, bg=whitey
        )
        self.frame_recive_options.place(x=370, y=80)

        lbl_name_partner = Label(
            self.frame_recive_options,
            text="أسم الصنايعي",
            font=("Arial", 15, "bold"),
            bg=whitey,
            fg=black,
        ).place(x=280, y=20)

        lbl_code = Label(
            self.frame_recive_options,
            text="كود القصه",
            font=("Arial", 15, "bold"),
            bg=whitey,
            fg=black,
            justify="right",
        ).place(x=300, y=70)

        lbl_recived_quantity = Label(
            self.frame_recive_options,
            text="العدد المستلم",
            font=("Arial", 15, "bold"),
            bg=whitey,
            fg=black,
            justify="right",
        ).place(x=300, y=120)

        lbl_recived_quantity_defgouhs = Label(
            self.frame_recive_options,
            text="عدد العيوب",
            font=("Arial", 15, "bold"),
            bg=whitey,
            fg=black,
            justify="right",
        ).place(x=300, y=170)

        lbl_recived_date = Label(
            self.frame_recive_options,
            text="تاريخ الأستلام",
            font=("Arial", 15, "bold"),
            bg=whitey,
            fg=black,
            justify="right",
        ).place(x=290, y=220)

        lbl_recived_warehouse = Label(
            self.frame_recive_options,
            text="المخزن",
            font=("Arial", 15, "bold"),
            bg=whitey,
            fg=black,
            justify="right",
        ).place(x=300, y=270)

        lbl_recived_comments = Label(
            self.frame_recive_options,
            text="الملاحظات",
            font=("Arial", 15, "bold"),
            bg=whitey,
            fg=black,
            justify="right",
        ).place(x=300, y=320)

        #  add entries to recive

        self.name_of_partner_recive = ttk.Combobox(
            self.frame_recive_options,
            state="readonly",
            width=14,
            font=("ca-bold", 15),
            justify="right",
        )
        self.name_of_partner_recive.place(x=50, y=20)

        self.code_of_partner_recive = ttk.Combobox(
            self.frame_recive_options,
            state="readonly",
            width=14,
            font=("ca-bold", 15),
            justify="right",
        )
        self.code_of_partner_recive.place(x=50, y=70)

        self.quantity_of_recive = ttk.Entry(
            self.frame_recive_options,
            width=15,
            font=("Arial", 15, "bold"),
            justify="right",
        )
        self.quantity_of_recive.place(x=50, y=120)

        self.quantity_of_recive_proplem = ttk.Entry(
            self.frame_recive_options,
            width=15,
            font=("Arial", 15, "bold"),
            justify="right",
        )
        self.quantity_of_recive_proplem.place(x=50, y=170)

        # date add

        self.days_combobox_date_partner_recive = ttk.Combobox(
            self.frame_recive_options,
            state="readonly",
            width=3,
            font=("ca-bold", 11),
            justify="right",
        )

        self.days_combobox_date_partner_recive["values"] = (
            "1",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
            "10",
            "11",
            "12",
            "13",
            "14",
            "15",
            "16",
            "17",
            "18",
            "19",
            "20",
            "21",
            "22",
            "23",
            "24",
            "25",
            "26",
            "27",
            "28",
            "29",
            "30",
            "31",
        )
        self.days_combobox_date_partner_recive.place(x=60, y=220)

        self.months_combobox_date_partner_recive = ttk.Combobox(
            self.frame_recive_options,
            state="readonly",
            width=3,
            font=("ca-bold", 11),
            justify="right",
        )
        self.months_combobox_date_partner_recive["values"] = (
            "1",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
            "10",
            "11",
            "12",
        )
        self.months_combobox_date_partner_recive.place(x=110, y=220)

        self.year_entry_date_partner_recive = ttk.Entry(
            self.frame_recive_options,
            width=5,
            font=("ca-bold", 11),
            justify="left",
        )
        self.year_entry_date_partner_recive.place(x=160, y=220)

        self.warehouse_of_partner_recive = ttk.Combobox(
            self.frame_recive_options,
            state="readonly",
            width=14,
            font=("ca-bold", 15),
            justify="right",
        )
        self.warehouse_of_partner_recive.place(x=50, y=270)

        self.txtbox_comment_recive_partner = Text(
            self.frame_recive_options, width=22, height=4, font=("ca-bold", 11), bd=0
        )
        self.txtbox_comment_recive_partner.place(x=50, y=320)

        # add buttons

        btn_see_data = tk.Button(
            self.frame_recive_options,
            text="رؤيه مسبقه",
            highlightbackground=blue,
            cursor="hand2",
            background=blue,
            foreground=white,
            activebackground=white,
            activeforeground=blue,
            highlightthickness=2,
            highlightcolor=blue,
            width=8,
            height=2,
            border=0,
            font=("Arial", 16, "bold"),
            command=self.update_the_entries,
        )
        btn_see_data.place(x=270, y=410)

        btn_see_data = tk.Button(
            self.frame_recive_options,
            text="أستلام",
            highlightbackground=black,
            cursor="hand2",
            background=black,
            foreground=white,
            activebackground=white,
            activeforeground=black,
            highlightthickness=2,
            highlightcolor=black,
            width=8,
            height=2,
            border=0,
            font=("Arial", 16, "bold"),
            command=self.receive_from_partener_insert,
        )
        btn_see_data.place(x=60, y=410)

        #  add frame to left side to add some functions

        self.frame_recive_external_data = Frame(
            self.recive_partener_frame, width=340, height=340, bg=white
        )
        self.frame_recive_external_data.place(x=856, y=31)

        # add labels in the new frame

        quantity_send = Label(
            self.frame_recive_external_data,
            text="العدد المرسل",
            font=("Arial", 15, "bold"),
            bg=white,
            fg=black,
            justify="right",
        ).place(x=250, y=10)

        date_send = Label(
            self.frame_recive_external_data,
            text="تاريخ المرسل",
            font=("Arial", 15, "bold"),
            bg=white,
            fg=black,
            justify="right",
        ).place(x=80, y=10)

        size = Label(
            self.frame_recive_external_data,
            text="المقاس",
            font=("Arial", 15, "bold"),
            bg=white,
            fg=black,
            justify="right",
        ).place(x=290, y=60)

        last_comments = Label(
            self.frame_recive_external_data,
            text="ملاحظات المرسل",
            font=("Arial", 15, "bold"),
            bg=white,
            fg=black,
            justify="right",
        ).place(x=80, y=60)

        # add simi line

        add_simi_line = Frame(
            self.frame_recive_external_data, width=200, height=2, bg=black
        ).place(x=80, y=120)

        el3gz = Label(
            self.frame_recive_external_data,
            text="العجز",
            font=("Arial", 15, "bold"),
            bg=white,
            fg=black,
            justify="right",
        ).place(x=300, y=150)

        number_of_days = Label(
            self.frame_recive_external_data,
            text="عدد الدقائق",
            font=("Arial", 15, "bold"),
            bg=white,
            fg=black,
            justify="center",
        ).place(x=80, y=150)

        name_of_the_product = Label(
            self.frame_recive_external_data,
            text="أسم المنتج",
            font=("Arial", 15, "bold"),
            bg=white,
            fg=black,
            justify="center",
        ).place(x=270, y=200)

        # add entries to the the new frame to show external data
        self.quantity_send_inrecive_page = Entry(
            self.frame_recive_external_data,
            width=10,
            font=("Arial", 10, "bold"),
            justify="center",
            bd=0,
            fg=dark_black,
            bg=white,
            state="readonly",
        )
        self.quantity_send_inrecive_page.place(x=175, y=15)

        self.size_of_product_in_recive = Entry(
            self.frame_recive_external_data,
            width=10,
            font=("Arial", 10, "bold"),
            justify="center",
            state="readonly",
            bd=0,
            fg=dark_black,
            bg=white,
        )
        self.size_of_product_in_recive.place(x=210, y=70)

        self.date_of_send_in_recive = Entry(
            self.frame_recive_external_data,
            width=0,
            font=("Arial", 10, "bold"),
            justify="center",
            state="readonly",
            bd=0,
            fg=dark_black,
            bg=white,
        )
        self.date_of_send_in_recive.place(x=1, y=45)

        self.comments_of_send_in_recive = Entry(
            self.frame_recive_external_data,
            width=10,
            font=("Arial", 10, "bold"),
            justify="center",
            state="readonly",
            bd=0,
            fg=dark_black,
            bg=white,
        )
        self.comments_of_send_in_recive.place(x=10, y=70)

        self.el3gz_of_send_in_recive = Entry(
            self.frame_recive_external_data,
            width=10,
            font=("Arial", 10, "bold"),
            justify="center",
            state="readonly",
            bd=0,
            fg=dark_black,
            bg=white,
        )
        self.el3gz_of_send_in_recive.place(x=220, y=155)

        self.days_of_send_in_recive = Entry(
            self.frame_recive_external_data,
            width=10,
            font=("Arial", 10, "bold"),
            justify="center",
            state="readonly",
            bd=0,
            fg=dark_black,
            bg=white,
        )
        self.days_of_send_in_recive.place(x=10, y=155)

        self.name_of_product_of_send_in_recive = Entry(
            self.frame_recive_external_data,
            width=15,
            font=("Arial", 15, "bold"),
            justify="center",
            state="readonly",
            bd=0,
            fg=dark_black,
            bg=white,
        )
        self.name_of_product_of_send_in_recive.place(x=90, y=205)

        # add buttons

        self.btn_all_recived = tk.Button(
            self.recive_partener_frame,
            text="جميع بينات الاستلام",
            highlightbackground=light_blue,
            cursor="hand2",
            background=light_blue,
            foreground=white,
            activebackground=white,
            activeforeground=light_blue,
            highlightthickness=2,
            highlightcolor=light_blue,
            width=15,
            height=2,
            border=0,
            font=("Arial", 16, "bold"),
        )
        self.btn_all_recived.place(x=1030, y=410)

        self.btn_edit_recived = tk.Button(
            self.recive_partener_frame,
            text="تعديل بينات الاستلام",
            highlightbackground=light_blue,
            cursor="hand2",
            background=light_blue,
            foreground=white,
            activebackground=white,
            activeforeground=light_blue,
            highlightthickness=2,
            highlightcolor=light_blue,
            width=14,
            height=2,
            border=0,
            font=("Arial", 16, "bold"),
        )
        self.btn_edit_recived.place(x=830, y=410)

        self.btn_send_to_partner = tk.Button(
            self.recive_partener_frame,
            text="ارسال للصنايعي",
            highlightbackground=light_blue,
            cursor="hand2",
            background=light_blue,
            foreground=white,
            activebackground=white,
            activeforeground=light_blue,
            highlightthickness=2,
            highlightcolor=light_blue,
            width=14,
            height=2,
            border=0,
            font=("Arial", 16, "bold"),
            command=self.send_to_partener,
        )

        self.btn_send_to_partner.place(x=830, y=480)

        self.bnt_add_partner = tk.Button(
            self.recive_partener_frame,
            text="أضافه صنايعي",
            highlightbackground=light_blue,
            cursor="hand2",
            background=light_blue,
            foreground=white,
            activebackground=white,
            activeforeground=light_blue,
            highlightthickness=2,
            highlightcolor=light_blue,
            width=15,
            height=2,
            border=0,
            font=("Arial", 16, "bold"),
            command=self.add_partners,
        )
        self.bnt_add_partner.place(x=1030, y=480)

        self.poplute_partner_warehouse_code_recive()
        self.name_of_partner_recive.bind("<<ComboboxSelected>>", self.poplute_id)

    def edit_product_partner(self):
        self.edit_partener_frame = Frame(
            self.partner_pages, width=1285, height=600, bg=white
        )
        self.edit_partener_frame.place(x=0, y=0)

    def settings(self):
        self.partner_main_frame = Frame(
            self.Upper_frame, bg=whitey, width=1285, height=700
        )
        self.partner_main_frame.place(x=0, y=1)

        self.add_image(
            "backgrounds\settings.png", 1285, 700, 0, 0, self.partner_main_frame, white
        )

        self.save_data_btn = tk.Button(
            self.partner_main_frame,
            text="حفظ البينات",
            bg=whitey,
            fg=green_canva,
            relief="flat",
            font=(
                "Arial",
                17,
            ),
            bd=0,
        )

        self.save_data_btn.place(x=130, y=580)

        self.about_btn = tk.Button(
            self.partner_main_frame,
            text="تواصل معانا",
            bg=whitey,
            fg=green_canva,
            relief="flat",
            font=(
                "Arial",
                17,
            ),
            command=self.about,
            bd=0,
        )

        self.about_btn.place(x=720, y=585)

        self.log_out_btn = tk.Button(
            self.partner_main_frame,
            text="تسجيل خروج",
            bg=whitey,
            fg=false_red,
            relief="flat",
            font=(
                "Arial",
                17,
            ),
            bd=0,
        )

        self.log_out_btn.place(x=435, y=583)

        self.proplem_btn = tk.Button(
            self.partner_main_frame,
            text="الشكاوي",
            bg=whitey,
            fg=pinky_canva,
            relief="flat",
            font=(
                "Arial",
                17,
            ),
            bd=0,
        )

        self.proplem_btn.place(x=1020, y=585)

    def about(self):
        self.about_main_frame = Frame(
            self.Upper_frame, bg=whitey, width=1285, height=700
        )
        self.about_main_frame.place(x=0, y=1)

        self.add_image(
            r"backgrounds\about.png", 1285, 700, 0, 0, self.about_main_frame, white
        )


white = "#FFFFFF"
whitey = "#e0e0e0"
purple = "#6023E5"
dark_yellow = "#FDCF61"
dark_black = "#080e25"
green_fa23 = "#78D000"
blue = "#4A7DF0"
zyty = "#004746"
asfar_fa23 = "#FFC745"
false_red = "#F20505"
black = "#0D0D0D"
light_blue = "#18608C"
dark_grey = "#808080"
blue_canva = "#0292B7"
blue_fat7_canva = "#BFD2DA"
green_canva = "#6BC3A4"
pinky_canva = "#F15B6C"
root = Tk()
oop = factory(root)
root.mainloop()

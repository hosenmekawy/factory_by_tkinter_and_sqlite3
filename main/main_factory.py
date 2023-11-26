# mekawy is talking pitches
from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
from tkinter import font
from tkinter.ttk import *
import csv
import pandas as pd
import numpy as np
import time
import matplotlib.pyplot as plt
import math
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db


class mainpage ():

    def __init__(self, root):

        # config

        self.root = root
        # width= self.root.winfo_screenwidth()
        # height= self.root.winfo_screenheight()
        # #setting tkinter window size
        # self.root.geometry("%dx%d" % (width, height))
        self.root.state('zoomed')
        self.root.title('project university')
        self.root.configure(background=white)
        self.root.resizable(TRUE, TRUE)
    # variables

    # left side frame

        self.left_frame = Frame(
            self.root, bg=dark_black, width=240, height=800)
        self.left_frame.place(x=1, y=0)

        # pinned logo
        logo_pic_main = Image.open(
            "logo\Screenshot_2023-07-24_202157-removebg-preview.png")
        resized = logo_pic_main.resize((200, 80))
        logo_pic_mainB = ImageTk.PhotoImage(resized)
        logo_pic_main_A = Label(
            self.left_frame, image=logo_pic_mainB, bg=dark_black)
        logo_pic_main_A.image = logo_pic_mainB
        logo_pic_main_A.place(x=20, y=0)

        
                        

    # upper Right frame
        self.Upper_frame = Frame(self.root, bg=white, width=1285, height=120)
        self.Upper_frame.place(x=246, y=0)

    # center frame

        self.Upper_frame = Frame(self.root, bg=white, width=1285, height=700)
        self.Upper_frame.place(x=246, y=120)
    # line separate
        self.line1_frame = Frame(self.root, bg=whitey, width=1283, height=5)
        self.line1_frame.place(x=246, y=120)

    def left_side_degisn(self):
        photo = PhotoImage(file=r"images\settings.png")

        # Resizing image to fit on button
        photoimage = photo.subsample(3, 3)

        # here, image option is used to
        # set image on button
        # compound option is used to align
        # image on LEFT side of button
        Button(self.left_frame, text='settings', image=photoimage,
               compound=LEFT).place(x=10, y=100)


white = '#FFFFFF'
whitey = '#e0e0e0'
purple = '#6023E5'
dark_yellow = '#c07500'
dark_black = '#080e25'
root = Tk()
oop = mainpage(root)
root.mainloop()

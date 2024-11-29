import tkinter as tk
from tkinter import *
import os
import cv2
import shutil
import csv
import numpy as np
from PIL import ImageTk, Image
import pandas as pd
import datetime
import time
import tkinter.font as font
import pyttsx3

# Project modules
import show_attendance
import takeImage
import trainImage
import automaticAttedance

# Define border width variable
border_width = 3  # Adjust this value as needed

# Text to Speech Function
def text_to_speech(user_text):
    engine = pyttsx3.init()
    engine.say(user_text)
    engine.runAndWait()

# File paths
haarcasecade_path = "haarcascade_frontalface_default.xml"
trainimagelabel_path = "Trainner.yml"
trainimage_path = "TrainingImage"
if not os.path.exists(trainimage_path):
    os.makedirs(trainimage_path)

studentdetail_path = "/StudentDetails/studentdetails.csv"
attendance_path = "Attendance"

# Main window setup
window = tk.Tk()
window.title("Face recognizer")
window.geometry("1280x720")
window.configure(background="black")

# Function to destroy the warning screen
def del_sc1():
    sc1.destroy()

# Error message for name and number
def err_screen():
    global sc1
    sc1 = tk.Tk()
    sc1.geometry("400x110")
    sc1.iconbitmap("AMS.ico")
    sc1.title("Warning!!")
    sc1.configure(background="black")
    sc1.resizable(0, 0)
    tk.Label(
        sc1,
        text="Enrollment & Name Required!!!",
        fg="white",
        bg="black",
        font=("times", 20, "bold"),
    ).pack()
    tk.Button(
        sc1,
        text="OK",
        command=del_sc1,
        fg="white",
        bg="black",
        width=9,
        height=1,
        activebackground="Red",
        font=("times", 20, "bold"),
        bd=border_width  # Use the border width variable here
    ).place(x=110, y=50)

# Function to validate entry (only digits allowed)
def testVal(inStr, acttyp):
    if acttyp == "1":  # insert
        if not inStr.isdigit():
            return False
    return True

# Define common font style for buttons and labels
common_font = ("times new roman", 16)

# Update the main title font for better visibility
titl = tk.Label(window, text="Efficient Student Attendance System", 
                bg="black", fg="green", font=("arial", 35, "bold"), bd=border_width, relief=RIDGE)
titl.pack(fill=X)

# Adjusted positions and padding for title and welcome message
a = tk.Label(window, text="Welcome to the Attendance System\nUsing LBPH and OpenCV", 
             bg="black", fg="white", font=("arial", 28, "bold"), bd=border_width, pady=10)
a.pack(pady=(30, 10))

# Load and place images
def load_and_place_image(image_path, x, y):
    img = Image.open(image_path)
    img = ImageTk.PhotoImage(img)
    label = tk.Label(window, image=img)
    label.image = img
    label.place(x=x, y=y)

# Adjusted image placement for balance
x = 120
y = 250
load_and_place_image("UI_Image/registerIcon.png", x, y)
load_and_place_image("UI_Image/attendanceIcon.png", x+400, y)
load_and_place_image("UI_Image/viewIcon.png", x+800, y)


def create_button_with_icon(text,color, command, x, y, icon=None):
    button = tk.Button(window, text=text, command=command, font=common_font, 
                       bg=color, fg="white", bd=border_width, height=2, width=18, relief=RIDGE)
    if icon:
        button.config(image=icon, compound=LEFT)
    button.place(x=x, y=y)

# Place buttons directly below the images
button_y_position = 500

create_button_with_icon("Register","black", lambda: TakeImageUI(), x, button_y_position)
create_button_with_icon("Take Attendance","black", lambda: automaticAttedance.subjectChoose(text_to_speech), x+400, button_y_position)
create_button_with_icon("View Attendance","black",lambda: show_attendance.subjectchoose(text_to_speech), x+800, button_y_position)

# Centering the Exit button # Adjust width based on button size
create_button_with_icon("EXIT","#FD2A2A", window.destroy, x+400, 600)  # Adjust the y-position if necessary

# Function to open the image registration UI
def TakeImageUI():
    ImageUI = tk.Tk()
    ImageUI.title("Take Student Image..")
    ImageUI.geometry("780x480")
    ImageUI.configure(background="black")
    ImageUI.resizable(0, 0)
    
    titl = tk.Label(ImageUI, bg="black", relief=RIDGE, bd=border_width, font=("arial", 35))
    titl.pack(fill=X)
    titl = tk.Label(
        ImageUI, text="Register", bg="black", fg="green", font=("arial", 30),
    )
    titl.place(x=270, y=12)

    a = tk.Label(
        ImageUI,
        text="Enter the details",
        bg="black",
        fg="white",
        bd=border_width,
        font=("arial", 24),
    )
    a.place(x=280, y=75)

    lbl1 = tk.Label(
        ImageUI,
        text="Enrollment No",
        width=10,
        height=2,
        bg="black",
        fg="white",
        bd=border_width,
        relief=RIDGE,
        font=("times new roman", 12),
    )
    lbl1.place(x=120, y=130)
    txt1 = tk.Entry(
        ImageUI,
        width=17,
        bd=border_width,
        validate="key",
        bg="black",
        fg="white",
        relief=RIDGE,
        font=("times", 25, "bold"),
    )
    txt1.place(x=250, y=130)
    txt1["validatecommand"] = (txt1.register(testVal), "%P", "%d")

    lbl2 = tk.Label(
        ImageUI,
        text="Name",
        width=10,
        height=2,
        bg="black",
        fg="white",
        bd=border_width,
        relief=RIDGE,
        font=("times new roman", 12),
    )
    lbl2.place(x=120, y=200)
    txt2 = tk.Entry(
        ImageUI,
        width=17,
        bd=border_width,
        bg="black",
        fg="white",
        relief=RIDGE,
        font=("times", 25, "bold"),
    )
    txt2.place(x=250, y=200)

    lbl3 = tk.Label(
        ImageUI,
        text="Notification",
        width=10,
        height=2,
        bg="black",
        fg="white",
        bd=border_width,
        relief=RIDGE,
        font=("times new roman", 12),
    )
    lbl3.place(x=120, y=270)

    message = tk.Label(
        ImageUI,
        text="",
        width=32,
        height=2,
        bd=border_width,
        bg="black",
        fg="white",
        relief=RIDGE,
        font=("times", 12, "bold"),
    )
    message.place(x=250, y=270)

    def take_image():
        l1 = txt1.get()
        l2 = txt2.get()
        takeImage.TakeImage(
            l1,
            l2,
            haarcasecade_path,
            trainimage_path,
            message,
            err_screen,
            text_to_speech,
        )
        txt1.delete(0, "end")
        txt2.delete(0, "end")

    takeImg = tk.Button(
        ImageUI,
        text="Take Image",
        command=take_image,
        bd=border_width,
        font=("times new roman", 18),
        bg="black",
        fg="white",
        height=2,
        width=12,
        relief=RIDGE,
    )
    takeImg.place(x=130, y=350)

    def train_image():
        trainImage.TrainImage(
            haarcasecade_path,
            trainimage_path,
            trainimagelabel_path,
            message,
            text_to_speech,
        )

    trainImg = tk.Button(
        ImageUI,
        text="Train Image",
        command=train_image,
        bd=border_width,
        font=("times new roman", 18),
        bg="black",
        fg="white",
        height=2,
        width=12,
        relief=RIDGE,
    )
    trainImg.place(x=350, y=350)

    def clear():
        txt1.delete(0, "end")
        txt2.delete(0, "end")

    clearButton = tk.Button(
        ImageUI,
        text="Clear",
        command=clear,
        bd=border_width,
        font=("times new roman", 18),
        bg="black",
        fg="white",
        height=2,
        width=12,
        relief=RIDGE,
    )
    clearButton.place(x=570, y=350)

    ImageUI.mainloop()

# Run the main window loop
window.mainloop()

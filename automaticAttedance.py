import tkinter as tk
from tkinter import *
import os, cv2
import shutil
import csv
import numpy as np
from PIL import ImageTk, Image
import pandas as pd
import datetime
import time
import tkinter.ttk as tkk
import tkinter.font as font

haarcasecade_path = "haarcascade_frontalface_default.xml"
trainimagelabel_path = "Trainner.yml"
trainimage_path = "TrainingImage"
studentdetail_path = "StudentDetails/studentdetails.csv"
attendance_path = "Attendance"

def subjectChoose(text_to_speech):
    def FillAttendance():
        sub = tx.get()
        now = time.time()
        future = now + 20

        if sub == "":
            t = "Please enter the subject name!!!"
            text_to_speech(t)
        else:
            try:
                recognizer = cv2.face.LBPHFaceRecognizer_create()
                if not os.path.isfile(trainimagelabel_path):
                    e = "Model not found, please train the model first."
                    Notifica.configure(
                        text=e,
                        bg="black",
                        fg="white",
                        width=33,
                        font=("times", 15, "bold"),
                    )
                    Notifica.place(x=20, y=250)
                    text_to_speech(e)
                    return
                
                recognizer.read(trainimagelabel_path)
                facecasCade = cv2.CascadeClassifier(haarcasecade_path)
                df = pd.read_csv(studentdetail_path)
                cam = cv2.VideoCapture(0)
                font = cv2.FONT_HERSHEY_SIMPLEX
                col_names = ["Enrollment", "Name"]
                attendance = pd.DataFrame(columns=col_names)
                
                while True:
                    ret, im = cam.read()
                    if not ret:
                        print("Failed to grab frame")
                        break
                    
                    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
                    faces = facecasCade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
                    print(f"Faces detected: {len(faces)}")
                    
                    for (x, y, w, h) in faces:
                        Id, conf = recognizer.predict(gray[y:y + h, x:x + w])
                        print(f"Confidence: {conf}")
                        if conf < 80:
                            aa = df.loc[df["Enrollment"] == Id]["Name"].values
                            tt = f"{Id}-{aa}"
                            attendance.loc[len(attendance)] = [Id, aa]
                            cv2.rectangle(im, (x, y), (x + w, y + h), (0, 255, 0), 4)
                            cv2.putText(im, str(tt), (x + h, y), font, 1, (255, 255, 0), 4)
                        else:
                            Id = "Unknown"
                            tt = str(Id)
                            cv2.rectangle(im, (x, y), (x + w, y + h), (0, 25, 255), 7)
                            cv2.putText(im, str(tt), (x + h, y), font, 1, (0, 25, 255), 4)
                    
                    if time.time() > future:
                        break

                    cv2.imshow("Filling Attendance...", im)
                    key = cv2.waitKey(30) & 0xFF
                    if key == 27:  # Press 'Esc' to exit
                        break

                attendance = attendance.drop_duplicates(["Enrollment"], keep="first")
                
                ts = time.time()
                date = datetime.datetime.fromtimestamp(ts).strftime("%Y-%m-%d")
                timeStamp = datetime.datetime.fromtimestamp(ts).strftime("%H:%M:%S")
                Hour, Minute, Second = timeStamp.split(":")
                
                # Ensure the folder path exists for the given subject
                subject_folder = os.path.join(attendance_path, sub)
                if not os.path.exists(subject_folder):
                    os.makedirs(subject_folder)

                # Save attendance CSV in the subject folder
                fileName = f"{subject_folder}/{sub}_{date}_{Hour}-{Minute}-{Second}.csv"
                attendance.to_csv(fileName, index=False)

                m = "Attendance filled successfully for " + sub
                Notifica.configure(
                    text=m,
                    bg="black",
                    fg="white",
                    width=33,
                    relief=RIDGE,
                    bd=3,
                    font=("times", 15, "bold"),
                )
                text_to_speech(m)
                Notifica.place(x=20, y=250)

                cam.release()
                cv2.destroyAllWindows()

                # Display the saved attendance in a new window
                root = tk.Tk()
                root.title("Attendance of " + sub)
                root.configure(background="black")
                
                with open(fileName, newline="") as file:
                    reader = csv.reader(file)
                    for r, col in enumerate(reader):
                        for c, row in enumerate(col):
                            label = tk.Label(
                                root,
                                width=10,
                                height=1,
                                fg="white",
                                font=("times", 15, " bold "),
                                bg="black",
                                text=row,
                                relief=tk.RIDGE,
                            )
                            label.grid(row=r, column=c)
                root.mainloop()
            except Exception as e:
                print(f"Error: {e}")
                f = "No Face found for attendance"
                text_to_speech(f)
                cv2.destroyAllWindows()

    subject = Tk()
    subject.title("Subject...")
    subject.geometry("580x320")
    subject.resizable(0, 0)
    subject.configure(background="black")

    titl = tk.Label(subject, bg="black", relief=RIDGE, bd=3, font=("arial", 30))
    titl.pack(fill=X)
    titl = tk.Label(
        subject,
        text="Enter the Subject Name",
        bg="black",
        fg="green",
        font=("arial", 25),
    )
    titl.place(x=160, y=12)
    Notifica = tk.Label(
        subject,
        text="Attendance filled Successfully",
        bg="white",
        fg="black",
        width=33,
        height=2,
        font=("times", 15, "bold"),
    )

    def Attf():
        sub = tx.get()
        if sub == "":
            t = "Please enter the subject name!!!"
            text_to_speech(t)
        else:
            os.startfile(f"Attendance\\{sub}")

    attf = tk.Button(
        subject,
        text="Check Sheets",
        command=Attf,
        bd=3,
        font=("times new roman", 15),
        bg="black",
        fg="white",
        height=2,
        width=10,
        relief=RIDGE,
    )
    attf.place(x=360, y=170)

    sub = tk.Label(
        subject,
        text="Enter Subject",
        width=10,
        height=2,
        bg="black",
        fg="white",
        bd=3,
        relief=RIDGE,
        font=("times new roman", 15),
    )
    sub.place(x=50, y=100)

    tx = tk.Entry(
        subject,
        width=15,
        bd=3,
        bg="black",
        fg="white",
        relief=RIDGE,
        font=("times", 30, "bold"),
    )
    tx.place(x=190, y=100)

    fill_a = tk.Button(
        subject,
        text="Fill Attendance",
        command=FillAttendance,
        bd=3,
        font=("times new roman", 15),
        bg="black",
        fg="white",
        height=2,
        width=12,
        relief=RIDGE,
    )
    fill_a.place(x=195, y=170)
    subject.mainloop()

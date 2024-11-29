import pandas as pd
from glob import glob
import os
import tkinter
import csv
import tkinter as tk
from tkinter import *

# Paths
attendance_path = "Attendance"

def subjectchoose(text_to_speech):
    def calculate_attendance():
        Subject = tx.get()
        if Subject == "":
            t = 'Please enter the subject name.'
            text_to_speech(t)
            return
        
        subject_directory = os.path.join(attendance_path, Subject)
        if not os.path.exists(subject_directory):
            t = f"No directory found for the subject: {Subject}"
            text_to_speech(t)
            return
        
        filenames = glob(os.path.join(subject_directory, f"{Subject}*.csv"))
        if len(filenames) == 0:
            t = f"No attendance files found for the subject: {Subject}"
            text_to_speech(t)
            return
        
        # Initialize an empty DataFrame to store merged attendance data
        all_data = pd.DataFrame()

        # Read each file and process attendance
        for file in filenames:
            df = pd.read_csv(file)
            df['Present'] = 1  # Mark students as present in this timestamp
            df['Timestamp'] = os.path.basename(file)  # Record the timestamp (from filename)
            all_data = pd.concat([all_data, df[['Enrollment', 'Name', 'Present']]], ignore_index=True)

        # Calculate attendance by counting appearances and dividing by the number of files
        attendance_summary = all_data.groupby(['Enrollment', 'Name']).sum()  # Sum the 'Present' counts
        attendance_summary['Attendance'] = (attendance_summary['Present'] / len(filenames)) * 100  # Calculate percentage
        attendance_summary['Attendance'] = attendance_summary['Attendance'].apply(lambda x: f"{int(round(x))}%")  # Format as percentage
            

        # Save the summary to a CSV
        fileName = f"{subject_directory}/{Subject} totalAttendance.csv"
        attendance_summary.reset_index().to_csv(fileName, index=False)

        # Display attendance in the Tkinter window
        root = tkinter.Tk()
        root.title("Attendance of " + Subject)
        root.configure(background="black")
        fileName = f"{Subject} totalAttendance.csv"
        cs = os.path.join(subject_directory, fileName)
        
        with open(cs) as file:
            reader = csv.reader(file)
            r = 0

            for col in reader:
                c = 0
                for row in col:
                    label = tkinter.Label(
                        root,
                        width=10,
                        height=1,
                        fg="white",
                        font=("times", 15, " bold "),
                        bg="black",
                        text=row,
                        relief=tkinter.RIDGE,
                    )
                    label.grid(row=r, column=c)
                    c += 1
                r += 1
        root.mainloop()
        print(attendance_summary)

    subject = Tk()
    subject.title("Subject...")
    subject.geometry("580x320")
    subject.resizable(0, 0)
    subject.configure(background="black")

    titl = tk.Label(subject, bg="black", relief=RIDGE, bd=3, font=("arial", 30))
    titl.pack(fill=X)
    titl = tk.Label(
        subject,
        text="Subject Attendance",
        bg="black",
        fg="green",
        font=("arial", 25),
    )
    titl.place(x=100, y=12)

    def Attf():
        sub = tx.get()
        if sub == "":
            t = "Please enter the subject name!!!"
            text_to_speech(t)
        else:
            os.startfile(os.path.join(attendance_path, sub))

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
        text="View Attendance",
        command=calculate_attendance,
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

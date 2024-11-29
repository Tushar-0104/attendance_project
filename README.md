
# Attendance-Management

This is a Face Recognition-based Attendance System built using OpenCV and Python. The system uses a pre-trained Haar Cascade Classifier for face detection and LBPH (Local Binary Patterns Histograms) for face recognition. It allows real-time attendance marking for up to 50 students per session and stores the attendance records in a CSV file. The project includes a GUI developed using Tkinter, making it easy for users to select subjects and monitor attendance.

## Features

- **Face Detection**: Uses OpenCV’s Haar Cascade Classifier for high accuracy.
- **Face Recognition**: Implements LBPH face recognizer for real-time face identification with 85% recognition accuracy.
- **Real-Time Attendance**: Automatically marks attendance as soon as the face is recognized.
- **CSV Data Storage**: Attendance records are stored in CSV format for easy access and manipulation.
- **GUI Interface**: A user-friendly Tkinter-based GUI for subject selection and attendance monitoring.
- **Handles up to 50 Students** per session efficiently.

## Tech Stack

- **Programming Language**: Python
- **Libraries**: 
  - OpenCV (for face detection and recognition)
  - Pandas (for data handling)
  - Tkinter (for GUI)

## Run Locally

1. Clone the repository:
   ```bash
   git clone https://github.com/anubhavlal07/Attendance-Management.git
   cd Attendance-Management
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Ensure you have OpenCV installed:
   ```bash
   pip install opencv-python
   pip install opencv-contrib-python
   ```

4. Run the application:
   ```bash
   python attendance.py
   ```

## How it Works

1. **Face Detection**: The Haar Cascade Classifier detects faces from the webcam feed.
2. **Face Recognition**: LBPH face recognizer is used to identify the faces in real-time.
3. **Attendance Marking**: Once a face is recognized, the system records the student’s attendance with their ID, name, subject, and timestamp.
4. **CSV Storage**: The attendance data is saved in CSV format for further processing.

## Future Enhancements

- Add support for cloud-based data storage.
- Integrate with a database for better scalability.
- Implement a notification system for students/teachers.
- Add attendance analytics and reporting features.

## Contributing

Feel free to fork this repository and submit pull requests for any improvements or bug fixes. Contributions are always welcome!

## Screenshots
**homePage**
![App Screenshot](https://raw.githubusercontent.com/anubhavlal07/Attendance-Management/refs/heads/main/Project%20Snap/homePage.png)

**registerPage**
![App Screenshot](https://raw.githubusercontent.com/anubhavlal07/Attendance-Management/refs/heads/main/Project%20Snap/register.png)

**takeAttendance**
![App Screenshot](https://raw.githubusercontent.com/anubhavlal07/Attendance-Management/refs/heads/main/Project%20Snap/takeAttendance.png)

**checkAttendance**
![App Screenshot](https://raw.githubusercontent.com/anubhavlal07/Attendance-Management/refs/heads/main/Project%20Snap/checkAttendance.png)
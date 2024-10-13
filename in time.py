from sklearn.neighbors import KNeighborsClassifier
import cv2
import pickle
import numpy as np
import os
import csv
import time
from datetime import datetime


from win32com.client import Dispatch

def speak(str1):
    speak=Dispatch(("SAPI.SpVoice"))
    speak.Speak(str1)

video=cv2.VideoCapture(0)
facedetect=cv2.CascadeClassifier('haarcascade_frontalface_default .xml')

with open('data/names.pkl', 'rb') as w:
    LABELS = pickle.load(w)
with open('data/faces_data.pkl', 'rb') as f:
    FACES = pickle.load(f)

knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(FACES, LABELS)

attendance_log = {}

# Initialize video capture
video = cv2.VideoCapture(0)

while True:
    ret, frame = video.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = facedetect.detectMultiScale(gray, 1.3, 5)
    
    if len(faces) > 0:
        for (x, y, w, h) in faces:
            crop_img = frame[y:y+h, x:x+w, :]
            resized_img = cv2.resize(crop_img, (50, 25)).flatten().reshape(1, -1)
            output = knn.predict(resized_img)
            name = output[0]
            ts = time.time()
            date = datetime.fromtimestamp(ts).strftime("%d-%m-%Y")
            timestamp = datetime.fromtimestamp(ts).strftime("%H:%M:%S")
            file_path = f"Attendance_{date}.csv"
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 1)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (50, 50, 255), 2)
            cv2.rectangle(frame, (x, y-40), (x+w, y), (50, 50, 255), -1)
            cv2.putText(frame, str(name), (x, y-15), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1)

            if name not in attendance_log:
                attendance_log[name] = {'date': date, 'in_time': timestamp}

            with open(file_path, "w" if not os.path.isfile(file_path) else "a", newline='') as csvfile:
                writer = csv.writer(csvfile)
                if not os.path.isfile(file_path):
                    writer.writerow(['NAME', 'DATE', 'IN-TIME'])
                writer.writerow([name, attendance_log[name]['date'], attendance_log[name]['in_time']])
             


         
            

        break  # Exit after logging attendance

    if cv2.waitKey(1) & 0xFF != 255:
        break

video.release()
cv2.destroyAllWindows()
print(f"Signing in {name} at {timestamp} on {date}")

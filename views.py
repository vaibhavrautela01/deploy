import os
from django.shortcuts import render, redirect
import cv2
import numpy as np
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')
    
def name(request):
    return render(request, 'index.html')
    
def password(request):
    return render(request, 'index.html')


def face_detection(request):
    folder_path = 'C:/Users/raute/OneDrive/Desktop/mini project/home/images'  

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    video = cv2.VideoCapture(0)
    facedetect = cv2.CascadeClassifier('C:/Users/raute/OneDrive/Desktop/mini project/Face-RecognitionSystem/haarcascade_frontalface_default.xml')
    count = 0

    while True:
        ret, frame = video.read()
        faces = facedetect.detectMultiScale(frame, 1.3, 5)
        for x, y, w, h in faces:
            count += 1
            image_path = os.path.join(folder_path, f'image{count}.jpg')
            print("Creating Images........." + image_path)
            cv2.imwrite(image_path, frame[y:y+h, x:x+w])
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)
        cv2.imshow("WindowFrame", frame)
        cv2.waitKey(1)
        if count > 500:
            break

    video.release()
    cv2.destroyAllWindows()
    
    return render(request, 'index.html')


def button(request):
    return redirect('face_detection')

def test(request):
    return redirect('vaibhav')
   
def vaibhav(request):
    import cv2
import os


def vaibhav(request):
    import cv2
import os
from django.shortcuts import render

def capture_faces(request):
    if request.method == 'POST':
        video = cv2.VideoCapture(0)
        facedetect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        count = 0
        nameID = request.POST.get('name').lower()
        path = 'images/' + nameID
        isExist = os.path.exists(path)

        if isExist:
            return render(request, 'error.html', {'message': 'Name Already Taken'})

        os.makedirs(path)

        while True:
            ret, frame = video.read()
            faces = facedetect.detectMultiScale(frame, 1.3, 5)

            for x, y, w, h in faces:
                count = count + 1
                name = './images/' + nameID + '/' + str(count) + '.jpg'
                print("Creating Images........." + name)
                cv2.imwrite(name, frame[y:y + h, x:x + w])
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)

            cv2.imshow("WindowFrame", frame)
            cv2.waitKey(1)

            if count > 500:
                break

        video.release()
        cv2.destroyAllWindows()

        return render(request, 'success.html')

    return render(request, 'capture.html')

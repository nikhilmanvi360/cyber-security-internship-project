import cv2
import os
import numpy as np
import time

import sys

FACE_MODEL_FILE = "face_model.yml"

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def get_face_detector():
    # Check local directory first (for portable exe)
    local_path = resource_path("haarcascade_frontalface_default.xml")
    if os.path.exists(local_path):
        return cv2.CascadeClassifier(local_path)
    
    # Fallback to cv2 data
    cascade_path = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
    return cv2.CascadeClassifier(cascade_path)

def train_model():
    """Captures face samples from webcam and trains the model."""
    cam = cv2.VideoCapture(0)
    if not cam.isOpened():
        print("Error: Could not open webcam.")
        return False

    detector = get_face_detector()
    samples = []
    ids = []
    
    print("Capturing face data... Please look at the camera.")
    count = 0
    
    while True:
        ret, img = cam.read()
        if not ret:
            break
            
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = detector.detectMultiScale(gray, 1.3, 5)
        
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
            count += 1
            # Save the captured image into the datasets folder
            samples.append(gray[y:y+h, x:x+w])
            ids.append(1) # User ID 1
            
            cv2.imshow('Face Enrollment', img)
            
        if cv2.waitKey(100) & 0xFF == 27: # ESC to stop
            break
        elif count >= 30: # Take 30 face sample
            break
            
    cam.release()
    cv2.destroyAllWindows()
    
    if not samples:
        print("No face detected.")
        return False

    print("\nTraining model...")
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.train(samples, np.array(ids))
    recognizer.save(FACE_MODEL_FILE)
    print("Model trained and saved.")
    return True

def authenticate():
    """Authenticates the user using face recognition."""
    if not os.path.exists(FACE_MODEL_FILE):
        print("No face model found. Please run setup first.")
        return False

    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read(resource_path(FACE_MODEL_FILE))
    detector = get_face_detector()
    
    cam = cv2.VideoCapture(0)
    if not cam.isOpened():
        print("Error: Could not open webcam.")
        return False
        
    print("Authenticating... Look at the camera.")
    start_time = time.time()
    authenticated = False
    
    while True:
        ret, img = cam.read()
        if not ret:
            break
            
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = detector.detectMultiScale(gray, 1.2, 5)
        
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
            id, confidence = recognizer.predict(gray[y:y+h, x:x+w])
            
            # Check if confidence is less than 100 ==> "0" is perfect match 
            if confidence < 50:
                authenticated = True
                cv2.putText(img, f"Authenticated: {round(100 - confidence)}%", (x+5, y-5), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
            else:
                cv2.putText(img, "Unknown", (x+5, y-5), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
        
        cv2.imshow('Face Authentication', img)
        
        if authenticated:
            print("Authentication Successful!")
            time.sleep(1) # Show success briefly
            break
            
        if time.time() - start_time > 10: # Timeout after 10 seconds
            print("Authentication Timed Out.")
            break
            
        if cv2.waitKey(10) & 0xFF == 27:
            break
            
    cam.release()
    cv2.destroyAllWindows()
    return authenticated

if __name__ == "__main__":
    print("Testing Face Authentication...")
    if authenticate():
        print("Test Passed: Face Recognized!")
    else:
        print("Test Failed: Face Not Recognized.")

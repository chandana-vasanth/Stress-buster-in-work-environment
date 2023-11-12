from flask import Flask, render_template,request
import cv2
from io import BytesIO
import base64

app = Flask(__name__)

# Load Haarcascades classifiers for face and smile detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_smile.xml')

# OpenCV camera capture
cap = cv2.VideoCapture(0)

def detect_smile(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
   
    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
   
    for (x, y, w, h) in faces:
        roi_gray = gray[y:y+h, x:x+w]
       
        # Adjust the parameters for smile detection
        smiles = smile_cascade.detectMultiScale(roi_gray, scaleFactor=1.1, minNeighbors=20, minSize=(25, 25), flags=cv2.CASCADE_SCALE_IMAGE)
       
        # If a smile is detected, check its size
        if len(smiles) > 0:
            if smiles[0][2] * smiles[0][3] < 1000:  # Adjust this threshold based on your needs
                return "small_smile"  # Indicate a small smile
            else:
                return "big_smile"  # Indicate a sufficiently big smile
    
    return "no_smile"  # Indicate no smile detected

@app.route('/saycheese')
def say_cheese():
    # Capture a frame from the webcam
    ret, frame = cap.read()

    # Convert the frame to base64 for displaying in HTML
    _, buffer = cv2.imencode('.jpg', frame)
    img_str = base64.b64encode(buffer).decode('utf-8')

    # Check for a smile
    smile_status = detect_smile(frame)

    return render_template('say_cheese.html', img_data=img_str, smile_status=smile_status)




@app.route('/lowstress')
def low_stress_page():
    return render_template('lowstress.html')

@app.route('/guidepet')
def guide_pet():
    return "Guide your virtual pet for a moment of relaxation."

@app.route('/oneminutebreak')
def one_minute_break_page():
    return render_template('oneminutebreak.html')

@app.route('/handle_one_minute_break', methods=['POST'])
def handle_one_minute_break():
    activity = request.form.get('activity')

    if activity == 'meditation':
        return render_template('meditation.html')

    else:
        return "Invalid activity choice."

if __name__ == '__main__':
    app.run(debug=True)

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

# Function to detect smiles
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

# Route to display the "Say Cheese" page
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

# Route to display the low stress page
@app.route('/lowstress')
def low_stress_page():
    return render_template('lowstress.html')

# Route to display the low stress page
@app.route('/medstress')
def med_stress_page():
    return render_template('medstress.html')

# Route to handle one-minute break form submission
@app.route('/handle_one_minute_break')
def handle_one_minute_break():
    
    return render_template('meditation.html')
    
movies = [
    {"title": "PK", "link": "https://www.sonyliv.com/movies/pk-1000041836?utm_source=Google&utm_medium=WatchNow&utm_campaign=1000041836", "poster": "static/assets/images/pk.jpg"},
    {"title": "Queen", "link": "https://www.netflix.com/in/title/80032081?source=35", "poster": "static/assets/images/queen.jpg"},
    {"title": "Mr. Bean's Holiday", "link": "https://www.netflix.com/in/title/70060002?source=35", "poster": "static/assets/images/bean.jpg"},
    {"title": "3 Idiots", "link": "https://www.primevideo.com/dp/amzn1.dv.gti.6ab5ef5d-dd32-c5ab-3a8f-0aff6123c065?autoplay=0&ref_=atv_cf_strg_wb", "poster": "static/assets/images/3idiots.jpg"},
    {"title": "Yeh Jawaani Hai Deewani", "link": "https://www.netflix.com/in/title/70276515?source=35", "poster": "static/assets/images/yjhd.jpg"},
    {"title": "Rab Ne Bana Di Jodi", "link": "https://www.primevideo.com/dp/amzn1.dv.gti.34abea88-67e0-3261-7599-645cb107e723?autoplay=0&ref_=atv_cf_strg_wb", "poster": "static/assets/images/rabne.jpg"},
    {"title": "Baby's day out", "link": "https://www.primevideo.com/dp/amzn1.dv.gti.3ab984a4-cb87-3c08-c00d-5cb0c423c3c5?autoplay=0&ref_=atv_cf_strg_wb", "poster": "static/assets/images/baby.jpg"},
    {"title": "Home Alone", "link": "https://www.primevideo.com/dp/amzn1.dv.gti.22b56962-c47f-9cbd-32d6-5f0b5265da51?autoplay=0&ref_=atv_cf_strg_wb", "poster": "static/assets/images/home.jpg"}
]

@app.route('/movie')
def movie():
    return render_template('movie.html', movies=movies)

# Your existing route to render main.html
@app.route('/')
def index():
    return render_template('main.html')

# Your existing route to render stress.html
@app.route('/start')
def start():
    return render_template('stress.html')

questions = [
    {
        'text': 'How stressed are you today?',
        'options': ['Low', 'Medium', 'High'],
        'response': {
            'Low': "Don't be overstressed. Take a break and relax!",
            'Medium': "It's important to manage stress. Try some deep breathing exercises.",
            'High': "Take a deep breath. Consider talking to someone or taking a break to relax."
        }
    },
    {
        'text': 'How well did you sleep last night?',
        'options': ['Well', 'Okay', 'Poorly'],
        'response': {
            'Well': "Great! A good night's sleep is important for your well-being.",
            'Okay': "If you're having trouble sleeping, consider establishing a bedtime routine.",
            'Poorly': "Poor sleep can impact your day. Try creating a calm bedtime environment."
        }
    },
    {
        'text': 'What is one thing that usually brings a smile to your face, even on tough days?',
        'options': ['A funny joke', 'Watching a movie', 'Going out for a walk'],
        'response': {
            'A funny joke': "Okey, then let me crack a joke. Do you know Why the computer catch cold? Because it left its Windows open!",
            'Watching a movie': "Grab some popcorn and watch Yeh jawani hai diwani",
            'Going out for walk': "PS: Don't forget to take your pet!!"
        }
    },
    {
        'text': "If you were a superhero, what would your superpower be?",
        'options': ['Invisibility', 'Super strength', 'Teleportation'],
        'response': {
            'Invisibility': "Imagine all the fun pranks you could pull or the secret missions you could embark on. What would be the first thing you'd do if you were invisible?",
            'Super strength': "A powerhouse choice! You'd be the go-to hero for lifting cars and toppling villains",
            'Teleportation': "Teleportation, the ultimate travel power! No more traffic or long flights."
        }
    },
    {
        'text': "If you could instantly master any skill, what would it be?",
        'options': ['Playing a musical instrument', 'Super strength', 'Teleportation'],
        'response': {
            'Playing a musical instrument': "Oh great choice!",
            'Speaking a new language': "Oh great choice!",
            'Cooking like a chef': "Oh great choice!"
        }
    }
]

current_question_index = 0

@app.route('/chat',methods=['GET', 'POST'])
def chat():

    global current_question_index
    current_question = questions[current_question_index]

    if request.method == 'POST':
        user_answer = request.form['answer']

        if user_answer in current_question['response']:
            response = current_question['response'][user_answer]
        else:
            response = "I didn't understand your response. Please choose a valid option."

        current_question_index += 1

        if current_question_index < len(questions):
            current_question = questions[current_question_index]
        else:
            current_question = None

        return render_template('chat.html', question=current_question, response=response)

    return render_template('chat.html', question=current_question)

@app.route('/spinner')
def spinner():
    return render_template('movie.html')

@app.route('/meditate')
def meditate():
    return render_template('movie.html')

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, request

app = Flask(__name__)

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

@app.route('/', methods=['GET', 'POST'])
def index():
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

        return render_template('index.html', question=current_question, response=response)

    return render_template('index.html', question=current_question)

if __name__ == '__main__':
    app.run(debug=True)

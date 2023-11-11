from flask import Flask, render_template

app = Flask(__name__)

@app.route('/lowstress')
def low_stress_page():
    return render_template('lowstress.html')

@app.route('/saycheese')
def say_cheese():
    return "Take a moment to smile! 😊"

@app.route('/guidepet')
def guide_pet():
    return "Guide your virtual pet for a moment of relaxation."

@app.route('/oneminutebreak')
def one_minute_break():
    return "Take a 1-minute break. Breathe deeply and relax."


if __name__ == '__main__':
    app.run(debug=True)


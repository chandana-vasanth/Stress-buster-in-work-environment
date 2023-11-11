from flask import Flask, render_template, request

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

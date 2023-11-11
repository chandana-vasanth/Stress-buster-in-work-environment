from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample list of mental health assistants
assistants = [
    {"name": "John Doe", "phone": "123-456-7890", "email": "john.doe@example.com"},
    {"name": "Jane Smith", "phone": "987-654-3210", "email": "jane.smith@example.com"},
    # Add more assistants as needed
]

# Route to display the list of mental health assistants
@app.route('/')
def index():
    return render_template('appointment.html', assistants=assistants)

# Route to handle the booking form
@app.route('/book/<int:assistant_id>', methods=['GET', 'POST'])
def book(assistant_id):
    if request.method == 'POST':
        # Retrieve user input from the form
        user_name = request.form['name']
        user_phone = request.form['phone']
        user_email = request.form['email']

        # Process the booking (you can customize this part as needed)

        # Redirect to a confirmation page
        return render_template('confirmation.html', assistant=assistants[assistant_id], user_name=user_name)
    
    # Display the booking form
    return render_template('booking_form.html', assistant=assistants[assistant_id])

if __name__ == '__main__':
    app.run(debug=True)

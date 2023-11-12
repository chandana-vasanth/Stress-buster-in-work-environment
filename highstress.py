from flask import Flask, render_template, request, redirect, url_for
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

app = Flask(__name__)

# Sample list of mental health assistants
assistants = [
    {"assistant_id": "0", "name": "John Doe", "phone": "123-456-7890", "email": "john.doe@example.com"},
    {"assistant_id": "1", "name": "Jane Smith", "phone": "987-654-3210", "email": "jane.smith@example.com"},
    # Add more assistants as needed
]

# Function to send an email
def send_email(subject, body, to_email):
    sender_email = "themoodmentor@gmail.com"
    app_password = "fgiu mrzx nxjj bwly"  # Use environment variable for security

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = to_email
    message["Subject"] = subject

    message.attach(MIMEText(body, "plain"))

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender_email, app_password)
            server.sendmail(sender_email, to_email, message.as_string())
        print("Successfully Sent")
    except Exception as e:
        print(f"Error sending email: {e}")

# Route to display the list of mental health assistants
@app.route('/')
def index():
    return render_template('appointment.html', assistants=assistants)

# Route to handle the appointment form submission
@app.route('/process-form', methods=['POST'])
def process_form():
    if request.method == 'POST':
        name = request.form['name']
        phone = request.form['phone']
        email = request.form['email']
        pemail = request.form['pemail']
        date = request.form['date']
        time = request.form['time']

        # Add form validation here

        # Example usage
        subject = f"New Session Request for {name}"
        body = f"""
        Greetings!

        Mood Mentor has received a new session request for a user experiencing high stress levels.

        User Details:
        - Name: {name}
        - Email: {email}
        - Preferred Date: {date}
        - Preferred Time: {time}

        Please consider scheduling a session with the user at your earliest convenience.

        Thank you,
        Mood Mentor
        """
        recipient_email = email

        send_email(subject, body, recipient_email)

        return render_template('confirmation.html')

# Route to handle the booking form
# ...

# Route to handle the booking form
@app.route('/book', methods=['POST', 'GET'])
def book():
    if request.method == 'POST':
        # This means the form has been submitted
        assistant_id = request.form.get('assistant_id')
        user_name = request.form.get('name')
        user_phone = request.form.get('phone')
        user_email = request.form.get('email')

        # Process the booking (you can customize this part as needed)
        # For example, you might want to store the booking information in a database.

        # Redirect to a confirmation page
        return render_template('confirmation.html', user_name=user_name, assistant_id=assistant_id)


    # If it's a GET request (direct link), redirect to the appointment list
    return render_template('booking_form.html')


if __name__ == '__main__':
    app.run(debug=True)

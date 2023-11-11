import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(subject, body, to_email):
    # Your email credentials
    sender_email = "themoodmentor@gmail.com"
    app_password = "fgiu mrzx nxjj bwly"  # Replace with your App Password

    # Create the email message
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = to_email
    message["Subject"] = subject

    # Attach the body of the email
    message.attach(MIMEText(body, "plain"))

    # Connect to the SMTP server using SSL
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender_email, app_password)

        # Send the email
        server.sendmail(sender_email, to_email, message.as_string())

# Example usage
subject = "Emergency Mood Boost Alert from CareEttan!🚨"
body = """Greetings!

 I'm CareEttan, your friendly neighborhood stress-busting companion from Mood Mentor, here with an urgent transmission.

🚨 Stress levels detected: HIGH! 🚨

Alert! Stress vibes detected around [Employee's Name]—our superhero in distress! 🚨🦸‍♂ Time for a CareEttan intervention!

As the Care Ambassador, it's my sworn duty to make sure your superhero hangout stays as chill as an ice cream cone in Antarctica! 🍦❄

PS: Treat this as an official alert! Take necessary steps to make our superhero comfortable at work, ensuring peak productivity. 🚀💪

If you need any more mood-boosting maneuvers, just give me a shout. I'm here 24/7, because who needs stress when you've got CareEttan on speed dial? 📞😎

Sending cyber-hugs your way,

CareEttan
Your Mood Mentor Companion 🌈
"""
recipient_email = "pkd20bit342@gecskp.ac.in"

send_email(subject, body, recipient_email)
print("Sucessfully Sent")
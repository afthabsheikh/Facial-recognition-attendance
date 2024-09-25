import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(sender_email, sender_password, receiver_email):
    try:
        subject = "Attendance"
        message = "Your attendance was succesfully applied.Thank you"

        # Set up the MIME
        message_body = MIMEMultipart()
        message_body['From'] = sender_email
        message_body['To'] = receiver_email
        message_body['Subject'] = subject

        # Attach the message to the MIME
        message_body.attach(MIMEText(message, 'plain'))

        # Create SMTP session for sending the mail
        session = smtplib.SMTP('smtp.gmail.com', 587)  # Use your email provider's SMTP server and port
        session.starttls()  # Enable TLS
        session.login(sender_email, sender_password)  # Login using your email credentials
        text = message_body.as_string()
        session.sendmail(sender_email, receiver_email, text)  # Send the email
        session.quit()
        print("Email sent successfully!")
    except Exception as e:
        print("Email sending failed.")
        print(e)

def main():
    # Email credentials and details
    sender_email = "afthabsheikh11710@gmail.com"  # Replace with your sender email
    sender_password = "eift tbkw pvmi drxu"  # Replace with your sender email password
    receiver_email = input("Enter receiver's email: ")

    # Send the email
    send_email(sender_email, sender_password, receiver_email)

if __name__ == "__main__":
    main()
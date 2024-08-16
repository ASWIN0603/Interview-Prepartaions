import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Replace with your information
sender_email = "innovation4th@gmail.com"
sender_password = "Inno4@th"
receiver_email = "aswinraja8098@gmail.com"

# Create the email
msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = receiver_email
msg['Subject'] = "Sample Email"

# Email body
body = "Dear Client,\n\nThis is a sample email sent from a Python script.\n\nBest Regards,\nYour Name"
msg.attach(MIMEText(body, 'plain'))

# Send the email
try:
    # Connect to the server
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()  # Secure the connection
    server.login(sender_email, sender_password)

    # Send the email
    text = msg.as_string()
    server.sendmail(sender_email, receiver_email, text)
    
    print("Email sent successfully!")
except Exception as e:
    print(f"Failed to send email: {e}")
finally:
    server.quit()

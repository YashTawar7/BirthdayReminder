import smtplib
import time
from email.message import EmailMessage


def sendEmail(receiver, email_list, birthday_person_name):
    # Email configuration
    sender_email = 'noreply@mastechdigital.com'
    receiver_email = receiver
    password = 'M@$te(h@$MTP$$'
    subject = 'Birthday Notification'
    message = "Hi" f" {birthday_person_name},""\n"f"\nWishing you a day filled with love, joy, and all the things that make you smile. May this year bring you new adventures, wonderful opportunities, and endless happiness." \
              f"Enjoy every moment of your special day!" \
              "\n"f"\nWish you a very Happy Birthday!" f" {birthday_person_name}." f"\n" f"\nRegards" f"\nQE Family"

    # Create a multipart message and set the headers
    msg = EmailMessage()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg['Cc'] = email_list
    msg.set_content(message)

    # Connect to the SMTP server
    smtp = smtplib.SMTP('smtp.office365.com', 587)
    smtp.starttls()  # Enable encryption
    smtp.login(sender_email, password)

    # Send the email
    smtp.send_message(msg)

    # Disconnect from the SMTP server
    smtp.quit()

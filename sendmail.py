# import library to link to gmail
import smtplib
from email.message import EmailMessage


def sendemail(email):
    msg = EmailMessage()
    # Content of the email
    msg.set_content("Your account has been successfully created!")

    # Subject of the email
    msg['Subject'] = 'Welcome to Wallet Wise!'
    # Specify the sender email
    msg['From'] = "teamwalletwise@gmail.com"
    # Specify the receiver email
    msg['To'] = email
    # Sender password
    password = "walletwise21"
    # Send the message via our own SMTP server (465)
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    # Log into the server email
    server.login("teamwalletwise@gmail.com", password)
    # Send message to receiver
    server.send_message(msg)
    # Print message to confirm that email has been sent
    print("Your account has been successfully created!")
    return
    server.quit()

# sendemail()
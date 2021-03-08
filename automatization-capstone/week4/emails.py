def generate_email(username):

    from email.message import EmailMessage
    import mimetypes
    import os

    message = EmailMessage()

    recipient = f"{username}@example.com"
    sender = "Automation@example.com"

    message['From'] = sender
    message['To'] = recipient

    message['Subject'] = 'Upload Completed = Online Fruit Store'
    
    body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
    message.set_content(body)

    mime_type, _ = mimetypes.guess_type("/tmp/processed.pdf")
    mime_type, mime_subtype = mime_type.split('/', 1)
    with open("/tmp/processed.pdf", 'rb') as ap:
        message.add_attachment(ap.read(),
        maintype = mime_type,
        subtype = mime_subtype,
        filename = os.path.basename("/tmp/processed.pdf"))
    
    return message

def generate_issue_email(username, subject):

    from email.message import EmailMessage

    message = EmailMessage()

    recipient = f"{username}@example.com"
    sender = "automation@example.com"

    message['From'] = sender
    message['To'] = recipient

    message['Subject'] = subject

    body = "Please check your system and resolve the ussue as soon as possible"

    message.set_content(body)

    return message

def send_email(username, password, message):
    import smtplib

    recipient = f"{username}@example.com"
    mail_server = smtplib.SMTP_SSL('smtp.example.com')
    mail_server.login(recipient, password)
    mail_server.send_message(message)
    mail_server.quit()
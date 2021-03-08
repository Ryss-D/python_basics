#The Simple Mail Transfer Protocol (SMTP) and Multipurpose Internet Mail Extensions (MIME) standards define how email messages are constructed. You could read the standards documentation and create email messages all on your own, but you don't need to go to all that trouble. The email built-in Python module lets us easily construct email messages.

from email.message import EmailMessage
message = EmailMessage()
print(message)
#then we create a empty message

sender = "me@example.com"
recipient = "you@example.com"

message['From'] = sender
message['To'] = recipient
print(message)

message['Subject'] = 'Greetings from {} to {}!'.format(sender, recipient)
print(message)

body = """Hey there!

    I'm learning to send emails using Python"""
message.set_content(body)
print(message)

##In order for the recipient of your message to understand what to do with an attachment, you  need to label the attachment with a MIME type and subtype to tell them what sort of file you’re sending. The Internet Assigned Numbers Authority (IANA) (iana.org) hosts a registry of valid MIME types. If you know the correct type and subtype of the files you’ll be sending, you can use those values directly. If you don't know, you can use the Python mimetypes module to make a good guess!

import os.path
attachment_path = "C:\\Users\\LENOVO\\Downloads\\2021-01-20.png"
attachment_filename = os.path.basename(attachment_path)
import mimetypes
mime_type, _ = mimetypes.guess_type(attachment_path)
print(mime_type)

mime_type, mime_subtype = mime_type.split('/', 1)
print(mime_type)
print(mime_subtype)

# with open(attachment_path, 'rb') as ap:
#     message.add_attachment(ap.read(),
#         maintype = mime_type,
#         subtype = mime_subtype,
#         filename = os.path.basename(attachment_path))
# print(message)

import smtplib

# mail_server = smtplib.SMTP('localhost')
mail_server = smtplib.SMTP_SSL('smtp.example.com')
#If you want to see the SMTP messages that are being sent back and forth by the smtplib module behind the scenes, you can set the debug level on the SMTP or SMTP_SSL object. The examples in this lesson won’t show the debug output, but you might find it interesting!
#mail_server.set_debuglevel(1)

import getpass 
mail_pass = getpass.getpass('Password? ')
print(mail_pass)

mail_server.login(sender, mail_pass)
#If the login attempt succeeds, the login method will return a tuple of the SMTP status code and a message explaining the reason for the status. If the login attempt fails, the module will raise a SMTPAuthenticationError exception.

mail_server.send_message(message)
mail_server.quit()
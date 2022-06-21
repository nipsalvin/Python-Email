import smtplib

server = smtplib.SMTP("emailserver.com", 465) # SMTP server and port number

server.starttls()

server.login("sender@email.com", "email_password")

server.sendmail("sender@email.com", "recepient@email.com", "This mail is sent from python")

print("Mail sent successfully")

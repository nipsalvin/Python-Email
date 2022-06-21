import smtplib

server = smtplib.SMTP("emailserver.com", 465"""port number""")

server.startssl()

server.login("sender@email.com", "email_password")

server.sendmail("sender@email.com", "recepient@email.com", "This mail is sent from python")

print("Mail sent successfully")

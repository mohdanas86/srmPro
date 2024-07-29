import random, smtplib
def sent(receiver_email, msg):
        
        sender_email = "noreplysrmistcs@gmail.com"
        sender_password = "sntgcdudppycsfny"

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()

        server.login(sender_email, sender_password)

        subject = "Appraisal Form Query - Urgent"
        body = msg
        message = f"Subject: {subject}\n\n{body}"

        server.sendmail(sender_email, receiver_email, message)

        server.quit()  
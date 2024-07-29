import random, smtplib
def otp_verification(receiver_email):
        otp = str(random.randint(100000, 999999))

        sender_email = "noreplysrmistcs@gmail.com"
        sender_password = "sntgcdudppycsfny"

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()

        server.login(sender_email, sender_password)

        subject = "Your OTP"
        body = f"Your OTP is: {otp}"
        message = f"Subject: {subject}\n\n{body}"

        server.sendmail(sender_email, receiver_email, message)

        server.quit()  
        return otp  
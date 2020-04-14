from __future__ import print_function
import smtplib
import re

def accept_input():
    email = ""
    try:
        email = raw_input("Target COMPANY E-Mail: ")
    except:
        email = input("Target COMPANY E-Mail: ")

    while not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        print("\nI am sorry, you must enter a valid email\n")
        try:
            email = raw_input("Target COMPANY E-Mail: ")
        except:
            email = input("Target COMPANY E-Mail: ")
    return email


def send_mail(email):
    subject = "Ich verkaufe leckere Wurst"
    text = """
Guten Tag,

mein name ist Peter Wiener und ich verkaufe Wurst.
Bitte kaufen Sie meine leckere Wurst.

Hochachtungsvoll,
Peter Wiener
    """
    sender = email
    receivers = [email]
    message = 'Subject: {}\n\n{}'.format(subject, text)


    try:
        smtpObj = smtplib.SMTP('mailgate.COMPANY.com', 25)
        smtpObj.sendmail(sender, receivers, message)
        return "Successfully sent email"
    except SMTPException:
        return "Error: unable to send email, did you enter a @COMPANY.com"


def show_output(response):
    print(response)


def main():
    email    = accept_input()
    response = send_mail(email)
    show_output(response)


if __name__ == "__main__":
    main()

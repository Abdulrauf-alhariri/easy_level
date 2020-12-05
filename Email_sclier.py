def email_sclier():
    email = input("Enter your email \n>>>")
    user_name = email[: email.index("@") + 1]
    domain = email[email.index("@") + 1:]

    print(f"You're user name {user_name} and domain {domain}")


email_sclier()

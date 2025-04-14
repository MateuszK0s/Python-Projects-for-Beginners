email = input("Enter your email account name: ").strip()
email = email.split("@")

print(f"Your username is {email[0]} and your domain is {email[1]}")

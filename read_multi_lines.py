# Reading multiple lines from a file
with open('emails.txt', 'r') as file:
    content = file.readlines()

print("Looking for icloud emails")
for email in content:
    if 'icloud' in email:
        print(f"Found icloud email: {email.strip()}")

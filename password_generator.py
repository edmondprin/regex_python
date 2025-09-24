import secrets
import string

'''
my_password = secrets.token_urlsafe(5)
print(my_password)
'''
# Generate 8-character long alphanumeric password

alphabet = string.ascii_letters + string.digits
password = "".join(secrets.choice(alphabet) for i in range(8))

print(f"My test password is {password}")
print(sum(c.isdigit() for c in password))


# Generate password with at least 1 uppercase letter, at least 1 lowercase letter, 3 digits minimum and 2 special characters


alphabet = string.ascii_letters + string.digits + string.punctuation
while True:
    password = "".join(secrets.choice(alphabet) for i in range(8))
    if (any(c.islower() for c in password) and any(c.isupper() for c in password) and sum(c.isdigit() for c in password) >= 3) and sum(c in string.punctuation for c in password) >= 2:
        break 
print(password)


# Generate an XKCD-style paraphrase

with open('/usr/share/dict/words') as f: # On standard Linux systems, use a convenient dictionary file.
    words = [word.strip() for word in f]
    password = ' '.join(secrets.choice(words) for i in range(4))
print(password)
import secrets
import string

letters = string.ascii_letters
numbers = string.digits
special_chars = string.punctuation

alphabet = letters + numbers + special_chars

password_length = input("Enter the desired password length: ")

generated_password = ''

for i in range(int(password_length)):
  generated_password +=  ''.join(secrets.choice(alphabet))

print(generated_password)
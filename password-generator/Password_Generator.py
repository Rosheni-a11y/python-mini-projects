import random
import string

def generate_password(length, use_numbers,use_symbols):
  characters = string.ascii_letters

  if use_numbers:
    characters += string.digits

  if use_symbols:
    characters += string.punctuation

  password = ""
  for i in range(length):
    random_char = random.choice(characters)
    password += random_char

  return password

print("Password Generator \n")

while True:

  length = int(input("How long should the password be? "))

  use_numbers = input("Include numbes? (yes/no): ").lower()
  use_symbols = input("Include symbols? (yes/no): ").lower()

  if use_numbers == "yes":
    use_numbers = True
  else:
    use_numbers = False
  
  if use_symbols == "yes":
    use_symbols= True
  else:
    use_symbols = False

  password = generate_password(length,use_numbers,use_symbols)

  print(f"\n Your password: {password}\n")

  again = input("Generate another password? (yes/no): ").lower()
  if again != "yes":
    print("\nThanks for using Password Generator! ")
    break
print("PASSWORD STRENGTH CHECKER")

password = input("Enter your password to check its strength: ")
print(f"Entered Password is: {password}")

length = len(password)
print(f"The length of entered password is : {lenght}") # f-string is better than print(str, val)

complexity = 4
has_uppercase = False
has_symbols = False
has_digits = False

for char in password:
    if char.isupper():
        has_uppercase = True
    if char.isdigit():
        has_digits = True
    if not char.isalnum():
        has_symbols = True

if length < 8:
    print("Your password is too short.")
    complexity -= 1

# If even one of the three (has_digits, has_symbols, has_uppercase) is falsy:
if not all([has_digits, has_symbols, has_uppercase]):
    if not has_digits:
        print("Add at least one digit to make the password stronger.")
        complexity -= 1
    if not has_symbols:
        print("Add at least one symbol to improve password security.")
        complexity -= 1
    if not has_uppercase:
        print("Add at least one uppercase letter to improve password strength.")
        complexity -= 1

match complexity:
    case 4:
        print("Your password is strong.")
    case 3:
        print("Your password is medium.")
    case 2:
        print("Your password is medium.")
    case 1:
        print("Your password is weak.")
    case 0:
        print("Your password is too weak; it's recommended that you change it.")

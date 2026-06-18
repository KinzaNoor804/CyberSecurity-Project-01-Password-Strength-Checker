print("PASSWORD STRENGTH CHECKER")

password = input("Enter your password to check its strength: ")
print("Entered Password is: ", password)

length = len(password)
print("The length of entered password is : ", length)

hasUpperCase = False;
hasSymbols = False;
hasDigits = False;

for char in password:
    if char.isupper():
        hasUpperCase = True;
    if char.isdigit():
        hasDigits = True
    if not char.isalnum():
        hasSymbols = True;


if length < 8:
    print("Your password is weak.")

elif hasDigits and hasSymbols and hasUpperCase:
    print("Your password is strong.")

elif hasUpperCase and hasDigits:
    print("Your password is medium.")
else:
    print("Your password is weak.")

if not hasUpperCase or not hasDigits or  not hasSymbols:
    print("Suggestions:")

    if not hasDigits:
        print("Add at least one digit to make the password stronger.")
    if not hasSymbols:
        print("Add at least one symbol to improve password security.")
    if not hasUpperCase:
        print("Add at least one uppercase letter to improve password strength.")









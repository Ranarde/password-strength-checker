# Get password input without displaying it on the screen
from getpass import getpass

print( "================================")
print( "      PASSWORD STRENGTH CHECKER" )
print( "================================")

password = getpass( "Enter a password: ")

# Check password length
if len(password) >= 12:
    print( "Length: Good")
else:
    print( "Length: Weak (should be at least 12 characters)")   
# Check for uppercase letters
if any(char.isupper() for char in password):
    print( "Uppercase: Good ")
else:
    print( "Uppercase: Missing (should contain at least one uppercase letter)")      
# Check for lowercase letters
if any(char.islower() for char in password):
    print( "Lowercase: Good ")
else:
    print( "Lowercase: Missing (should contain at least one lowercase letter)")
# Check for numbers
if any(char.isdigit() for char in password):
    print( "Number: Good ")
else:
    print( "Number: Missing (should contain at least one number)")
# Check for special characters
if any(not char.isalnum() for char in password):
    print( "Special Character: Good ")
else:
    print( "Special Character: Missing (should contain at least one special character)")
# Calculate password strength score
score = 0
if len(password) >= 12:
    score += 1
if any(char.isupper() for char in password):
    score += 1
if any(char.islower() for char in password):
    score += 1
if any(char.isdigit() for char in password):
    score += 1
if any(not char.isalnum() for char in password):
    score += 1


print()
print("===============================")
print( "Password Strength Score: ", score, "/ 5" )


if score >= 4:
    print( "Overall: Strong" )
elif score >= 3:
    print( "Overall: Moderate" )
else:
    print( "Overall: Weak" )
    print("===============================")
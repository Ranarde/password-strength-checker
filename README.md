# Password Strength Checker

A Python-based password strength checker that evaluates common password security requirements.

## Features

- Checks password length
- Checks for uppercase letters
- Checks for lowercase letters
- Checks for numbers
- Checks for special characters
- Calculates a password strength score from 0–5
- Classifies passwords as Weak, Moderate, or Strong
- Hides password input using Python's `getpass` module

## Technologies Used

- Python
- Visual Studio Code
- GitHub

## How It Works

The program evaluates a password against five security requirements:

1. Minimum length of 12 characters
2. At least one uppercase letter
3. At least one lowercase letter
4. At least one number
5. At least one special character

Each requirement earns one point.

### Strength Rating

| Score | Rating |
|---|---|
| 0–2 | Weak |
| 3–4 | Moderate |
| 5 | Strong |

## Example

```text
PASSWORD STRENGTH CHECKER

Enter a password:

Length: Good
Uppercase: Good
Lowercase: Good
Number: Good
Special Character: Good

Password Strength Score: 5/5
Overall: Strong
```

Markdown

## Example Output
![Password Strength Checker Output](<Screenshot 2026-08-20 214158.png>)

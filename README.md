# Password Strength Checker

This is a simple password strength checker built using Python's `tkinter` library for the GUI and `re` (regular expressions) for password validation. The program evaluates the strength of a password based on specific criteria and provides feedback on how to improve it.

## Features
- **Password Validation**: The program checks the password based on length, lowercase letters, uppercase letters, digits, and special characters.
- **Detailed Feedback**: If the password is weak or moderate, the user receives detailed suggestions to improve its strength.
- **GUI**: The application provides a user-friendly graphical interface for password evaluation using `tkinter`.
- **Interactive**: Results and suggestions are shown in a popup message box for better user experience.

## Prerequisites

To run this project, you need to have Python installed on your system along with the `tkinter` library. `tkinter` typically comes pre-installed with Python, but in case it's missing, you can install it via:

```bash
sudo apt-get install python3-tk # For Linux
```
## How to Run

Clone the repository:

```bash
git clone https://github.com/Yusuf611/password-strength-checker.git
```
cd password-strength-checker
Run the script:

```bash
python password_checker.py
```
A GUI window will appear where you can enter your password and check its strength.

## Password Strength Criteria

The password is evaluated based on the following:

- Length: Must be at least 8 characters.

- Lowercase Letters: Should contain at least one lowercase letter.

- Uppercase Letters: Should contain at least one uppercase letter.

- Numbers: Should contain at least one digit.

- Special Characters: Should contain at least one special character (e.g., @, #, $, etc.).

The password can be classified into the following categories:

- Strong: Meets all the criteria.

- Moderate: Misses one criterion.

- Weak: Misses two or more criteria.

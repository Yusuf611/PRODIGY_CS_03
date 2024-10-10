import re
import tkinter as tk
from tkinter import messagebox

def check_password_strength(password):
    strength = 0
    feedback = []

    if len(password) < 3:
        feedback.append("Your password is too short to be secure. A password with fewer than 3 characters is extremely weak and vulnerable. Please use a longer password.")
        return "Very weak password.", feedback

    if len(password) >= 8:
        strength += 1
    else:
        feedback.append("Password should be at least 8 characters long to ensure better security.")

    if re.search("[a-z]", password):
        strength += 1
    else:
        feedback.append("Password should contain at least one lowercase letter.")

    if re.search("[A-Z]", password):
        strength += 1
    else:
        feedback.append("Password should contain at least one uppercase letter.")

    if re.search("[0-9]", password):
        strength += 1
    else:
        feedback.append("Password should contain at least one digit.")

    if re.search("[@#$%^&+=!]", password):
        strength += 1
    else:
        feedback.append("Password should contain at least one special character (e.g., @, #, $, etc.).")

    if strength == 5:
        return "Strong password!", feedback
    elif strength == 4:
        return "Moderate password.", feedback
    else:
        return "Weak password.", feedback

def evaluate_password():
    password = entry.get()
    result, suggestions = check_password_strength(password)
    result_label.config(text=result)
    
    if suggestions:
        suggestions_text = "\n".join(f"- {s}" for s in suggestions)
        messagebox.showinfo("Suggestions to Improve Your Password", suggestions_text)
    else:
        messagebox.showinfo("Success", "Your password meets all the criteria!")

root = tk.Tk()
root.title("Password Strength Checker")

tk.Label(root, text="Enter your password:").pack(pady=10)
entry = tk.Entry(root, show="*", width=30)
entry.pack(pady=5)

check_button = tk.Button(root, text="Check Strength", command=evaluate_password)
check_button.pack(pady=10)

result_label = tk.Label(root, text="", font=("Helvetica", 12, "bold"))
result_label.pack(pady=5)

root.mainloop()

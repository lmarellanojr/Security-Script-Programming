from cProfile import label
import re
import getpass
import tkinter as tk
from tkinter import messagebox

def assess_password_strength(password):
    criteria_score = 0

    common_passwords = ['password', '123456', 'qwerty', 'admin', 'letmein']
    dictionary_words = ['apple', 'house', 'car', 'dog', 'love']

    #common password and dictionary word checks
    is_common = password.lower() in common_passwords
    is_contains = any(word in password.lower() for word in dictionary_words)

    if not is_common:
        criteria_score += 1
    if not is_contains:
        criteria_score += 1

    #Criteria checks
    if len(password) >= 12:
        criteria_score += 1
    if re.search(r'[A-Z]', password):
        criteria_score += 1
    if re.search(r'[a-z]', password):
        criteria_score += 1
    if re.search(r'[0-9]', password):
        criteria_score += 1
    if re.search(r'[!@#$%^&*()_\+\-=\[\]\{\};:\'\",.<>?/\\|]', password):
        criteria_score += 1

    print("DEBUG: score:", criteria_score)

    #score assessment
    if criteria_score <= 3 or is_common or is_contains:
        strength = "Weak"
    elif criteria_score in [4, 5]:
        strength = "Moderate"
    elif criteria_score >= 6 and not is_common and not is_contains:
        strength = "Strong"
    else:
        strength = "Moderate"

    return strength

#Main App Window
app = tk.Tk()
app.title("Password Strength Assessor")

frame = tk.Frame(app, padx=20, pady=20)
frame.pack()

label = tk.Label(frame, text="Enter Password to Assess:")
label.pack(pady=10)
entry = tk.Entry(frame, show="*")
entry.pack(pady=5)

def check_password():
    password = entry.get()
    strength = assess_password_strength(password)
    messagebox.showinfo("Password Strength", f"Password Strength: {strength}")

button = tk.Button(app, text="Check Password", command=check_password)
button.pack(pady=10)

app.mainloop()
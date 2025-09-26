import re
import tkinter as tk
from tkinter import messagebox


def assess_password_strength(password: str) -> str:
    score = 0

    # Criteria checks
    if len(password) >= 8:
        score += 1
    if len(password) >= 12:
        score += 1
    if re.search(r"[A-Z]", password):
        score += 1
    if re.search(r"[a-z]", password):
        score += 1
    if re.search(r"[0-9]", password):
        score += 1
    if re.search(r"[^A-Za-z0-9]", password):
        score += 1

    # Strength classification
    if score <= 2:
        return "Weak"
    elif score == 3 or score == 4:
        return "Moderate"
    elif score == 5:
        return "Strong"
    else:
        return "Very Strong"


def check_password():
    password = entry.get()
    if not password:
        messagebox.showwarning("Input Error", "Please enter a password")
        return
    strength = assess_password_strength(password)
    result_label.config(text=f"Strength: {strength}")


# GUI Setup
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("400x200")
root.resizable(False, False)

frame = tk.Frame(root, padx=20, pady=20)
frame.pack(expand=True)

label = tk.Label(frame, text="Enter your password:", font=("Arial", 12))
label.pack(pady=5)

entry = tk.Entry(frame, show="", width=30, font=("Arial", 12))
entry.pack(pady=5)

check_button = tk.Button(frame, text="Check Strength", command=check_password, font=("Arial", 12))
check_button.pack(pady=10)

result_label = tk.Label(frame, text="", font=("Arial", 12, "bold"))
result_label.pack(pady=5)

root.mainloop()

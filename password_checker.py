import tkinter as tk
from tkinter import messagebox
import re
import random
import string

def check_strength():
    password = entry.get()
    strength = 0
    remarks = []

    if len(password) >= 8:
        strength += 1
    else:
        remarks.append("At least 8 characters")

    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        remarks.append("Add an uppercase letter")

    if re.search(r"[a-z]", password):
        strength += 1
    else:
        remarks.append("Add a lowercase letter")

    if re.search(r"\d", password):
        strength += 1
    else:
        remarks.append("Add a digit")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1
    else:
        remarks.append("Add a special character")

    if strength == 5:
        result_label.config(text="✅ Strong Password", fg="green")
    elif 3 <= strength < 5:
        result_label.config(text="⚠ Moderate Password", fg="orange")
    else:
        result_label.config(text="❌ Weak Password", fg="red")

    suggestions_label.config(text="\n".join(remarks), fg="gray")

def suggest_passwords(event=None):
    base = entry.get().strip()
    suggestions = []

    if len(base) > 2:
        capitalized = base.capitalize()
        patterns = ["@123", "2024#", "_321!", "World@1", "!Secure"]
        for pattern in random.sample(patterns, 3):
            suggestions.append(capitalized + pattern)

        password_suggestions_label.config(
            text="💡 Try these strong passwords:\n" + "\n".join(suggestions), fg="blue"
        )
    else:
        password_suggestions_label.config(text="")

# ==== GUI SETUP ====
root = tk.Tk()
root.title("Password Strength Checker")
root.iconify()
root.minsize(600, 400)
root.state("zoomed")
root.resizable(True, True)

# Create a container Frame (centered manually)
container = tk.Frame(root)

# All widgets inside container
title = tk.Label(container, text="Password Strength Checker", font=("Helvetica", 18, "bold"))
title.pack(pady=10)

entry = tk.Entry(container, font=("Helvetica", 14), width=30)
entry.pack(pady=10)
entry.bind("<KeyRelease>", suggest_passwords)

check_btn = tk.Button(container, text="Check Strength", command=check_strength, font=("Helvetica", 12))
check_btn.pack(pady=5)

result_label = tk.Label(container, text="", font=("Helvetica", 14))
result_label.pack(pady=5)

suggestions_label = tk.Label(container, text="", font=("Helvetica", 10), justify="center")
suggestions_label.pack(pady=5)

password_suggestions_label = tk.Label(container, text="", font=("Helvetica", 10), justify="center")
password_suggestions_label.pack(pady=5)

# Function to center the container when window resizes
def center_container(event=None):
    win_width = root.winfo_width()
    win_height = root.winfo_height()
    container.update_idletasks()
    frame_width = container.winfo_width()
    frame_height = container.winfo_height()

    x = (win_width - frame_width) // 2
    y = (win_height - frame_height) // 2

    container.place(x=x, y=y)

# Bind the resize event
root.bind("<Configure>", center_container)

# Initial center
center_container()

root.mainloop()

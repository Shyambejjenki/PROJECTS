import tkinter as tk
from tkinter import messagebox
import random
import string

# Function to generate password
def generate_password():
    length = int(length_var.get())
    use_upper = upper_var.get()
    use_lower = lower_var.get()
    use_digits = digit_var.get()
    use_symbols = symbol_var.get()

    characters = ''
    if use_upper:
        characters += string.ascii_uppercase
    if use_lower:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        messagebox.showwarning("Warning", "Select at least one character type!")
        return

    password = ''.join(random.choice(characters) for _ in range(length))
    password_var.set(password)
    update_strength(password)

# Function to update password strength
def update_strength(password):
    strength = "Weak"
    if len(password) >= 12 and any(c in string.punctuation for c in password):
        strength = "Strong"
    elif len(password) >= 8:
        strength = "Medium"

    strength_var.set(f"Strength: {strength}")

# Function to copy password to clipboard
def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(password_var.get())
    messagebox.showinfo("Copied", "Password copied to clipboard!")

# GUI Setup
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x300")
root.resizable(False, False)

# Variables
length_var = tk.StringVar(value='12')
upper_var = tk.BooleanVar(value=True)
lower_var = tk.BooleanVar(value=True)
digit_var = tk.BooleanVar(value=True)
symbol_var = tk.BooleanVar(value=True)
password_var = tk.StringVar()
strength_var = tk.StringVar(value="Strength: ")

# Widgets
tk.Label(root, text="Password Length:").pack(pady=5)
tk.Entry(root, textvariable=length_var, width=5).pack()

tk.Checkbutton(root, text="Include Uppercase Letters", variable=upper_var).pack()
tk.Checkbutton(root, text="Include Lowercase Letters", variable=lower_var).pack()
tk.Checkbutton(root, text="Include Digits", variable=digit_var).pack()
tk.Checkbutton(root, text="Include Symbols", variable=symbol_var).pack()

tk.Button(root, text="Generate Password", command=generate_password).pack(pady=10)
tk.Entry(root, textvariable=password_var, font=('Arial', 14), justify='center', state='readonly').pack(pady=5)
tk.Label(root, textvariable=strength_var, font=('Arial', 12)).pack()

tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard).pack(pady=10)

root.mainloop()


import tkinter as tk
from tkinter import messagebox
import random
import string

"""
Password Generator
------------------

Description:
This Python program generates customizable passwords through a graphical user interface (GUI) built with Tkinter.
Users can specify the password length and choose the number of special characters, digits, uppercase letters, and lowercase letters.
The program includes real-time validation to ensure the input is correct and displays error messages if needed.
Additionally, the generated password can be copied to the clipboard for easy use.

Author: Leah Orenstein
October 2024
"""


def generate_password():
    """
    Generate a password based on user-specified criteria.
    
    This function reads the values from the GUI spinboxes, validates the input,
    and generates a password that meets the specified criteria.
    """
    length = int(passLngth.get())
    characters = string.ascii_letters + string.digits + string.punctuation

    specials = int(specChars.get())
    digits = int(digChars.get())
    uppers = int(upperChars.get())
    lowers = int(lowerChars.get())
    print(lowers)
    rands = length - (digits + specials + uppers + lowers)
    if specials + digits + uppers + lowers > length:
        messagebox.showinfo("Error", "Length is too short for the required characters")
        reset_spinboxes()
        return

    requiredChars = {"spec": specials, "dig": digits, "upper": uppers, "lower": lowers, "random": rands}
    password = ''

    for i in range(length):
        # Deleting the keys with value 0
        listKeys = list(requiredChars.keys())
        for key in listKeys:
            if requiredChars[key] == 0:
                del requiredChars[key]

        key = random.choice(list(requiredChars.keys()))
        requiredChars[key] -= 1

        if key == "spec":
            password = password + random.choice(string.punctuation)
        elif key == "dig":
            password = password + random.choice(string.digits)
        elif key == "upper":
            password = password + random.choice(string.ascii_uppercase)
        elif key == "lower":
            password = password + random.choice(string.ascii_lowercase)
        else:
            password = password + random.choice(characters)

    labelPassword.config(text=password)
    passwordFrame.pack(pady=10)
    show_copy_btn()

def show_copy_btn():
    """
    Display the copy button after a password has been generated.
    """
    copyButton.grid(row=0, column=1, pady=10, padx=10)

def copy_to_clipboard():
    """
    Copy the generated password to the clipboard.
    """
    window.clipboard_clear()  
    window.clipboard_append(labelPassword["text"])  
    window.update()  

def frame_customization():
    """
    Toggle the visibility of the customization frame based on the checkbox state.
    """
    if var.get():
        frame.pack(pady=10)
    else:
        frame.pack_forget()
        reset_spinboxes()

def reset_spinboxes():
    """
    Reset all spinboxes to their default values.
    """
    specChars.delete(0, "end")
    specChars.insert(0, 0)
    
    digChars.delete(0, "end")
    digChars.insert(0, 0)
    
    upperChars.delete(0, "end")
    upperChars.insert(0, 0)
    
    lowerChars.delete(0, "end")
    lowerChars.insert(0, 0)
    
    passLngth.delete(0, "end")
    passLngth.insert(0, 8)

def restart():
    """
    Reset the application to its initial state.
    """
    frame.pack_forget()
    passwordFrame.pack_forget()
    var.set(0)
    reset_spinboxes()

# Main window setup
window = tk.Tk()
window.title("Password Generator")
window.geometry("1000x600") 
window.configure(bg="black")

# Background image setup
bgImage = tk.PhotoImage(file="picture.png")
canvasBg = tk.Canvas(window, width=1000, height=600)
canvasBg.place(x=0, y=0, relwidth=1, relheight=1)
canvasBg.create_image(0, 0, image=bgImage, anchor="nw")

# Title label
labelTitle = tk.Label(window, text="Professional Password Generator", bg="black", fg="white", font=("Agency FB", 35, "bold"))
labelTitle.pack(pady=(200, 40))

# Main frame for controls
mngFrame = tk.Frame(window, bg="black")
mngFrame.pack(pady=10)

# Restart button
icon = tk.PhotoImage(file="restart.png")
restartButton = tk.Button(mngFrame, image=icon, command=restart)
restartButton.grid(row=0, column=0, padx=10, pady=5)

# Frame for displaying generated password
passwordFrame = tk.Frame(window, bg="black")
passwordFrame.pack(pady=10)

# Copy button (initially hidden)
copyButton = tk.Button(passwordFrame, text="Copy", command=copy_to_clipboard, font=("Arial Nova Cond Light", 10))

# Label for displaying generated password
labelPassword = tk.Label(passwordFrame, bg="black", fg="white", font=("Arial Nova Cond Light", 16, "bold"))
labelPassword.grid(row=0, column=0, pady=10, padx=10)

# Generate password button
generateButton = tk.Button(mngFrame, text="Generate Password", command=generate_password, font=("Arial Nova Cond Light", 14))
generateButton.grid(row=0, column=1, pady=5)

# Password length control
lenLabel = tk.Label(mngFrame, text=" Length:", bg="black", fg="white", font=("Arial Nova Cond Light", 12))
lenLabel.grid(row=0, column=2, padx=10, pady=5)
passLngth = tk.Spinbox(mngFrame, from_=8, to=18, font=("Arial Nova Cond Light", 12), width=2)
passLngth.grid(row=0, column=3, padx=10, pady=5)

# Customization checkbox
var = tk.IntVar()
customization = tk.Checkbutton(mngFrame, text="Customization", bg="black", fg="white", variable=var, command=frame_customization)
customization.grid(row=0, column=4, padx=10, pady=5)

# Customization frame (initially hidden)
frame = tk.Frame(window, bg="black")

# Special characters control
lblSpcl = tk.Label(frame, text="Special Characters:", bg="black", fg="white", font=("Arial Nova Cond Light", 12, "bold"))
lblSpcl.grid(row=0, column=0, padx=20, pady=5)
specChars = tk.Spinbox(frame, from_=0, to=10, width=2)
specChars.grid(row=1, column=0, pady=5, padx=20)

# Digits control
lblDig = tk.Label(frame, text="Digits:", bg="black", fg="white", font=("Arial Nova Cond Light", 12, "bold"))
lblDig.grid(row=0, column=1, padx=20, pady=5)
digChars = tk.Spinbox(frame, from_=0, to=10, width=2)
digChars.grid(row=1, column=1, pady=5, padx=20)

# Uppercase letters control
lblupper = tk.Label(frame, text="Uppercase Letters:", bg="black", fg="white", font=("Arial Nova Cond Light", 12, "bold"))
lblupper.grid(row=0, column=2, padx=20, pady=5)
upperChars = tk.Spinbox(frame, from_=0, to=10, width=2)
upperChars.grid(row=1, column=2, pady=5, padx=20)

# Lowercase letters control
lblLower = tk.Label(frame, text="Lowercase Letters:", bg="black", fg="white", font=("Arial Nova Cond Light", 12, "bold"))
lblLower.grid(row=0, column=3, padx=20, pady=5)
lowerChars = tk.Spinbox(frame, from_=0, to=10, width=2)
lowerChars.grid(row=1, column=3, pady=5, padx=20)

# Start the main event loop
window.mainloop()
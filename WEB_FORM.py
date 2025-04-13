import tkinter as tk
from tkinter import messagebox

def submit_form():
    name = name_entry.get()
    age = age_entry.get()
    email = email_entry.get()
    gender = gender_var.get()
    country = country_var.get()
    
    if not name or not age or not email or not gender or country == "Select Country":
        messagebox.showerror("Error", "Please fill all the fields!")
    else:
        messagebox.showinfo("Form Submitted", f"Name: {name}\nAge: {age}\nEmail: {email}\nGender: {gender}\nCounty: {country}")


root=tk.Tk()
root.title("User Registration Form")
root.geometry("300x350")

tk.Label(root, text="Name:").pack()
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root, text="Age:").pack()
age_entry = tk.Entry(root)
age_entry.pack()

tk.Label(root, text="Email:").pack()
email_entry = tk.Entry(root)
email_entry.pack()

tk.Label(root, text="Gender:").pack()
gender_var = tk.StringVar()
tk.Radiobutton(root, text="Male", variable=gender_var, value="Male").pack()
tk.Radiobutton(root, text="Female", variable=gender_var, value="Female").pack()

tk.Label(root, text="Country:").pack()
country_var = tk.StringVar(value="Select Country")
country_menu = tk.OptionMenu(root, country_var, "USA", "UK", "Canada", "Australia", "Pakistan", "India")
country_menu.pack()

tk.Button(root, text="Submit", command=submit_form).pack(pady=10)

root.mainloop()


        
        
import tkinter as tk
from tkinter import messagebox

def check_Quiz():
    val1 = Q1.get()
    val2 = Q2.get()
    
    marks=0
    if val1 == "25-December-1876":
        marks += 5
    else:
        marks=0
        
    if val2 == "9-November-1877":
        marks+=5
         
    messagebox.showinfo("Quiz Submitted", f"Your marks: {marks}/10")
        
root=tk.Tk()
root.title("User Registration Form")
root.geometry("300x350")

tk.Label(root, text="QUIZ").pack()

tk.Label(root, text="Quaid-e-Azam was born on: ").pack()
Q1 = tk.StringVar()
tk.Radiobutton(root, text="20-October-1877", variable=Q1, value="20-October-1877").pack()
tk.Radiobutton(root, text="25-December-1876", variable=Q1, value="25-December-1876").pack()
tk.Radiobutton(root, text="6-June-1875", variable=Q1, value="6-June-1875").pack()
tk.Radiobutton(root, text="17-July-1875", variable=Q1, value="17-July-1875").pack()

tk.Label(root, text="Allama Iqbal was born on: ").pack()
Q2 = tk.StringVar()
tk.Radiobutton(root, text="17-May-1874", variable=Q2, value="17-May-1874").pack()
tk.Radiobutton(root, text="25-December-1876", variable=Q2, value="25-December-1876").pack()
tk.Radiobutton(root, text="9-November-1877", variable=Q2, value="9-November-1877").pack()
tk.Radiobutton(root, text="6-June-1875", variable=Q2, value="6-June-1875").pack()

tk.Button(root, text="Submit", command=check_Quiz).pack(pady=10)

root.mainloop()
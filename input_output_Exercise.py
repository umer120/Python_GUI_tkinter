from tkinter import simpledialog,messagebox

# 1st task
user_inp=simpledialog.askstring("Input","Enter Input:")
messagebox.showinfo("Output",user_inp)


# 2nd task
numbers = list(map(int, input("Enter numbers separated by space: ").split('+')))
print("List of numbers:",numbers)


# 3rd task
user_input = int(simpledialog.askstring("Input", "Input integer: "))

message=""
for num in range(11):
    message+=f"{user_input} x {num} = {user_input*num}\n"

messagebox.showinfo("Output",message)
    
    


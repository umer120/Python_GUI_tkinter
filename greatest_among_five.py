from tkinter import simpledialog,messagebox

numbers = list(map(int, simpledialog.askstring("Input", "Input integer: ").split()))
print("List of numbers:",numbers)

maximum=numbers[0]

for i in range(1,len(numbers)):
    if numbers[i]>maximum:
        maximum=numbers[i]
    
messagebox.showinfo("Output",maximum)
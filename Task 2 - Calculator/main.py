import tkinter as tk

def calculate():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    operation = operation_choice.get()

    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        result = num1 / num2
    else:
        result = "Invalid operation"

    label_result.config(text="Result: " + str(result))

root = tk.Tk()
root.title("Simple Calculator")

label_num1 = tk.Label(root, text="Number 1:")
label_num1.pack()

entry_num1 = tk.Entry(root)
entry_num1.pack()

label_num2 = tk.Label(root, text="Number 2:")
label_num2.pack()

entry_num2 = tk.Entry(root)
entry_num2.pack()

label_operation = tk.Label(root, text="Operation:")
label_operation.pack()

operation_choice = tk.StringVar(root)
operation_choice.set("+")

option_menu = tk.OptionMenu(root, operation_choice, "+", "-", "*", "/")
option_menu.pack()

button_calculate = tk.Button(root, text="Calculate", command=calculate)
button_calculate.pack()

label_result = tk.Label(root, text="Result:")
label_result.pack()

root.mainloop()

import tkinter as tk


# Create the global variables
result = 0

# Function to calculate the result
def calculate():
    global result
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    operation = operation_choice.get()

    # Check the operation
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

    # Update the result label
    label_result.config(text="Result: " + str(result))

# Function to continue the calculation
def continued():
    entry_num1.delete(0, tk.END)
    entry_num2.delete(0, tk.END)
    entry_num1.insert(0, result) # Insert the result into the first number
    label_result.config(text="Result: ")

# Function to clear the inputs
def clear():
    entry_num1.delete(0, tk.END)
    entry_num2.delete(0, tk.END)
    label_result.config(text="Result: ")

# Create the main window
root = tk.Tk() # Create the window
root.title("Simple Calculator") # Set the title
root.resizable(False, False) # Disable resizing

#Create the title
label_title = tk.Label(root, text="Simple Calculator", font=("Arial", 30))
label_title.grid(padx=10, pady=10, columnspan=2)

# Create the inputs
label_num1 = tk.Label(root, text="Number 1:", font=("Arial", 15))   # Create the label
label_num1.grid(row=1, column=0, padx=10, pady=10)

entry_num1 = tk.Entry(root, font=("Arial", 15))     # Create the entry
entry_num1.grid(row=1, column=1, padx=10, pady=10)

label_num2 = tk.Label(root, text="Number 2:", font=("Arial", 15))   # Create the label
label_num2.grid(row=2, column=0, padx=10, pady=10)

entry_num2 = tk.Entry(root, font=("Arial", 15))     # Create the entry
entry_num2.grid(row=2, column=1, padx=10, pady=10)

# Create the operation
label_operation = tk.Label(root, text="Operation:", font=("Arial", 15))     # Create the label
label_operation.grid(row=3, column=0, padx=10, pady=10)

operation_choice = tk.StringVar(root)    # Create the variable
operation_choice.set("+")    # Set the default value

option_menu = tk.OptionMenu(root, operation_choice, "+", "-", "*", "/")     # Create the option menu
option_menu.configure(font=("Arial", 15))
option_menu.grid(row=3, column=1, padx=10, pady=10)

# Create the buttons
button_calculate = tk.Button(root, text="Calculate", font=("Arial", 15), command=calculate)    # Create the button
button_calculate.grid(row=4, column=0, padx=10, pady=10, columnspan=2)

button_continue = tk.Button(root, text="Continue", command=continued)   # Create the button
button_continue.grid(row=5, padx=10, pady=10, columnspan=2)

button_clear = tk.Button(root, text="Clear", command=clear)     # Create the button
button_clear.grid(row=6, padx=10, pady=10, columnspan=2)

# Create the result label
label_result = tk.Label(root, text="Result:", font=("Arial", 18))   # Create the label
label_result.grid(row=7, padx=10, pady=10, columnspan=2)

# Create the footer
footer = tk.Label(root, text="Made by @jaguar000212\n♥️♥️♥️", anchor="center")   # Create the label
footer.configure(font=("Arial", 10, "bold",), fg="red", cursor="hand2", pady=10, padx=10)
footer.grid(columnspan=2, padx=100, pady=25)

# Run the main window loop
root.mainloop()
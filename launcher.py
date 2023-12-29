import tkinter as tk
import subprocess

class ToolTip:
    def __init__(self, widget, text):
        self.widget = widget
        self.text = text
        self.tooltip = None

    def show_tooltip(self):
        x, y, _, _ = self.widget.bbox("insert")
        x += self.widget.winfo_rootx() + 25
        y += self.widget.winfo_rooty() + 20
        self.tooltip = tk.Toplevel(self.widget)
        self.tooltip.wm_overrideredirect(True)
        self.tooltip.wm_geometry(f"+{x}+{y}")
        label = tk.Label(self.tooltip, text=self.text)
        label.pack()

    def hide_tooltip(self):
        if self.tooltip:
            self.tooltip.destroy()
            self.tooltip = None

root = tk.Tk()
root.title("Application Launcher")
root.resizable(False, False)
root.iconbitmap('icon.ico')  # Set window icon
root.configure(bg='lightblue')  # Set window background color

def run_app_by_number(event):
    app_number = int(event.char) - 1  # Subtract 1 because list indices start at 0
    if 0 <= app_number < len(app_directories):
        run_app(app_directories[app_number])

def run_app(app_directory):
    status.set(f"Running {app_directory}...")
    subprocess.call(["python", "main.py"], cwd=app_directory)
    status.set(f"Succesfully ran {app_directory}, now Ready")

status = tk.StringVar(value="Ready")

head = tk.Label(root, text = "CodSoft Internship", font = ("Ariel", 30), bg='lightblue')
head.grid(columnspan=2, padx = 50)

program = tk.Label(root, text = "Python Programming", font = ("Ariel", 18), bg='lightblue')
program.grid(columnspan=2)

byline = tk.Label(root, text = "By Shryansh Parashar, aka Jaguar000212", font = ("Ariel", 8), bg='lightblue')
byline.grid(columnspan=2)

app_directories = ["Task 1 - ToDo List", "Task 2 - Calculator", "Task 3 - Password Generator", "Task 4 - RPS Game", "Task 5 - Address Book"]

for index, app_directory in enumerate(app_directories):
    label = tk.Label(root, text=f"Run {app_directory}", font = ("Ariel", 15), anchor="w", bg='lightblue')
    label.grid(row=index+3, column=0, padx=10, pady=10, sticky="w")
    button = tk.Button(root, text="Launch", command=lambda app_directory=app_directory: run_app(app_directory), font = ("Ariel", 15))
    button.grid(row=index+3, column=1, padx=10, pady=10)
    tooltip = ToolTip(button, f"Press {index+1} or click to launch")
    button.bind("<Enter>", lambda e, tooltip=tooltip: tooltip.show_tooltip())
    button.bind("<Leave>", lambda e, tooltip=tooltip: tooltip.hide_tooltip())

status_bar = tk.Label(root, relief=tk.SUNKEN, anchor=tk.W, textvariable=status, bg='lightblue')
status_bar.grid(sticky='ew', padx=5, pady=5)

root.bind('<Key>', run_app_by_number)  # Bind the run_app_by_number function to key press events

root.mainloop()
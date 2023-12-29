import tkinter as tk
import subprocess

# Tooltip class
class ToolTip:
    def __init__(self, widget, text):
        self.widget = widget
        self.text = text
        self.tooltip = None

    def show_tooltip(self):
        x, y, _, _ = self.widget.bbox("insert") # Get the position of the cursor
        x += self.widget.winfo_rootx() + 25 # Offset the position of the tooltip
        y += self.widget.winfo_rooty() + 20 # Offset the position of the tooltip
        self.tooltip = tk.Toplevel(self.widget) # Create a new window for the tooltip
        self.tooltip.wm_overrideredirect(True) # Remove the window border
        self.tooltip.wm_geometry(f"+{x}+{y}") # Set the position of the tooltip
        label = tk.Label(self.tooltip, text=self.text) # Create a label for the tooltip
        label.pack() 

    def hide_tooltip(self):
        if self.tooltip:
            self.tooltip.destroy() # Destroy the tooltip window
            self.tooltip = None
            
# Main window
root = tk.Tk() 
root.title("Application Launcher") # Set window title
root.resizable(False, False) # Disable resizing of window
root.iconbitmap('icon.ico')  # Set window icon
root.configure(bg='lightblue')  # Set window background color

# Functions
def run_app_by_number(event):  # Function to run an app based on the number pressed
    app_number = int(event.char) - 1  # Subtract 1 because list indices start at 0
    if 0 <= app_number < len(app_directories):
        run_app(app_directories[app_number]) # Run the app if the number is valid

def run_app(app_directory): # Function to run an app
    status.set(f"Running {app_directory}...")
    subprocess.call(["python", "main.py"], cwd=app_directory)
    status.set(f"Succesfully ran {app_directory}, now Ready")

status = tk.StringVar(value="Ready") # Set initial status bar text

head = tk.Label(root, text = "CodSoft Internship", font = ("Ariel", 30), bg='lightblue') # Set heading
head.grid(columnspan=2, padx = 50)

program = tk.Label(root, text = "Python Programming", font = ("Ariel", 18), bg='lightblue') # Set subheading
program.grid(columnspan=2)

byline = tk.Label(root, text = "By Shryansh Parashar, aka Jaguar000212", font = ("Ariel", 8), bg='lightblue') # Set byline
byline.grid(columnspan=2)

# Create a label and button for each app
app_directories = ["Task 1 - ToDo List", "Task 2 - Calculator", "Task 3 - Password Generator", "Task 4 - RPS Game", "Task 5 - Address Book"]

for index, app_directory in enumerate(app_directories):
    label = tk.Label(root, text=f"Run {app_directory}", font = ("Ariel", 15), anchor="w", bg='lightblue') # Create a label for the app
    label.grid(row=index+3, column=0, padx=10, pady=10, sticky="w") 
    button = tk.Button(root, text="Launch", command=lambda app_directory=app_directory: run_app(app_directory), font = ("Ariel", 15)) # Create a button to launch the app
    button.grid(row=index+3, column=1, padx=10, pady=10)
    tooltip = ToolTip(button, f"Press {index+1} or click to launch") # Create a tooltip for the button
    button.bind("<Enter>", lambda e, tooltip=tooltip: tooltip.show_tooltip()) # Bind the show_tooltip function to mouse enter events
    button.bind("<Leave>", lambda e, tooltip=tooltip: tooltip.hide_tooltip()) # Bind the hide_tooltip function to mouse leave events

status_bar = tk.Label(root, relief=tk.SUNKEN, anchor=tk.W, textvariable=status, bg='lightblue') # Create a status bar
status_bar.grid(sticky='ew', padx=5, pady=5) 

root.bind('<Key>', run_app_by_number)  # Bind the run_app_by_number function to key press events

root.mainloop() # Run the main window

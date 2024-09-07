import os
import tkinter as tk
from tkinter import filedialog, messagebox, ttk

# Create the main window
root = tk.Tk()
root.title("Windows Update Integrator")
root.geometry("500x300")  # Initial window size

# Make the window resizable
root.grid_columnconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)

# Variables to hold file paths and status
iso_path = tk.StringVar()
updates_path = tk.StringVar()
status_message = tk.StringVar(value="Ready")

# Function to browse for ISO file
def browse_iso():
    iso = filedialog.askopenfilename(filetypes=[("ISO files", "*.iso")])
    if iso:
        iso_path.set(iso)
        iso_entry.update()
        update_status("ISO file selected.")

# Function to browse for updates folder
def browse_updates():
    updates = filedialog.askdirectory()
    if updates:
        updates_path.set(updates)
        updates_entry.update()
        update_status("Updates folder selected.")

# Function to update status message
def update_status(message):
    status_message.set(message)

# Function to validate inputs
def validate_inputs():
    if not iso_path.get():
        messagebox.showerror("Error", "Please select a Windows ISO file.")
        return False
    if not updates_path.get():
        messagebox.showerror("Error", "Please select a folder with updates.")
        return False
    return True

# Function to simulate integration process
def integrate_updates():
    if not validate_inputs():
        return
    
    update_status("Starting integration...")
    
    # Reset progress bar
    progress_bar['value'] = 0
    root.update_idletasks()
    
    # Simulate progress for each step (replace with actual logic)
    steps = 5
    for step in range(steps):
        progress_bar['value'] += 100 / steps  # Update the progress bar
        update_status(f"Step {step + 1}/{steps} in progress...")
        root.update_idletasks()
        root.after(500)  # Simulate processing delay

    update_status("Integration complete!")
    messagebox.showinfo("Success", "Windows updates have been integrated successfully.")

# Labels, Entry fields, and Browse buttons for ISO and Updates folder
tk.Label(root, text="Select Windows ISO:").grid(row=0, column=0, padx=10, pady=10, sticky="e")
iso_entry = tk.Entry(root, textvariable=iso_path, width=40)
iso_entry.grid(row=0, column=1, padx=10, pady=10, sticky="we")
tk.Button(root, text="Browse", command=browse_iso).grid(row=0, column=2, padx=10, pady=10)

tk.Label(root, text="Select Updates Folder:").grid(row=1, column=0, padx=10, pady=10, sticky="e")
updates_entry = tk.Entry(root, textvariable=updates_path, width=40)
updates_entry.grid(row=1, column=1, padx=10, pady=10, sticky="we")
tk.Button(root, text="Browse", command=browse_updates).grid(row=1, column=2, padx=10, pady=10)

# Progress bar for showing progress during the integration process
progress_bar = ttk.Progressbar(root, orient="horizontal", length=400, mode="determinate")
progress_bar.grid(row=2, column=0, columnspan=3, padx=10, pady=20, sticky="we")

# Integrate Updates button
integrate_button = tk.Button(root, text="Integrate Updates", command=integrate_updates)
integrate_button.grid(row=3, column=1, pady=10)

# Status label to show current status
status_label = tk.Label(root, textvariable=status_message, relief="sunken", anchor="w")
status_label.grid(row=4, column=0, columnspan=3, padx=10, pady=10, sticky="we")

# Run the Tkinter event loop
root.mainloop()

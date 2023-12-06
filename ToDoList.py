import tkinter as tk

# Function to handle adding tasks to the to-do list
def add_task():
    task = task_entry.get()
    if task:
        listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)

# Function to handle removing selected task from the to-do list
def remove_task():
    selected_task_index = listbox.curselection()
    if selected_task_index:
        listbox.delete(selected_task_index)

# Create the main Tkinter window
root = tk.Tk()
root.title("To-Do List App")

# Entry widget to add tasks
task_entry = tk.Entry(root, width=30)
task_entry.pack(pady=10)

# Button to add tasks
add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack(pady=5)

# Listbox to display tasks
listbox = tk.Listbox(root, selectmode=tk.SINGLE, height=10, width=40)
listbox.pack(pady=10)

# Button to remove selected task
remove_button = tk.Button(root, text="Remove Task", command=remove_task)
remove_button.pack(pady=5)

# Start the Tkinter event loop
root.mainloop()

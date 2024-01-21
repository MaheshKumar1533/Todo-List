import tkinter as tk

def addtask():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)

def removetask():
    selected_task_index = listbox.curselection()
    if selected_task_index:
        listbox.delete(selected_task_index)

root = tk.Tk()
root.title("To-Do List")

listbox = tk.Listbox(root, selectmode=tk.SINGLE)
listbox.pack(pady=10)

entry = tk.Entry(root, width=40)
entry.pack(pady=10)

addbutton = tk.Button(root, text="Add Task", command=addtask)
addbutton.pack(pady=5)

removebutton = tk.Button(root, text="Remove Task", command=removetask)
removebutton.pack(pady=5)
root.mainloop()
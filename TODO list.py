import tkinter
import tkinter.messagebox

root = tkinter.Tk()
root.title("To-Do List")
root.config(bg="light blue")

def add_task():
    task = entry_task.get()                                  #entry box(typing)
    if task != "":                                           #add to the list box
        listbox_tasks.insert(tkinter.END, task)
        entry_task.delete(0, tkinter.END)
    else:                                                    #no text is entered ,it shows warning
        tkinter.messagebox.showwarning(title="Warning!", message="You must enter a task.")

def delete_task():
    try:   #avoiding errors
        task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(task_index)
    except:   #clearing the errors - shows warning
        tkinter.messagebox.showwarning(title="Warning!", message="You must select a task.")


def modify_task():
    try:
        task_index = listbox_tasks.curselection()[0]
        new_task = entry_task.get()                         #gets the new task from the user in the entry field
        listbox_tasks.delete(task_index)                    #delete the particular task
        listbox_tasks.insert(task_index, new_task)  #insert the new task
        entry_task.delete(0, tkinter.END)
    except:
        tkinter.messagebox.showwarning(title="Warning!", message="You must select a task.")


def delete_all_tasks():
    listbox_tasks.delete(0, tkinter.END)



frame_tasks = tkinter.Frame(root)                               #for task list & scrollbar
frame_tasks.grid(row=0, column=0, padx=15, pady=15,)

listbox_tasks = tkinter.Listbox(frame_tasks, height=12, width=75,)    #for display the task list
listbox_tasks.grid(row=0, column=0, sticky=tkinter.W)

scrollbar_tasks = tkinter.Scrollbar(frame_tasks)                      #to stick the scrollbar in the edge
scrollbar_tasks.grid(row=0, column=1, sticky=tkinter.N+tkinter.S)     #to scroll the bar frm top-bottom

listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)             #to set the scrollbar
scrollbar_tasks.config(command=listbox_tasks.yview)

entry_task = tkinter.Entry(root, width=50, )                        #for enterinig the new task
entry_task.grid(row=1, column=0, padx=15, pady=15)

button_add_task = tkinter.Button(root, text="Add task", bg="light yellow",  width=48, command=add_task)
button_add_task.grid(row=2, column=0, padx=15, pady=10)

button_delete_task = tkinter.Button(root, text="Delete task", bg="red",  width=48, command=delete_task)
button_delete_task.grid(row=3, column=0, padx=15, pady=10)

button_delete_all = tkinter.Button(root, text="Delete All Tasks", bg="red", width=48, command=delete_all_tasks)
button_delete_all.grid(row=5, column=0, padx=15, pady=10)

button_modify_task = tkinter.Button(root, text="Modify task", bg="light yellow", width=48, command=modify_task)
button_modify_task.grid(row=4, column=0, padx=15, pady=10)

root.mainloop()
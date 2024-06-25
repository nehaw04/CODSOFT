from tkinter import *
from tkinter import messagebox
import pickle

root=Tk()
root.title("TO-DO LIST")
root.geometry("500x350")
root.configure(background="black")
root.grid_rowconfigure(0,minsize=40)
root.grid_columnconfigure(0,weight=1)

lbl=Label(root,text="",bg="black")
lbl.grid(column=0, row=0, sticky="w")

list_frame=Frame(root, bg="black")
list_frame.grid(column=0,row=11,columnspan=4,sticky="nsew")
list_frame.grid_columnconfigure(0,weight=1)

scroller=Scrollbar(list_frame)
scroller.grid(column=1,row=0,sticky="ns")


task_num=1
tasks=[]

def add_task():
    todo=task_add_entry.get()
    global task_num
    if todo!="":
        listbox.insert(END, f"{len(tasks) + 1}. {todo}")
        tasks.append(todo)
        task_entry.delete(0, END)
    else:
        messagebox.showinfo(title="ATTENTION !!",message="task should  not be blank")

def remove_task():
    try:
        index_of_task=listbox.curselection()
        listbox.delete(index_of_task)
        tasks.pop(index_of_task)  

        for i in range(index_of_task, listbox.size()):
            task = listbox.get(i)
            task_number, task_text = task.split('. ', 1)
            new_task_number = int(task_number) - 1
            new_task = f"{new_task_number}. {task_text}"
            listbox.delete(i)
            listbox.insert(i, new_task)
    except:
        messagebox.showwarning("ATTENTION","To delete a task,you must select a task")

def update_task():
    try:
        index_of_task=listbox.curselection()[0]
        select_task=listbox.get(index_of_task)

        update_window=Toplevel(root)
        update_window.title("Update task")

        update_label=Label(update_window,text="Enter new task:")
        update_label.grid()
   
        update_entry=Entry(update_window,width=40)
        update_entry.grid()
        update_entry.insert(0,select_task)

        def save_update(event=None):
            new_task=update_entry.get()
            if new_task:
                listbox.delete(index_of_task)
                listbox.insert(index_of_task, f"{index_of_task }. {new_task}")
                tasks[index_of_task] = new_task  # Update the tasks list
                update_window.destroy()

        update_button=Button(update_window,text="Update",command=save_update)
        update_button.grid()
    except:
        messagebox.showwarning("ATTENTION","To Update a task,you must select a task")

def tick_task():
    
    try:
        indx_of_task=listbox.curselection()[0]
        task_text=listbox.get(indx_of_task)
        listbox.delete(indx_of_task)
        listbox.insert(indx_of_task, f"{task_text} (Done)")
    except:
        messagebox.showwarning("ATENTION", "To tick a task, you must select a task")

    
def show_number():
    messagebox.showinfo("number of tasks",f"You have {len(listbox.get(0,END))}tasks")

    
task_add_entry=Entry(root,width=40)
task_add_entry.insert(0, "Enter a task name here")  
task_add_entry.grid(column=0,row=4,sticky="nsew",pady=(0,10))

add_task_button=Button(root,text="Add",font=("arial",15,"bold"),background="cyan",width=20,command=add_task)
add_task_button.grid(column=0,row=8,sticky="w")

remove_task_button=Button(root,text="Remove",font=("arial",15,"bold"),background="cyan",width=20,command=remove_task)
remove_task_button.grid(column=1,row=8,sticky="w")

update_task_button=Button(root,text="Update Task",font=("arial",15,"bold"),background="cyan",width=20,command=update_task)
update_task_button.grid(column=0,row=9,sticky="w")

tick_task_button=Button(root,text="Mark as Done",font=("arial",15,"bold"),background="cyan",width=20,command=tick_task)
tick_task_button.grid(column=1,row=9,sticky="w")


listbox=Listbox(list_frame,height=10,width=30,yscrollcommand=scroller.set,borderwidth=1,relief="solid")
listbox.insert(0,"Task Box")
listbox.grid(column=0,row=0,sticky="nsew",pady=(0,20))
scroller.configure(command=listbox.yview)



root.mainloop()
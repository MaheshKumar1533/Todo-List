import os.path
import pickle

def create_file():
    file_pointer = open("data.bin", 'wb')
    pickle.dump([], file_pointer)
    pickle.dump([], file_pointer)
    file_pointer.close()

def gettasks():
    f = open("data.bin", 'rb')
    tasks = pickle.load(f)
    completed = pickle.load(f)
    f.close()
    return tasks, completed

def puttasks(tasks, completed):
    f = open("data.bin", 'wb')
    pickle.dump(tasks, f)
    pickle.dump(completed, f)
    f.close()

def printtasks():
    tasks, completed = gettasks()
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")

def addtask():
    tasks, completed = gettasks()
    task = input("Enter the task : ")
    tasks.append(task)
    puttasks(tasks, completed)

def completetask():
    tasks, completed = gettasks()
    printtasks()
    choice = int(input("Enter the task number : "))
    if 0<=choice-1<len(tasks):
        task = tasks.pop(choice-1)
        completed.append(task)
        puttasks(tasks, completed)
    else:
        print("Invalid Choice")

def deletetask():
    printtasks()
    tasks, completed = gettasks()
    choice = int(input("Enter the task number : "))
    if 0<=choice-1<len(tasks):
        tasks.pop(choice-1)
        puttasks(tasks, completed)
    else:
        print("Invalid Choice")

def showcompletedtasks():
    tasks, completed = gettasks()
    for i, task in enumerate(completed, start=1):
        print(f"{i}.\t{task}")

if __name__ == "__main__":
    if not os.path.isfile("data.bin"):
        create_file()
    while True:
        try:
            print("1. Show Tasks")
            print("2. Add Task")
            print("3. Complete Task")
            print("4. Delete Task")
            print("5. Show completed tasks")
            print("6. Exit")
            choice = int(input("Enter your choice : "))
            if choice==1:
                printtasks()
            elif choice==2:
                addtask()
            elif choice==3:
                completetask()
            elif choice==4:
                deletetask()
            elif choice==5:
                showcompletedtasks()
            elif choice==6:
                break
            else:
                print("Invalid chioce")
        except Exception as e:
            print(f"Error Occured : {e}")
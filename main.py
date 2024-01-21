import os.path
import pickle

def create_file():
    file_pointer = open("data.bin", 'wb')
    pickle.dump([], file_pointer)
    file_pointer.close()

def gettasks():
    f = open("data.bin", 'rb')
    tasks = pickle.load(f)
    f.close()
    return tasks

def puttasks(tasks):
    f = open("data.bin", 'wb')
    pickle.dump(tasks, f)
    f.close()

def printtasks():
    tasks = gettasks()
    for i, task in enumerate(tasks, start=1):
        print(f"{i}.\t{task}")

def addtask():
    tasks = gettasks()
    task = input("Enter the task : ")
    tasks.append(task)
    puttasks(tasks)

def deletetask():
    printtasks()
    tasks = gettasks()
    choice = int(input("Enter the task number : "))
    if 0<=choice-1<len(tasks):
        tasks.pop(choice-1)
        puttasks(tasks)
    else:
        print("Invalid Choice")

if __name__ == "__main__":
    if not os.path.isfile("data.bin"):
        create_file()
    while True:
        print("1. Show Tasks")
        print("2. Add Task")
        print("3. Delete Task")
        print("4. Exit")
        try:
            choice = int(input("Enter your choice : "))
            if choice==1:
                printtasks()
            elif choice==2:
                addtask()
            elif choice==3:
                deletetask()
            elif choice==4:
                break
            else:
                print("Invalid chioce")
        except:
            print("Error occured please try again")

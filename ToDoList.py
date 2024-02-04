taskList=dict()
while True:
    print("---------------------------------")
    print("-----------TO DO LIST-----------")
    print("1.Add New Task")
    print("2.View All Task")
    print("3.Mark a Task as Done")
    print("4.Exit")
    ch=int(input("Enter your choice:"))
    if ch==1:
        task=input().strip()
        taskList[task]="Not Done"
        print("Task Added successfully")

    elif ch==2:
        print("Displaying task.............")
        num=1
        for i in taskList:
            print(f"{num}.{i}-{taskList[i]}")
            num+=1
    elif ch==3:
        taskNum=int(input("Enter the Task number:"))
        if taskNum>len(taskList):
            print("Invalid Task Number")
        else:
            for i,task in enumerate(taskList):
                if i+1==taskNum:
                    taskList[task]="Done"
                    print("Task Marked as done.......")
    else:
        print("Exiting.............")
        break


    
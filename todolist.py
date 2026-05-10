
def add(tasks):
    
    addition=input("what do you want to add?\n")
    tasks.append(addition)
    print("\ntask added successfully!\n")
    print(f'===To Do List===\n',tasks)
    print('\n')


def remove(tasks):
    rem=int(input("which task do you want to remove? give index number\n"))
    if rem <= len(tasks):
            
        tasks.remove(tasks[rem])
        print("\ntask removed successfully!\n")
        print(f'===To Do List===\n ',tasks)
        print('\n')
    else:
        print("idex out of range!")
        remove(tasks)

tasks=[]



choice=-1
while (choice!=0):
    print('press 0 to exit')
    print("press 1 to add")
    
    choice=int(input('press 2 to remove\n'))

    if choice==1:
        add(tasks)


    elif choice==2:
        remove(tasks)

    elif choice==0:
        print("good bye!")

    else:
        print("invalid entry!")


total=0
while True:  
    a = input("Enter the amount or type 'exit' to finish: ")
    if a=="exit":
        print("The total is: ", total)
        print("goodbye!")

        break
    
    
    a=int(a)
    total=total + a
    print("The total is: ", total)





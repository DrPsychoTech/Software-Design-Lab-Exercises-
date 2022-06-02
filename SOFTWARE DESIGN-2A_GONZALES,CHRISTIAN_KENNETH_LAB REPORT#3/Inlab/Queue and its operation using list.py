# implementing Queue using List :
q=[]
q.append(10)
q.append(100)
q.append(1000)
q.append(10000)
print("Initial Queue is:",q)
print(q.pop(0))
print(q.pop(0))
print(q.pop(0))
print("After Removing elements:",q)


q=[]
def Enqueue():
    if len(q)==size: # check wether the stack is full or not
        print("Queue is Full!!!!")
    else:
        element=input("Enter the element:")
        q.append(element)
        print(element,"is added to the Queue!")
def dequeue():
    if not q:# or if len(stack)==0
        print("Queue is Empty!!!")
    else:
        e=q.pop(0)
        print("element removed!!:",e)
def display():
    print(q)
    size=int(input("Enter the size of Queue:"))
    while True:
        print("Select the Operation:1.Add 2.Delete 3. Display 4. Quit")
        choice=int(input())
        if choice==1:
            Enqueue()
        elif choice==2:
            dequeue()
        elif choice==3:
            display()
        elif choice==4:
            break
        else:
            print("Invalid Option!!!")




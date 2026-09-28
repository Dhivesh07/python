queue=[]
MAX=5
def enqueue():
    if len(queue)==MAX:
        print("Parking is full")
    else:
        car= input("Enter car number:")
        queue.append(car)
        print(car,"has entered the parking")
def dequeue():
    if len(queue)==0:
        print("parking is empty!")
    else:
        car=queue.pop(0)
        print(car,"has exited the parking")
def display():
    if len(queue)==0:
        print("No cars is the parking")
    else:
        print("cars in parking")
        for car in queue:
            print(car)
while True:
    print("/n----- cars parking system-----")
    print("1. park car(enqueue)")
    print("2.remove car(dequeue)")
    print("3.display car")
    print("4.exit")
    ch=int(input("Enter your choice:"))
    if ch==1:
        enqueue()
    elif ch==2:
        dequeue()
    elif ch==3:
        display()
    elif ch==4:
        print("Exiting the program")
        break
    else:
        print("Invalid choice")

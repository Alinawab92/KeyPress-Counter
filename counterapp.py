import time
import keyboard

def myapp(counter):
    for i in range(counter + 1): 
        if keyboard.is_pressed('space'):
            print("\nCounter Suspended!")  
            break
        print(f"\rCounter: {i}", end="")
        time.sleep(1)
    else:
        print(f"\nCounter reached target: {counter}") 

if __name__ == "_main_":
    target = int(input("Enter the target number: "))
    myapp(target)
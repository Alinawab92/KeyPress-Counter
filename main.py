import time
import keyboard
import argparse

def myapp(counter):
    for i in range(counter + 1): 
        if keyboard.is_pressed('space'):
            print("\nCounter Suspended!")  
            break

        print(f"\rCounter: {i}", end="")
        time.sleep(1)

    else:
        print(f"\nCounter reached target: {counter}") 

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("target", type=int)
    target = parser.parse_args().target

    myapp(target)


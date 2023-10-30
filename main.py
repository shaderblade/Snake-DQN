import os
import sys
from agent import train
from test_agent import test

def main():
    print("\nWelcome to Snake Game!")
    while True:
        print("\nMenu:")
        print("1. Train Snake AI")
        print("2. Test Snake AI")
        print("3. Quit")

        choice = input("\nEnter your choice (1/2/3): ")

        if choice == '1':
            train()
        elif choice == '2':
            test()
        elif choice == '3':
            print("\nGoodbye!")
            sys.exit()
        else:
            print("\nInvalid choice. Please enter 1, 2, or 3.")

if __name__ == '__main__':
    main()
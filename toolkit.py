 
# Personal Mini-Toolkit
# A menu-driven program with three useful tools.

import random

print("Welcome to your Personal Mini-Toolkit!")

running = True
tasks = []

while running:
    print()
    print("=== Personal Mini-Toolkit ===")
    print("1. Number Guessing Game")
    print("2. To-Do List")
    print("3. Name Formatter")
    print("4. Quit")

    choice = input("Choose an option (1-4): ")

    # Tool 1: Number Guessing Game
    # The computer picks a number from 1 to 10.
    # The user keeps guessing until the answer is correct.

    if choice == "1":
        secret = random.randint(1, 10)
        guesses = 0

        print("I am thinking of a number from 1 to 10.")

        while True:
            guess = input("Your guess: ")

            if not guess.isdigit():
                print("Please type a whole number.")
                continue

            guess = int(guess)

            if guess < 1 or guess > 10:
                print("Please choose a number between 1 and 10.")
                continue

            guesses += 1

            if guess < secret:
                print("Too low! Try again.")
            elif guess > secret:
                print("Too high! Try again.")
            else:
                print(f"Correct! You got it in {guesses} guesses.")
                break

    # Tool 2: To-Do List
    # Allows the user to add, view and remove tasks.
    # A list stores tasks while the program is running.

    elif choice == "2":

        while True:
            print("\n=== To-Do List ===")
            print("1. Add a task")
            print("2. View tasks")
            print("3. Remove a task")
            print("4. Back to main menu")

            todo_choice = input("Choose an option (1-4): ")

            if todo_choice == "1":
                task = input("Enter your task: ").strip()

                if task:
                    tasks.append(task)
                    print(f"Task '{task}' added successfully!")
                else:
                    print("Task cannot be empty.")

            elif todo_choice == "2":
                if len(tasks) == 0:
                    print("Your to-do list is empty.")
                else:
                    print("\nYour tasks:")
                    for number, task in enumerate(tasks, start=1):
                        print(f"{number}. {task}")

            elif todo_choice == "3":
                if len(tasks) == 0:
                    print("There are no tasks to remove.")
                else:
                    for number, task in enumerate(tasks, start=1):
                        print(f"{number}. {task}")

                    remove_task = input("Enter task number to remove: ")

                    if remove_task.isdigit():
                        task_number = int(remove_task)

                        if 1 <= task_number <= len(tasks):
                            removed = tasks.pop(task_number - 1)
                            print(f"Task '{removed}' removed successfully!")
                        else:
                            print("Invalid task number.")
                    else:
                        print("Please enter a valid number.")

            elif todo_choice == "4":
                print("Returning to the main menu.")
                break

            else:
                print("Invalid choice. Please select 1, 2, 3 or 4.")

    # Tool 3: Name Formatter
    # Takes a name and formats it with proper capitalization.

    elif choice == "3":
        name = input("Enter your full name: ").strip()

        if name:
            formatted_name = name.title()
            print(f"Your formatted name is: {formatted_name}")
        else:
            print("Please enter a valid name.")

    # Quit the program

    elif choice == "4":
        print("Goodbye! Thanks for using the toolkit.")
        running = False

    # Handle invalid main menu choices

    else:
        print(f"Sorry, '{choice}' is not on the menu. Please type 1, 2, 3 or 4.")

import json
import os

# Using a custom filename for data persistence
DATA_FILE = "task_data.json"

def load_data():
    """Fetches existing tasks from the JSON file on startup"""
    if not os.path.exists(DATA_FILE):
        return [] # Return empty list if file doesn't exist yet
    
    with open(DATA_FILE, "r") as f:
        # Converting JSON back to a Python list
        return json.load(f)

def save_data(tasks):
    """Saves the current state of the list to the file"""
    with open(DATA_FILE, "w") as f:
        # Added indentation to make the file human-readable
        json.dump(tasks, f, indent=4)

def main():
    # Load all saved tasks at the beginning
    all_tasks = load_data()

    while True:
        print("\n--- TO-DO APP MENU ---")
        print("1. Add New Task")
        print("2. View All Tasks")
        print("3. Mark as Completed")
        print("4. Remove a Task")
        print("5. Save and Exit")
        
        choice = input("\nWhat would you like to do? ")

        if choice == "1":
            # Logic for adding a new task entry
            t_name = input("Enter task name: ")
            if t_name.strip(): # Validating that input isn't just whitespace
                all_tasks.append({"task": t_name, "done": False})
                print("Task added successfully!")
            else:
                print("Error: Task name cannot be empty.")

        elif choice == "2":
            # Displaying the current list with status icons
            if not all_tasks:
                print("Your list is currently empty.")
            else:
                print("\n--- YOUR CURRENT TASKS ---")
                for i, t in enumerate(all_tasks, 1):
                    # Using icons to make the status clear at a glance
                    status = "✅" if t["done"] else "❌"
                    print(f"{i}. {t['task']} [{status}]")

        elif choice == "3":
            # Updating the 'done' status based on user index
            try:
                num = int(input("Enter task number to mark done: ")) - 1
                all_tasks[num]["done"] = True
                print("Great! Task marked as complete.")
            except (ValueError, IndexError):
                print("Invalid number. Please check the list and try again.")

        elif choice == "4":
            # Logic for deleting a specific task
            try:
                num = int(input("Enter task number to delete: ")) - 1
                deleted = all_tasks.pop(num)
                print(f"Removed: {deleted['task']}")
            except:
                print("Oops! Could not delete. Please provide a valid index.")

        elif choice == "5":
            # Final save before closing the program
            save_data(all_tasks)
            print("Progress saved. Goodbye!")
            break
        
        else:
            print("Please select a valid option (1-5).")

if __name__ == "__main__":
    # The entry point of the script
    main()

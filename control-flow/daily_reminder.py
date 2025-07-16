task = input("Enter your task:")

priority = input("Priority (high/medium/low):").lower()

time_bound = input("Is it time-bound? (yes/no):").lower()

match priority:
    case "high":
        print(f"Reminder: The task '{task}' is a high priority task.", end="")
    case "medium":
        print(f"Reminder: The task '{task}' is a medium priority task.", end="")
    case "low":
        print(f"Reminder: The task '{task}' is a low priority task.", end="")
    case _:
        print(f"Reminder: The task '{task}' has an unknown priority level.", end="")

if time_bound == "yes":
    print(" This task requires immediate attention today!")
else:
    print()

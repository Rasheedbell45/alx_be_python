task = input("Enter your task:")

priority = input("Priority (high/medium/low):").lower()

time_bound = input("Is it time-bound? (yes/no):").lower()

match priority:
    case "high":
        reminder = f"The task '{task}' is a high priority task."
    case "medium":
        reminder = f"The task '{task}' is a medium priority task."
    case "low":
        reminder = f"The task '{task}' is a low priority task."
    case _:
        reminder = f"The task '{task}' has an unknown priority level."

if time_bound == "yes":
    reminder += " This task requires immediate attention today!"

print(reminder)

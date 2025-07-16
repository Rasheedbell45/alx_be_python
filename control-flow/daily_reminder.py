task = input("Enter your task:")

priority = input("Priority (high/medium/low):").lower()

time_bound = input("Is it time-bound? (yes/no):").lower()

match priority:
    case "high":
        message = f"Reminder: The task '{task}' is a high priority task."
    case "medium":
        message = f"Reminder: The task '{task}' is a medium priority task."
    case "low":
        message = f"Reminder: The task '{task}' is a low priority task."
    case _:
        message = f"Reminder: The task '{task}' has an unknown priority level."

if time_bound == "yes":
    message += " This task requires immediate attention today!"

print(message)

# daily_reminder.py

# Prompt for a single task
task = input("Enter your task for today: ")

# Prompt for the task’s priority
priority = input("Enter the task’s priority (high, medium, low): ").lower()

# Ask if the task is time-bound
time_bound = input("Is the task time-bound? (yes or no): ").lower()

# Match Case to handle task priority
match priority:
    case "high":
        reminder = f"The task '{task}' is a high priority task."
    case "medium":
        reminder = f"The task '{task}' is a medium priority task."
    case "low":
        reminder = f"The task '{task}' is a low priority task."
    case _:
        reminder = f"The task '{task}' has an unknown priority level."

# If the task is time-bound, add urgency
if time_bound == "yes":
    reminder += " This task requires immediate attention today!"

# Print final reminder
print(reminder)

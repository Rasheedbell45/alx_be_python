# daily_reminder.py

# Prompt for a single task
task = input("Enter a task: ")

# Prompt for the task’s priority
priority = input("Enter the task’s priority (high, medium, low): ").lower()

# Ask if the task is time-bound
time_bound = input("Is the task time-bound? (yes or no): ").lower()

# Match Case statement based on priority
match priority:
    case "high":
        reminder = f"Reminder: The task '{task}' is a high priority task."
    case "medium":
        reminder = f"Reminder: The task '{task}' is a medium priority task."
    case "low":
        reminder = f"Reminder: The task '{task}' is a low priority task."
    case _:
        reminder = f"Reminder: The task '{task}' has an unrecognized priority."

# Use if statement to check if time-sensitive
if time_bound == "yes":
    reminder += " This task requires immediate attention today!"

# Print the customized reminder
print(reminder)

task = input("Enter your task for today: ")
priority = input("Enter the priority level (high, medium, low): ").lower()
time_bound = input("Is this task time-bound? (yes or no): ").lower()

while priority not in ("high", "medium", "low"):
    print("Please enter a valid priority: high, medium, or low.")
    priority = input("Enter the priority level (high, medium, low): ").lower()

match priority:
    case "high":
        message = f"REMINDER: '{task}' is a HIGH priority task."
    case "medium":
        message = f"REMINDER: '{task}' is a MEDIUM priority task."
    case "low":
        message = f"REMINDER: '{task}' is a LOW priority task."
    case _:
        message = f"REMINDER: '{task}' has an unknown priority."

if time_bound == "yes":
    message += " It requires immediate attention today!"

print("\n" + message)

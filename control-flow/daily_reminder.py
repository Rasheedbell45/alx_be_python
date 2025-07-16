task = input("Enter your task for today: ")

priority = input("Enter the task’s priority (high, medium, low): ").lower()

time_bound = input("Is the task time-bound? (yes or no): ").lower()

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
            reminder += "'Finish project report' is a high priority task that requires immediate attention today!"
print(reminder)

   if time_bond == "no":
            reminder += "'Read a book' is a low priority task. Consider completing it when you have free time."
print(reminder)

# ASSIGNMENT : CREATE A DAILY CHECKLIST AND SHOW WHICH TASKS WERE COMPLETED AND WHICH WERE NOT COMPLETED
print("\nLet's create your checklist for the day.")
tasks = []
n = int(input("\nHow many tasks today : "))
for i in range(n):
    tasks.append(input(f"Enter task {i+1} : "))

completed_tasks = []
incomplete_tasks = []

for task in tasks:
    answer = input(f"Did you {task}? (yes/no): ") 
    if answer.lower() == 'yes':                             
        completed_tasks.append(task)
    else:
        incomplete_tasks.append(task)

print("\nThe tasks you Completed are :-")
for i in completed_tasks:
    print(" - ", i)

print("\nThe tasks you didn't complete are :-")
for i in incomplete_tasks:
    print(" - ", i)
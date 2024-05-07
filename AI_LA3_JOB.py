arr = []

def take_input():
    while True:
        job_id = input("Enter job ID (or 'done' to finish): ")
        if job_id == "done":
            break
        duration = int(input("Enter duration of job: "))
        profit = int(input("Enter profit of job: "))
        arr.append([job_id, duration, profit])

take_input()

print("Following is the maximum profit sequence of Jobs: ")
n = len(arr)
t = int(input("Enter total time slots available: "))

for i in range(n):
   for j in range(n - 1 - i):
     if arr[j][2] < arr[j + 1][2]:
       arr[j], arr[j + 1] = arr[j + 1], arr[j]

result = [False] * t
job = ['-1'] * t

for i in range(len(arr)):
   for j in range(min(t - 1, arr[i][1] - 1), -1, -1):
     if result[j] is False:
       result[j] = True
       job[j] = arr[i][0]
       break

print("Job sequence:", job)


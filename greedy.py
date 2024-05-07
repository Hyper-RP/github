def greedy_job_selection(jobs):
    # Sort jobs by profit in descending order
    sorted_jobs = sorted(jobs, key=lambda x: x[1], reverse=True)
    
    # Initialize an empty list to store selected jobs
    selected_jobs = []
    
    # Initialize a set to keep track of selected time slots
    selected_times = set()
    
    # Iterate through sorted jobs
    total_profit = 0
    for job in sorted_jobs:
        name, profit, time = job
        # Check if the time slot is available
        if time not in selected_times:
            # Add job to selected jobs and update selected time slots
            selected_jobs.append(job)
            selected_times.add(time)
            # Update total profit
            total_profit += profit
    
    return selected_jobs, total_profit

# Get user-defined inputs for jobs
num_jobs = int(input("Enter the number of jobs: "))
jobs = []
for i in range(num_jobs):
    name = input("Enter job name: ")
    profit = int(input("Enter profit for {}: ".format(name)))
    time = int(input("Enter time for {}: ".format(name)))
    jobs.append((name, profit, time))

# Get selected jobs using greedy algorithm
selected_jobs, total_profit = greedy_job_selection(jobs)

# Output selected jobs and total profit
print("\nSelected Jobs:")
for job in selected_jobs:
    print("Job:", job[0], "| Profit:", job[1], "| Time:", job[2])
print("Total Profit:", total_profit)



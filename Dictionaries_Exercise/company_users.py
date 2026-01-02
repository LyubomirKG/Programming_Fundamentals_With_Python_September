company_register = {}

while True:
    command = input().split(" -> ")
    if command[0] == "End":
        break
    
    company_name = command[0]
    employee_id = command[1]
    
    # Initialize the list for a new company if it doesn't exist
    if company_name not in company_register:
        company_register[company_name] = []
    
    # Check for uniqueness: only add the ID if it's not already in the list
    if employee_id in company_register[company_name]:
        continue
    
    company_register[company_name].append(employee_id)

# Print results in the required format
for company_name, employee_ids in company_register.items():
    print(f"{company_name}")
    # Using list comprehension and unpack operator to print formatted IDs
    print(*[f"-- {emp_id}" for emp_id in employee_ids], sep="\n")

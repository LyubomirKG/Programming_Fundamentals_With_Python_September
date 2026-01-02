# Step 1: Read number of courses
n = int(input())

# Step 2: Create empty list
courses = []

# Step 3: Read each course and add to list
for _ in range(n):
    course_name = input()
    courses.append(course_name)

# Step 4: Print the list
print(courses)

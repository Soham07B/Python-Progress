users = ["Amit", "Rahul", "Priya", "Soham"]

for user in users:
    print(user)

skills = ["Python", "SQL", "FastAPI"]

for i in range(len(skills)):
    print(i, skills[i])

skills = ["Python", "SQL", "FastAPI"]

for index, skill in enumerate(skills):
    print(index, skill)

skills = ["Python", "SQL", "FastAPI", "PostgreSQL", "Docker"]

for skill in skills:
    if "SQL" in skill:
        print(skill)

students = ["Amit", "Priya", "Rahul", "Soham"]
for index, student in enumnerate(students, start=1):
    print(index, student)

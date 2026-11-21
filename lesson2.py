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

languages = ["PYTHON", "java", "C++", "JavaScript", "RUBY"]
for language in languages:
    if "y" in language.lowe():
        print(language)
#list comprehension
numbers=[10,20,30,40,50]
result=[number for number in numbers if number>20]
print(result)

numbers = [5, 10, 15, 20, 25, 30]

result=[number for number in numbers if number >=15]
print(result)

numbers = [5, 10, 15, 20, 25, 30]

# Filtering
result = [number for number in numbers if number > 10]


# Transformation
result = [number * 2 for number in numbers]
#using both
result = [number * 2 for number in numbers if number > 10]

print(result)

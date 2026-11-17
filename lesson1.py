name="Soham"
age=23
degree="M.Sc"
germanLevel="A2"
programmingLanguages=["Java","Python","Javascript"]
print(f"My name is {name}. My age is {age}. My degree is {degree}. My german level is {germanLevel}. I know {programmingLanguages}")
programmingLanguages.append("C++") 
germanLevel="A2.2"
print(f"I also know {programmingLanguages[3]}. And my language level is {germanLevel}")


backend_skills = ["Python", "SQL", "FastAPI", "Docker"]
print(backend_skills[0])
print(backend_skills[-1])
backend_skills[1]="PostgreSQL"
backend_skills.append("Git")
backend_skills.insert(2,"Redis")
backend_skills.remove("Docker")
print(backend_skills)
print(len(backend_skills))

skills = ["Python", "SQL", "FastAPI", "Docker", "Redis"]

print(skills[1:4])

skills[:3]    # First three elements
skills[2:]    # From index 2 to the end
skills[:]     # Entire list (shallow copy)
skills[-3:]

numbers = [0, 1, 2, 3, 4, 5, 6, 7]

print(numbers[::2])
print(numbers[::-1])

data = [10, 20, 30, 40, 50, 60, 70, 80]

print(data[2:6])
print(data[:4])
print(data[-3:])
print(data[::2])
print(data[::-1])

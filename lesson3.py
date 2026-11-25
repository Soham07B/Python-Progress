numbers = [10, 20, 30, 40]

def calculate_average(numbers):
    total=0
    for number in numbers:   #return sum(numbers) / len(numbers) [Also a way]
        total+=number
    return total/len(numbers)
    
result = calculate_average(numbers)

print(result)

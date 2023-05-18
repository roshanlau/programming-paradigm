# Question 1
count = 1

while count <= 10:
    print(count)
    if count == 5:
        print("Python")
    count += 1

# Question 2
numbers = []
for i in range(10):
    numbers.append(float(input(f"Input Number {i + 1}: ")))

numbers_sum = sum(numbers)

numbers_product = 1
for n in numbers:
    numbers_product *= n
numbers_average = numbers_sum/len(numbers)

print("Sum\t: ", numbers_sum)
print("Product\t: ", numbers_product)
print("Average\t: ", numbers_average)

#Question 3
def make_sandwich(*items):
    print("Summary of sandwich ordered:")
    for item in items:
        print(f"- {item}")
    print("Done!")

make_sandwich('Peanut butter', 'Butter')
make_sandwich('Tuna', 'Tomato', 'Lettuce')
make_sandwich('Crispy Chicken', 'Lettuce', 'Tomato', 'Chilli Sauce')

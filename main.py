MAX = 1500
numbers = []
numbers_2 = []
perfect_squares = []

x = int(MAX**(1/2))
for i in range(1, x+1):
    numbers.append(i)


for num in numbers:
    num = (num**2)
    numbers_2.append(num)

print(numbers_2)

# for i in range(1,11):
#     y = numbers_2.findall(i)
#     print(y)



    
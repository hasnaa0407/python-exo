
numbers = []
shoe_sizes = []
i=1
while i<=5:
    numbers.append(i)
    i+=1
for size in [8, 9, 10, 11, 12]:
    shoe_sizes.append(size)
print("Numbers List:", numbers)
print("Shoe Sizes List:", shoe_sizes)
numbers.append(3)
combined_list = numbers + shoe_sizes
print("Combined List:", combined_list)

# Calculate the difference between the sum of the squares and the square of the sums for the first 10 natural numbers
sum=0
result=0    

for i in range(1, 11):
    square = i * i
    result = square + result
print(result)

for i in range(1, 11):
    sum= sum+i
    total= sum*sum
print(total)

print(total - result)
    
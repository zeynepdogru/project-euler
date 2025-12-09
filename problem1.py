# Print all numbers from 1 to 1000 that are multiples of 3 or 5
for i in range(1, 101):
    if i%3 == 0 or i%5 == 0:
        print(i)
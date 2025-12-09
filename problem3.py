# Find the largest prime factor of the number 13195
number = 13195
largest_prime = []

def is_prime(n):
    if n <= 1:
        return False
    for j in range(2, n):
        if n % j == 0:
            return False
    return True 


for i in range(1, number ):
    if number % i == 0 and is_prime (i):
        largest_prime.append(i)

print("The prime factor of", number, "is", largest_prime)
print("The largest prime factor of", number, "is", max(largest_prime)) 

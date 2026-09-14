# Display prime numbers from 1 to 250
# and save them in results.txt

prime_numbers = []

for number in range(2, 251):
    is_prime = True

    for divisor in range(2, int(number ** 0.5) + 1):
        if number % divisor == 0:
            is_prime = False
            break

    if is_prime:
        prime_numbers.append(number)

with open("results.txt", "w") as file:
    for prime in prime_numbers:
        print(prime)
        file.write(str(prime) + "\n")

print("\nThe prime numbers were saved in results.txt.")
## prompt the user to enter a positive number n

n = int(input("Enter a positive number:"))
sum_even = 0
for i in range(1, n + 1):
      if i % 2 == 0:
       sum_even += i
## display result
print(f"Sum of even numbers:",sum_even)


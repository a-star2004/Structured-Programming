## allow user to enter enter 5 numbers, storing them in a list
numbers = []
print("Enter 5 numbers:")
for i in range(5):
    num = int(input())
    numbers.append(num)
    #Display the list of numbers
    print("Numbers:",numbers)
    #display the maximum, minimum, and average
    print("Maximum:", max(numbers))
    print("Minimum:", min(numbers))
    print("Average", sum(numbers) / len(numbers))
    #display the list in sorted order
    print("Sorted:", sorted(numbers))

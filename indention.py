## Even and Odd numbers
def main():
    print("Welcome to the Indentation Race!")
    for i in range(5):
        print("Current number:", i)
        if i % 2 == 0:
            print("Even number.")
        else:
            print("Odd number.")
    print("Race completed!")
main()

## Total Cost calculator
def calculate_total_price(item_price, quantity):
    item_total = item_price * quantity
    tax_rate = 0.07
    tax_amount = item_total * tax_rate
    total_price = item_total + tax_amount
    discount = 0.1
    discounted_price = total_price - (total_price * discount)
    return discounted_price
item_price = 25.0
quantity = 4
print("Total Price:", calculate_total_price(item_price, quantity))
    
    ## Average calculator
def calculate_average(numbers):
    total = 0
    for number in numbers:
        total += number
    average = total / len(numbers)
    return average
def classify_average(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    return "F"
student_scores = [95, 88, 72, 65, 79]
average_score = calculate_average(student_scores)
letter_grade = classify_average(average_score)
print("Average Score:", average_score)
print("Letter Grade:", letter_grade)

## Investigation Scene
flashlight_available = True
def investigate_scene():
    print("You arrive at a dimly lit room with clues scattered around.")
    if flashlight_available:
        print("You can see better with your flashlight.")
    print("You find a note on the table.")
    if flashlight_available:
        print("The note reads, 'The code to the safe is 4732.'")
    else:
        print("The note reads, 'You need to find the flashlight first.'")
def open_safe(code):
    if code == 4732:
        print("The safe opens, revealing a hidden treasure.")
        print("Congratulations! You solved the mystery.")
    else:
        print("The safe remains locked. Try again.")

 ## Student Information Display
def display_student_info(name, age):
    print("Student Name:", name)
    print("Student Age:", age)
    if age < 18:
        print("Status: Minor")
    else:
        print("Status: Adult")
    return
student_name = "Alice"
student_age = 20
display_student_info(student_name, student_age)

## Fancy Average Calculator
def calculate_average(numbers):
    sum = 0
    for number in numbers:
        sum += number
    average = sum / len(numbers)
    return average
numbers = [12, 8, 16, 4, 20]
average = calculate_average(numbers)
print("Average:", average)
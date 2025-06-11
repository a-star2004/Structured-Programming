## differentiate between assigning and declaring a variable giving practical examples of each
"assigning is variable means giving a variable a specific value while declaring a variable means introducing a new vaiableto the program"
"Examples of assigning variables"
x = 10
"Examples of declaring a variable"
x = None

## convert the variables from string to integer
#integer "8"
#convert the integer to a string
string_int = "8"
string_int = int(string_int)
print(string_int)

length = "56.90" ## convert to integer
float_length = float(length) 
int_length = int(float_length) 
print(int_length)

height = "34.09944" ## convert to integer
float_height = float(height)
int_height = int(float_height)
print(int_height)

print("Welcome to MUBS grading system")
marks = int(input("please enter marks between 0 and 100"))
if marks >= 91 and marks <= 100:
    print("A+")
elif marks >= 81 and marks <=90:
   print("A")
elif marks >=71 and marks <=80:
   print("B+")  
elif marks >=61 and marks <=70:
   print("B")
elif marks >=51 and marks <=60:
   print("C+")
elif marks >=41 and marks <=50:
   print("C")
elif marks >=31 and marks <=40:
   print("D+")
elif marks >=21 and marks <=30:
   print("D")
elif marks >=11 and marks <=20:
   print("E")
elif marks >=0 and marks <=10:
   print("fail")
else:
    print("Invalid please enter a mark between 0 and 100")





'''Write a menu driven program to perform the
following menu: (1) Find Area of Circle (2)
Find Area of Triangle (3) Find Area of Square
(4) Find Simple Interest (5) Exit. (using match-
case)'''


print("menu:")
print("1. Find Area of Circle")
print("2. Find Area of Triangle")   
print("3. Find Area of Square")
print("4. Find Simple Interest")
print("5. Exit")
choice = int(input("Enter your choice (1-5): "))
match choice:
    case 1:
        radius = float(input("Enter the radius of the circle: "))
        area = 3.14 * radius * radius
        print(f"The area of the circle is: {area}")
        
    case 2:
        base = float(input("Enter the base of the triangle: "))
        height = float(input("Enter the height of the triangle: "))
        area = 0.5 * base * height
        print(f"The area of the triangle is: {area}")
        
    case 3:
        side = float(input("Enter the side of the square: "))
        area = side * side
        print(f"The area of the square is: {area}")
        
    case 4:
        principal = float(input("Enter the principal amount: "))
        rate = float(input("Enter the rate of interest: "))
        time = float(input("Enter the time (in years): "))
        interest = (principal * rate * time) / 100
        print(f"The simple interest is: {interest}")
        
    case 5:
        print("Exiting the program.")
        
    case _:
        print("Invalid choice. Please select a valid option.")
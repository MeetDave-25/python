'''Write a program to search an element in the list using
for loop and also demonstrate the use of “else” with for loop.'''

number = [10,20,30,40,50]
print("List of numbers:", number)
search = int(input("Enter the number to search: "))
for i in number:
    if i == search:
        print(f"{search} found in the list.")
        break
else:
    print(f"{search} not found in the list.")
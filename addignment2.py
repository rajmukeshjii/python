
def area(side_length):
    return side_length * side_length

# Input: Get the side length from the user
try:
    side_length = float(input("Enter the side length of the square: "))
    
    # Check if the side length is valid (positive)
    if side_length < 0:
        print("Side length cannot be negative.")
    else:
        # Calculate and print the area using the area() function
        square_area = area(side_length)
        print(f"The area of the square with side length {side_length} is {square_area}")
except ValueError:
    print("Invalid input. Please enter a valid number for the side length.")

def square_and_separate(start, end):
    even_squares = []
    odd_squares = []
    
    for num in range(start, end + 1):
        square = num ** 2
        
        if square % 2 == 0:
            even_squares.append(square)
        else:
            odd_squares.append(square)
            
    print(f"\nEven squares in the range: {even_squares}")
    print(f"Odd squares in the range: {odd_squares}")

try:
    range_start = int(input("Enter the beginning of the range: "))
    range_end = int(input("Enter the end of the range: "))

    square_and_separate(range_start, range_end)

except ValueError:
    print("Please enter valid integers for the range.")
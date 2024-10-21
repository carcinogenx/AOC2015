
#parsing input
def find_floor(instructions):
    floor = 0
    for char in instructions: 
        if char == '(':
            floor += 1
        elif char == ')':
            floor -= 1
    return floor


#take input from terminal
instructions = input("Enter the instructions for Satan: ")


result = find_floor(instructions)
print("Satan ends up on floor:", result)

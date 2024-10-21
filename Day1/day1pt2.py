

#parsing input
def find_floor(instructions):
    floor = 0
    for position, char in enumerate(instructions, start=1):
        if char == '(':
            floor += 1
        elif char == ')':
            floor -= 1
        if floor == -1:
            return position
    return None


#take input from terminal
instructions = input("Enter the instructions for Satan: ")


position = find_floor(instructions)

if position:
    print("satan first enters the basement at position:", position)
else:
    print("satan never enters the basement")

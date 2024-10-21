

def calculate_ribbon(dimensions):
    total_ribbon = 0
    for dimension in dimensions:
        l, w, h = map(int, dimension.split('x'))
        smallest_perimeter = 2 * min(l + w, w + h, h + l)
        volume = l * w * h
        total_ribbon += smallest_perimeter + volume
    return total_ribbon

dimensions = []
print("enter dimensions and send done when done")
while True:
    line = input()
    if line.lower() == "done":
        break
    dimensions.append(line)

total_ribbon = calculate_ribbon(dimensions)
print("total ribbon needed:", total_ribbon)

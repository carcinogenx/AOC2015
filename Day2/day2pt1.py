

def calculate_paper(dimensions):
    total_paper = 0
    for dimension in dimensions:
        l, w, h = map(int,dimension.split('x'))
        surface_area = 2 * l * w + 2 * w * h + 2 * h * l
        smallest_side = min(l * w, w * h, h * l)
        total_paper += surface_area + smallest_side
    return total_paper


dimensions = []

print("enter dimensions and send done when done")
while True:
    line = input()
    if line.lower() == "done":
        break
    dimensions.append(line)


total_paper = calculate_paper(dimensions)
print("total paper is", total_paper)

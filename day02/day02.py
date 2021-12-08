with open("input.txt","r") as f:
    directions = f.readlines()

horizontal = 0
depth = 0
aim = 0
for dir in directions:
    vector, mag = dir.split(" ")
    mag = int(mag)
    
    if vector == "down":
        # depth += mag
        aim += mag
    
    if vector == "up":
        # depth -= mag
        aim -= mag

    if vector == "forward":
        horizontal += mag
        depth += (mag * aim)
    
    if depth < 0:
        print("Something's wrong")

print(f'Final depth: {depth}, final horiztonal: {horizontal}')
print(depth * horizontal)
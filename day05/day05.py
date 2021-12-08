def read_file(filename):
    lines = []
    with open(filename,'r') as f:
        for line in f:
            points = line.split(' -> ')
            lines.append([int(p) for p in points[0].split(',')] + [int(p) for p in points[1].split(',')])

    return lines

def part_1(lines):
    max_x = max(max([p[0],p[2]]) for p in lines) + 1
    max_y = max(max([p[1],p[3]]) for p in lines) + 1

    grid = []
    for y in range(max_y):
        row = []
        for x in range(max_x):
            row.append(0)
        grid.append(row)

    for line in lines:
        x_start = min([line[0],line[2]])
        x_end = max([line[0],line[2]])
        y_start = min([line[1],line[3]])
        y_end = max([line[1],line[3]])

        if line[0] == line[2]:
            # vertical line
            for y in range(y_start,y_end + 1):
                grid[y][line[0]] += 1
        
        elif line[1] == line[3]:
            # horizontal line
            for x in range(x_start,x_end + 1):
                grid[line[1]][x] += 1

    return grid

def sign(diff):
    if diff == 0:
        return 1
    
    return int(diff / abs(diff))

def part_2(lines):
    max_x = max(max([p[0],p[2]]) for p in lines) + 1
    max_y = max(max([p[1],p[3]]) for p in lines) + 1

    grid = []
    for y in range(max_y):
        row = []
        for x in range(max_x):
            row.append(0)
        grid.append(row)

    for line in lines:
        x_sign = sign(line[2] - line[0])
        y_sign = sign(line[3] - line[1])
        x_range = range(line[0], line[2] + x_sign, x_sign)
        y_range = range(line[1], line[3] + y_sign, y_sign )

        if line[0] == line[2]:
            # vertical line
            for y in y_range:
                grid[y][line[0]] += 1
        
        elif line[1] == line[3]:
            # horizontal line
            for x in x_range:
                grid[line[1]][x] += 1
        
        else:
            m = (line[3] - line[1]) / (line[2] - line[0])
            b = line[3] - (m * line[2])
            for x in x_range:
                y = int(m * x + b)
                grid[y][x] += 1

    return grid

def count_grid(grid):
    n_overlap = 0
    for row in grid:
        for cell in row:
            if cell > 1:
                n_overlap += 1
    return n_overlap

if __name__ == "__main__":
    lines = read_file("input.txt")
    grid = part_1(lines)
    print(count_grid(grid))
    grid = part_2(lines)
    print(count_grid(grid))
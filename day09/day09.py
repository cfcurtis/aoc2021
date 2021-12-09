def read_input(filename):
    grid = []
    with open(filename,'r') as f:
        for line in f:
            grid.append([int(tok) for tok in line if tok.isnumeric()])
    
    return grid

def get_adjacent_points(grid, i, j):
    adjacent = []
    if i > 0:
        adjacent.append([i-1, j])
    if j > 0:
        adjacent.append([i, j-1])
    if i < len(grid) - 1:
        adjacent.append([i+1, j])
    if j < len(grid[i]) - 1:
        adjacent.append([i, j+1])
    
    return adjacent       

def is_low_point(grid, pt, adjacent):
    if len(adjacent) == 0:
        return False

    return all([grid[pt[0]][pt[1]] < grid[p[0]][p[1]] for p in adjacent])

def get_basin(grid, pt, basin):
    adjacent = get_adjacent_points(grid, pt[0], pt[1])

    # remove anything currently in the basin from the list of adjacent points
    for b in basin:
        if b in adjacent:
            adjacent.remove(b)

    if is_low_point(grid, pt, adjacent):
        basin.append(pt)
        for ap in adjacent:
            basin = get_basin(grid, ap, basin)
    
    return basin


def part_1(grid):
    risk = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            adjacent = get_adjacent_points(grid, i, j)
            if is_low_point(grid, [i,j], adjacent):
                risk += grid[i][j] + 1
    
    print(risk)

def part_2(grid):
    basins = []
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            adjacent = get_adjacent_points(grid, i, j)
            if is_low_point(grid, [i, j], adjacent):
                # get the size of the basin
                basins.append(len(get_basin(grid, [i,j],basin=[])))

    basins.sort(reverse=True)
    print(basins[0]*basins[1]*basins[2])

if __name__ == "__main__":
    depths = read_input("input.txt")
    part_1(depths)
    part_2(depths)
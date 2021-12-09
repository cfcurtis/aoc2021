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
    return all([grid[pt[0]][pt[1]] < grid[p[0]][p[1]] for p in adjacent])

def get_basin(grid, i, j, basin):
    adjacent = get_adjacent_points(grid, i, j)
    basin.append([i,j])

    for pt in adjacent:
        pt_adjacent = get_adjacent_points(grid, pt[0], pt[1])
        for b in basin:
            if b in pt_adjacent:
                pt_adjacent.remove(b)
        
        if is_low_point(grid, pt, pt_adjacent):
            basin += get_basin(grid, pt[0], pt[i], basin)
    
    return basin



def get_basin_recursion(grid, i, j, basin):
    # get the neighbouring points, and remove anything in the current basin
    adjacent = get_adjacent_points(grid, i, j)
    
    for pt in adjacent:
        # get this point's neighbours and compare, but remove the current basin first
        pt_adjacent = get_adjacent_points(grid, pt[0], pt[1])
        for b in basin:
            if b in pt_adjacent:
                pt_adjacent.remove(b)

        if is_low_point(grid, pt, pt_adjacent):
            basin.append(pt)
    
    return len(basin)
    


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
                basins.append(get_basin(grid, i, j, []))

    print(basins)

if __name__ == "__main__":
    depths = read_input("example.txt")
    part_1(depths)
    part_2(depths)
class BasinFinder:
    grid = []
    basins = []
    def __init__(self, filename) -> None:
        with open(filename,'r') as f:
            for line in f:
                self.grid.append([int(tok) for tok in line if tok.isnumeric()])
        
        
    def show_basin(self, basin):
        min_i = max(min([pt[0] for pt in basin]) - 1, 0)
        min_j = max(min([pt[1] for pt in basin]) - 1, 0)
        max_i = min(max([pt[0] for pt in basin]) + 1, len(self.grid) - 1)
        max_j = min(max([pt[1] for pt in basin]) + 1, len(self.grid[0]) - 1)

        print("")
        for i in range(min_i, max_i + 1):
            row = ''
            for j in range(min_j, max_j + 1):
                if (i, j) in basin:
                    row += f'({self.grid[i][j]})'
                else:
                    row += f' {self.grid[i][j]} '
            
            print(row)
        
        print("")

    def get_adjacent_points(self, pt):
        adjacent = []
        if pt[0] > 0:
            adjacent.append((pt[0] - 1, pt[1]))
        if pt[1] > 0:
            adjacent.append((pt[0], pt[1] - 1))
        if pt[0] < len(self.grid) - 1:
            adjacent.append((pt[0] + 1, pt[1]))
        if pt[1] < len(self.grid[pt[0]]) - 1:
            adjacent.append((pt[0], pt[1] + 1))
        
        return adjacent       

    def is_low_point(self, pt, adjacent):
        if len(adjacent) == 0:
            return False

        return all([self.grid[pt[0]][pt[1]] < self.grid[p[0]][p[1]] for p in adjacent])

    def get_basin(self, pt, basin):
        if self.grid[pt[0]][pt[1]] == 9:
            # at the boundary, we're done
            return basin
        
        for b in self.basins:
            if any([pt in b]):
                # merge the basins and update the reference
                b += basin
                basin = b
        
        # add the current point to the basin, then check adjacent
        basin.append(pt)
        adjacent = self.get_adjacent_points(pt)

        # remove anything currently in the basin from the list of adjacent points
        for b in basin:
            if b in adjacent:
                adjacent.remove(b)
        
        for ap in adjacent:
            basin = self.get_basin(ap, basin)
        
        return basin

    def part_1(self):
        risk = 0
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                adjacent = self.get_adjacent_points((i, j))
                if self.is_low_point((i, j), adjacent):
                    risk += self.grid[i][j] + 1
        
        print(risk)

    def part_2(self):
        basin_size = []
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                if self.grid[i][j] != 9 and all([(i, j) not in b for b in self.basins]):
                    self.basins.append(self.get_basin((i, j),basin=[]))
                    # self.show_basin(self.basins[-1])
                    # remove duplicates, not particularly efficient
                    self.basins[-1] = set(self.basins[-1])

        basin_size = [len(b) for b in self.basins]
        basin_size.sort(reverse=True)
        print(basin_size[0]*basin_size[1]*basin_size[2])

if __name__ == "__main__":
    bf = BasinFinder("input.txt")
    bf.part_1()
    bf.part_2()
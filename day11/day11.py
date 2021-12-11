class Octopus:
    energy = []
    flashed = []

    def __init__(self,filename):
        self.energy = []
        with open(filename, 'r') as f:
            for line in f.readlines():
                self.energy.append([int(tok) for tok in line.strip()])
                self.flashed.append([False] * len(self.energy[0]))
    
    def i_win(self,i):
        return range(max(0, i-1), min(i + 2, len(self.energy)))
    
    def j_win(self,j):
        return range(max(0, j-1), min(j + 2, len(self.energy[0])))

    def print_energy(self):
        for row in self.energy:
            print("".join([str(e) for e in row]))

    def all_neighbours_flashed(self, i, j):
        if i == 0 or i == len(self.energy) - 1 or \
           j == 0 or j == len(self.energy[i]) - 1:
            return False

        for ii in range(i-1, i+2):
            for jj in range(j-1, j+2):
                if ii != jj and not self.flashed[ii][jj]:
                    return False
        
        return True

    def increment_neighbours(self):
        changing = False
        for i in range(len(self.energy)):
            for j in range(len(self.energy[i])):
                if self.energy[i][j] > 9 and not self.flashed[i][j]:
                    changing = True
                    self.flashed[i][j] = True
                    # increment the neighbours
                    for ii in self.i_win(i):
                        for jj in self.j_win(j):
                            self.energy[ii][jj] += 1
        
        # if anything changed, go again
        if changing:
            self.increment_neighbours()

    def part_1(self, steps):
        flashes = 0
        for step in range(steps):
            # they all increment
            for i in range(len(self.energy)):
                for j in range(len(self.energy[i])):
                    self.energy[i][j] += 1
            
            # then they influence their neighbours
            self.increment_neighbours()

            # check which ones flashed and reset
            for i in range(len(self.energy)):
                for j in range(len(self.energy[i])):
                    if self.flashed[i][j] or self.all_neighbours_flashed(i, j):
                        flashes += 1
                        self.flashed[i][j] = False
                        self.energy[i][j] = 0
        
        print(flashes)
    
    def part_2(self):
        flashes = 0
        counter = 0
        all_octopi = len(self.energy) * len(self.energy[0])
        while flashes < all_octopi:
            flashes = 0
            # they all increment
            for i in range(len(self.energy)):
                for j in range(len(self.energy[i])):
                    self.energy[i][j] += 1
            
            # then they influence their neighbours
            self.increment_neighbours()

            # check which ones flashed and reset
            for i in range(len(self.energy)):
                for j in range(len(self.energy[i])):
                    if self.flashed[i][j] or self.all_neighbours_flashed(i, j):
                        flashes += 1
                        self.flashed[i][j] = False
                        self.energy[i][j] = 0
            
            counter += 1

        print(counter)

if __name__ == "__main__":
    octopi = Octopus("input.txt")
    # octopi.part_1(100)
    octopi.part_2()
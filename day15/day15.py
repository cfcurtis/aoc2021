risk = []
min_path = []
min_risk = 0
last_row = 0
last_col = 0

def read_file(filename):
    with open(filename,'r') as f:
        global risk
        global visited
        risk = []
        for line in f:
            risk.append([int(tok) for tok in list(line.strip())])

def get_neighbours(pt):
    neighbours = []
    if pt[0] > 0:
        neighbours.append((pt[0]-1, pt[1]))
    if pt[1] > 0:
        neighbours.append((pt[0], pt[1]-1))
    if pt[0] < len(risk) - 1:
        neighbours.append((pt[0]+1, pt[1]))
    if pt[1] < len(risk[0]) - 1:
        neighbours.append((pt[0], pt[1]+1))
    
    return neighbours

def print_risk():
    for i in range(len(risk)):
        row = ''
        for j in range(len(risk[i])):
            if (i,j) in min_path:
                row += str(risk[i][j])
            else:
                row += '.'
        print(row)

def walk(current_path, pt, val):
    global min_path
    global min_risk
    
    if val > min_risk:
        # no use continuing on, it's already bigger
        return

    # add upon entry
    current_path.append(pt)
    val += risk[pt[0]][pt[1]]
    # print('Visiting ', current_pt)

    # check if we've hit a new minimum
    if pt == (last_row, last_col):
        if val < min_risk:
            min_risk = val
            min_path = current_path
        return

    # otherwise, get all the neighbours and iterate
    neighbours = [(i,j) for i in range(pt[0]-1, pt[1] + 2) for j in range(pt[0]-1, pt[1] + 2)]
    neighbours = [n for n in neighbours if n not in current_path]

    if len(neighbours) == 0:
        return

    n_risk = [risk[n[0]][n[1]] for n in neighbours]
    neighbours = [n for _, n in sorted(zip(n_risk,neighbours))]
    
    for n in neighbours:
        branch = current_path.copy()
        walk(branch, n, val)

def part_1():
    global min_risk
    global last_row
    global last_col
    last_row = len(risk) - 1
    last_col = len(risk[0]) - 1

    # initialize min_risk to the diagonal
    min_risk = 0
    for i in range(len(risk)):
        for j in range(len(risk[i])):
            min_risk += risk[i][j]

    print('Diagonal risk:', min_risk)

    walk([],(0,0),0)
    print_risk()
    print(min_risk - risk[0][0])

if __name__ == '__main__':
    read_file('example.txt')
    
    import cProfile
    cProfile.run('part_1()')
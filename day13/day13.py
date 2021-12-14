
def read_input(filename):
    dots = []
    folds = []
    with open(filename,'r') as f:
        line = f.readline()
        while line.strip():
            dots.append([int(tok) for tok in line.strip().split(',')])
            line = f.readline()
                   
        line = f.readline()
        while line.strip():
            toks = line[11:].split('=')
            if toks[0] == 'x':
                folds.append([int(toks[1]), 0])
            else:
                folds.append([0, int(toks[1])])
            line = f.readline()
    
    return dots, folds

def fold(dots,fold):
    if fold[0] == 0:
        # y axis fold
        return set([(dot[0],abs(dot[1] - fold[1]) + fold[1]) for dot in dots])
    else:
        # x axis fold
        return set([(abs(dot[0] - fold[0]) + fold[0], dot[1]) for dot in dots])

def display(dots):
    min_x = min([dot[0] for dot in dots])
    min_y = min([dot[1] for dot in dots])
    max_x = max([dot[0] for dot in dots])
    max_y = max([dot[1] for dot in dots])

    grid = []
    for row in range(max_y - min_y + 1):
        grid.append(['.'] * (max_x - min_x + 1))

    for dot in dots:
        grid[dot[1] - min_y][dot[0] - min_x] = '#'
    
    with open('output.txt','w') as f:
        for row in grid:
            f.write("".join(row) + '\n')

if __name__ == '__main__':
    dots, folds = read_input('input.txt')
    
    # part 1
    folded = fold(dots,folds[0])
    print(len(folded))

    # part 2
    for f in folds[1:]:
        folded = fold(folded,f)
    
    # visualize
    display(folded)
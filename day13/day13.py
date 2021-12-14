
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

def get_dot_range(dots):
    min_x = min([dot[0] for dot in dots])
    max_x = max([dot[0] for dot in dots])
    min_y = min([dot[1] for dot in dots])
    max_y = max([dot[1] for dot in dots])
    return min_x, max_x, min_y, max_y

def fold(dots,fold):
    if fold[0] == 0:
        # y axis fold
        return set([(dot[0], abs(dot[1] - fold[1]) - 1) for dot in dots])
    else:
        # x axis fold
        return set([(abs(dot[0] - fold[0]) - 1, dot[1]) for dot in dots])

def display(dots):
    grid = []
    _, max_x, _, max_y = get_dot_range(dots)

    for row in range(max_y + 1):
        grid.append(['.'] * (max_x + 1))

    for dot in dots:
        grid[dot[1]][dot[0]] = '#'
    
    for row in grid[::-1]:
        print("".join(row[::-1]))

if __name__ == '__main__':
    dots, folds = read_input('input.txt')

    print('Initial range:')
    print(get_dot_range(dots))
    
    # part 1
    folded = fold(dots,folds[0])
    print(len(folded))

    # part 2
    for f in folds:
        dots = fold(dots,f)

    # visualize
    display(dots)
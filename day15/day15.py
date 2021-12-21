risk = []

def read_file(filename):
    with open(filename,'r') as f:
        global risk
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

def print_risk(path, min_risk = None):
    for i in range(len(risk)):
        row = ''
        for j in range(len(risk[i])):
            if (i,j) in path:
                if min_risk is not None:
                    row += f'{min_risk[(i,j)]:4}'
                else:
                    row += str(risk[i][j])
            else:
                row += '.'
        print(row)

def part_1():
    # initialize min_risk to big number
    min_risk = {(i,j): 2**32 for i in range(0,len(risk)) for j in range(0,len(risk[0]))}
    visited = set()
    current = (0,0)
    min_risk[current] = 0
    to_visit = [(0, current)]

    while to_visit:
        # sort to find the lowest one to check next
        to_visit.sort(reverse=True)
        current_total, current = to_visit.pop()
        visited.add(current)

        # get the neighbours and their risk values
        neighbours = [n for n in get_neighbours(current) if n not in visited]

        for n in neighbours:
            total_risk = risk[n[0]][n[1]] + current_total
            if total_risk < min_risk[n]:
                min_risk[n] = total_risk

                # add the total risk to the list to visit
                to_visit.append((total_risk,n))
        
            
    print(min_risk[(len(risk) - 1, len(risk[0]) - 1)])

if __name__ == '__main__':
    read_file('input.txt')
    part_1()
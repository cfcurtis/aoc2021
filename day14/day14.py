def read_input(filename):
    with open(filename,'r') as f:
        template = f.readline().strip()
        f.readline()
        pairs = {}
        for line in f:
            toks = line.strip().split(' -> ')
            pairs[toks[0]] = toks[1]
    
    return template,pairs

def grow_polymer(template,pairs):
    polymer = template
    counts = {val: polymer.count(val) for val in pairs.values()}
    prev = 1
    for i in range(1,len(template)):
        polymer = polymer[:prev] + pairs[template[i-1:i+1]] + polymer[prev:]
        prev += 2
        counts[pairs[template[i-1:i+1]]] += 1
    
    return polymer, counts
    
def part_1(template,pairs,reps):
    polymer = template
    total_counts = {val: polymer.count(val) for val in pairs.values()}
    for _ in range(reps):
        polymer, counts = grow_polymer(polymer, pairs)
        total_counts = {k: total_counts[k] + counts[k] for k in total_counts.keys()}
    
    print(max(counts.values()) - min(counts.values()))

def part_2(template,pairs,reps):
    total_counts = {val: template.count(val) for val in pairs.values()}
    polymer = template

    # group the letters, just like the fish
    for rep in range(reps):
        print(f'Rep {rep}: {polymer}')
        combos = [polymer[i-1:i+1] for i in range(1,len(polymer))]
        poly_set = set(combos)
        polymer = polymer[0]

        # need to account for multipliers
        for p in poly_set:
            polymer += pairs[p] + p[1]
            total_counts[pairs[p]] += combos.count(p)
        
        print(total_counts)

    print(total_counts)

if __name__ == '__main__':
    template,pairs = read_input('example.txt')
    part_1(template,pairs,10)
    part_2(template,pairs,10)

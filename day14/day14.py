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
    # split and grow independently
    to_grow = template
    for _ in range(2):
        polymers = [to_grow[i:i+2] for i in range(len(to_grow) - 1)]
        for i in range(len(polymers)):
            for rep in range(reps):
                polymers[i], counts = grow_polymer(polymers[i],pairs)
                total_counts = {k: total_counts[k] + counts[k] for k in total_counts.keys()}
                if 'BH' in polymers[i]:
                    print('BH found')
            
            # collapse each one down to its ends
            polymers[i] = polymers[i][0] + polymers[i][-1]
        
        # cut off the ends
        polymers[0] = polymers[0][1]
        polymers[-1] = polymers[-1][0]

        # concatenate into the new one to grow
        to_grow = ''.join(polymers)

    print(total_counts)
    print(max(counts.values()) - min(counts.values()))


if __name__ == '__main__':
    template,pairs = read_input('example.txt')
    part_1(template,pairs,10)
    part_2(template,pairs,10)

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

def part_2(template,pairs):
    polymer = template
    total_counts = {val: polymer.count(val) for val in pairs.values()}
    for group in range(4):
        for rep in range(10):
            polymer, counts = grow_polymer(polymer, pairs)
            total_counts = {k: total_counts[k] + counts[k] for k in total_counts.keys()}
        
        # grow up to 10, then split
        p_len = len(polymer) // 4
        polymers = [
            polymer[:p_len],
            polymer[p_len:2*p_len],
            polymer[2*p_len:3*p_len],
            polymer[3*p_len:]
        ]



    print(total_counts)
    print(max(counts.values()) - min(counts.values()))


if __name__ == '__main__':
    template,pairs = read_input('example.txt')
    part_1(template,pairs,10)
    part_2(template,pairs,10)

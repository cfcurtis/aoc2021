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
    for rep in range(reps):
        polymer, counts = grow_polymer(polymer, pairs)
        print(f'Rep {rep}: ', counts)
        total_counts = {k: total_counts[k] + counts[k] for k in total_counts.keys()}
    
    print(max(counts.values()) - min(counts.values()))

def part_2(template,pairs,reps):
    letter_counts = {val: template.count(val) for val in pairs.values()}
    pair_counts = {key: 0 for key in pairs.keys()}
    for i in range(1,len(template)):
        pair_counts[template[i-1:i+1]] += 1

    # group the letters, just like the fish
    for rep in range(reps):
        print(f'Rep {rep}: {letter_counts}')
        this_rep = pair_counts.copy()
        for pair, count in this_rep.items():
            new_letter = pairs[pair]
            letter_counts[new_letter] += count
            pair_counts[pair[0] + new_letter] += count
            pair_counts[new_letter + pair[1]] += count
            # remove the pair we just split up
            pair_counts[pair] -= count

    print(max(letter_counts.values()) - min(letter_counts.values()))

if __name__ == '__main__':
    template,pairs = read_input('input.txt')
    part_1(template,pairs,10)
    part_2(template,pairs,40)

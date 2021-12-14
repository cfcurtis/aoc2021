def read_input(filename):
    with open(filename,'r') as f:
        template = f.readline().strip()
        f.readline()
        pairs = {}
        for line in f:
            toks = line.strip().split(' -> ')
            pairs[toks[0]] = toks[1]
    
    return template,pairs

def part_1(template,pairs,reps):
    polymer = template
    counts = {val: polymer.count(val) for val in pairs.values()}
    for _ in range(reps):
        prev = 1
        for i in range(1,len(template)):
            polymer = polymer[:prev] + pairs[template[i-1:i+1]] + polymer[prev:]
            prev += 2
            counts[pairs[template[i-1:i+1]]] += 1
        template = polymer
    
    print(max(counts.values()) - min(counts.values()))


if __name__ == '__main__':
    template,pairs = read_input('input.txt')
    part_1(template,pairs,10)

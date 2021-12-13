class Cave:
    def __init__(self,name):
        self.name = name
        self.connections = []
    
    def is_small(self):
        return self.name.islower()
    
    def is_end(self):
        return self.name == 'end'

    def add_connection(self,conn):
        if conn not in self.connections:
            self.connections.append(conn)
    
    def __eq__(self, other):
        return self.name == other.name
    
    def __str__(self):
        str =  f'{self.name}: \n' 
        for c in self.connections:
            str += f' -> {c.name}\n'

        return str

def spawn_new(path):
    new_path = path.copy()
    return new_path

def walk(paths, current_path, current_cave, limit):
    # can never return to the starting cave
    if current_cave.name == 'start' and len(current_path) > 0:
        return

    # if it's already in the path we can't go back
    if current_cave.is_small() and limit(current_cave.name, current_path):
        return

    current_path.append(current_cave.name)

    if current_cave.is_end():
        paths.append(current_path)
        return

    for c in current_cave.connections:
        # otherwise, keep going
        branch = spawn_new(current_path)
        walk(paths, branch, c, limit)
        
def part_1_limit(name, path):
    return name in path
    
def part_2_limit(name, path):
    small_caves = [p for p in path if p.islower()]

    return name in path and len(set(small_caves)) < len(small_caves)
        
def part_1(caves):
    start = [c for c in caves if c.name == 'start'][0]
    paths = []
    walk(paths,[], start, part_1_limit)
    print(len(paths))
        
def part_2(caves):
    start = [c for c in caves if c.name == 'start'][0]
    paths = []
    walk(paths,[], start, part_2_limit)
    print(len(paths))


if __name__ == '__main__':
    caves = []
    with open('input.txt','r') as f:
        for line in f.readlines():
            a,b = line.strip().split("-")
            ca = Cave(a)
            cb = Cave(b)
            
            if cb in caves:
                cb = caves[caves.index(cb)]
            else:
                caves.append(cb)

            if ca in caves:
                ca = caves[caves.index(ca)]
            else:
                caves.append(ca)
            
            ca.add_connection(cb)
            cb.add_connection(ca)

    # part_1(caves)
    part_2(caves)
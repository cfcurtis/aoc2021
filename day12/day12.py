

class Cave:
    def __init__(self,name):
        self.name = name
        self.connections = []
        self.visited = 0
    
    def visit_limit(self):
        return self.visited > 0 and self.is_small
    
    def is_small(self):
        return self.name.islower() and not self.is_end()
    
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
    for c in new_path:
        if c.name != 'start':
            c.visited = 0
    
    return new_path

def walk(paths, current_path):
    for c in current_path[-1].connections:
        new_path = spawn_new(current_path)

        # stop if we've reached the visit limit in a single path
        if c.visit_limit():
            paths.append(current_path)
            current_path = new_path
            continue

        # if we've reached the last node, add self first
        current_path.append(c)
        c.visited += 1

        if c.is_end():
            paths.append(current_path)
            current_path = new_path
            continue
        
        # otherwise, keep going
        walk(paths, current_path)
        
def part_1(caves):
    start = [c for c in caves if c.name == 'start'][0]
    start.visited += 1
    paths = [[start]]
    current_path = paths[0]
    walk(paths,current_path)
    valid_paths = [path for path in paths if path[-1].name == 'end']
    for path in paths:
        print([c.name for c in path])

if __name__ == '__main__':
    caves = []
    with open('example.txt','r') as f:
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
    
    part_1(caves)
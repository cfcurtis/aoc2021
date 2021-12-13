import copy

class Cave:
    def __init__(self,name):
        self.name = name
        self.connections = []
        self.visited = 0
    
    def visit_limit(self):
        return self.visited > 0 and self.is_small()
    
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
    new_path = copy.deepcopy(path)
    return new_path

def walk(paths, current):
    current_path = paths[-1]

    # if we can't visit the cave, return before adding
    if current.is_small() and any([current.name in c.name for c in current_path]):
        del paths[-1]
        return

    current.visited += 1
    current_path.append(current)

    if current.is_end():
        return

    for c in current.connections:
        # otherwise, keep going
        walk(paths, c)
        branch = spawn_new(current_path)
        paths.append(branch)
        
def part_1(caves):
    start = [c for c in caves if c.name == 'start'][0]
    paths = [[]]
    walk(paths,start)
    valid_paths = [path for path in paths if path[-1].name == 'end']
    print(len(valid_paths))
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
    
    part_1(caves)
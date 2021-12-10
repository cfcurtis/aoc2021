points_table = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

completion_points = {
    '(': 1,
    '[': 2,
    '{': 3,
    '<': 4
}

open_chars = ['(','[','{','<']
close_chars = [')',']','}','>']

def read_input(filename) -> list:
    with open(filename,'r') as f:
        return f.readlines()

def get_first_corrupted(line):
    buf = []
    for char in line:
        if char in open_chars:
            buf.append(char)
        if char in close_chars:
            opening = open_chars[close_chars.index(char)]
            if buf.pop() != opening:
                return points_table[char], buf
    
    return 0, buf

def part_1(code):
    error_score = 0
    for line in code:
        score, _ = get_first_corrupted(line)
        error_score += score
    
    print(error_score)

def part_2(code):
    line_scores = []
    for line in code:
        line_score = 0
        score, buf = get_first_corrupted(line)
        if score == 0:
            for char in reversed(buf):
                line_score *= 5 
                line_score += completion_points[char]
        
            line_scores.append(line_score)
    
    line_scores.sort(reverse=True)
    print(line_scores[(len(line_scores) - 1) // 2])

if __name__ == "__main__":
    code = read_input("input.txt")
    part_1(code)
    part_2(code)
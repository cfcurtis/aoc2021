num_map = {
    0: 'abcefg', # 6
    1: 'cf',     # 2
    2: 'acdeg',  # 5
    3: 'acdfg',  # 5
    4: 'bcdf',   # 4
    5: 'abdfg',  # 5
    6: 'abdefg', # 6
    7: 'acf',    # 3
    8: 'abcdefg',# 7
    9: 'abcdfg'  # 6
}

digit_map = {digit: num for num, digit in num_map.items()}

def print_grid():
    print('num  a  b  c  d  e  f  g')
    for key, value in num_map.items():
        row = f'  {key}  '
        for letter in 'abcdefg':
            row += f'{letter}  ' if letter in value else '   '
        print(row)

unique_nums = {1: 2, 4:4, 7:3, 8:7}
unique_lengths = {length: num for num, length in unique_nums.items()}

def read_input(filename):
    signals = []
    outputs = []
    with open(filename,'r') as f:
        for line in f:
            toks = line.split('|')
            signals.append(toks[0].split())
            outputs.append(toks[1].split())

    return signals, outputs

def signal_including(signal, to_include):
    return [sig for sig in signal if all([l in sig for l in to_include])]

def signal_minus(signal, to_remove):
    new_sig = signal
    for letter in to_remove:
        new_sig = new_sig.replace(letter,'')
    return new_sig

def re_map(signals):
    letter_map = {letter: None for letter in 'abcdefg'}
    known = {num: None for num in unique_nums.keys()}
    unknown = {num: [] for num in range(8) if num not in unique_lengths.keys()}
    for signal in signals:
        length = len(signal)
        if length in unique_nums.values():
            known[unique_lengths[length]] = signal
        else:
            unknown[length] += [signal]
    
    # a is the letter that's not in both 1 and 7
    a = [l for l in known[7] if l not in known[1]][0]
    letter_map[a] = 'a'

    # b and d are the ones in 4 but not 1 and 7
    bd = [l for l in known[4] if l not in known[7]]

    # 5 is the one with 5 letters including b and d
    known[5] = signal_including(unknown[5], bd)[0]
    unknown[5].remove(known[5])

    # 3 is the one including acf (7)
    known[3] = signal_including(unknown[5], known[7])[0]
    unknown[5].remove(known[3])
    
    # this also distinguishes b from d and gives us g
    dg = signal_minus(known[3],known[7])
    g = [l for l in dg if l not in bd][0]
    d = [l for l in dg if l in bd][0]
    b = [l for l in bd if l not in dg][0]

    letter_map[g] = 'g'
    letter_map[b] = 'b'
    letter_map[d] = 'd'

    # 2 is the one left over
    known[2] = unknown[5][0]
    del unknown[5]

    # and also gives us c, f, and e
    cf = signal_minus(known[7], a)
    ce = signal_minus(known[2], a + d + g)
    
    c = [l for l in cf if l in ce][0]
    f = signal_minus(cf, c)
    e = signal_minus(ce, c)

    letter_map[c] = 'c'
    letter_map[f] = 'f'
    letter_map[e] = 'e'

    # now we can translate the rest of them
    for signal in unknown[6]:
        translated = "".join(sorted([letter_map[k] for k in signal]))
        known[digit_map[translated]] = signal

    # return the inverted map
    return {"".join(sorted(value)): key for key, value in known.items()}

def part_1(outputs):
    num_unique = 0
    for output in outputs:
        for digit in output:
            if len(digit) in unique_nums.values():
                num_unique += 1

    print(num_unique)

def part_2(signals, outputs):
    total_outputs = 0
    for signal, output in zip(signals, outputs):
        new_map = re_map(signal)
        displayed = int("".join([str(new_map["".join(sorted(digit))]) for digit in output]))
        total_outputs += displayed

    print(f'Sum of outputs: {total_outputs}')

if __name__ == "__main__":
    signals, outputs = read_input("input.txt")
    part_1(outputs)
    part_2(signals, outputs)
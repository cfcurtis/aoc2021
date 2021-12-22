with open('example.txt','r') as f:
    raw_seqences = f.readlines()

raw_seqences = ['D2FE28']

bin_sequences = []
for seq in raw_seqences:
    bin_sequences.append(''.join([format(int(c,16),'04b') for c in seq]))

print(bin_sequences[0])

for seq in bin_sequences:
    version = int(seq[:3],base=2)
    type_id = int(seq[3:6],base=2)

    if type_id == 4:
        num_bin = ''
        i = 6
        countdown = 2
        while seq[i] == '1':
            num_bin += seq[i+1:i+5]
            i += 5
        
        # one more
        num_bin += seq[i+1:i+5]
    
    else:
        length_type_id = int(seq[6],base=2)
        if length_type_id == 0:
            subpacket_length = int(seq[7:22],base=2)
            subpackets = seq[22:22+subpacket_length]
            # and now, recurse
        
        if length_type_id == 1:
            n_subpackets = int(seq[7:18],base=2)


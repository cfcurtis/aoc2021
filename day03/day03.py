with open('input.txt','r') as f:
    readings = f.readlines()

readings = [r.strip() for r in readings]
n_bits = len(readings[0])
n_readings = len(readings)
sum_bits = [0]*n_bits
for r in readings:
    sum_bits = [sum_bits[b] + int(r[b]) for b in range(n_bits)]

gamma_bin = "".join([str(int(b > n_readings / 2)) for b in sum_bits])
epsilon_bin = "".join([str(int(b < n_readings / 2)) for b in sum_bits])
gamma_dec = int(gamma_bin,2)
epsilon_dec = int(epsilon_bin,2)
print(gamma_dec * epsilon_dec)

## part 2: filtering down
O2_gen = readings.copy()
scrubber = readings.copy()
b = 0
while len(O2_gen) > 1:
    most_common = str(int(sum([int(gen[b]) for gen in O2_gen]) >= len(O2_gen) / 2))
    O2_gen = [gen for gen in O2_gen if gen[b] == most_common]
    b += 1

b = 0
while len(scrubber) > 1:
    least_common = str(int(sum([int(scrub[b]) for scrub in scrubber]) < len(scrubber) / 2))
    scrubber = [scrub for scrub in scrubber if scrub[b] == least_common]
    b += 1

print("Part 2: ", int(scrubber[0],2) * int(O2_gen[0],2))

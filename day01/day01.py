prev = None
increasing = 0
nums = []

with open("depths.txt") as f:
    for line in f:
        reading = int(line)
        if prev is not None and reading > prev:
            increasing += 1
        prev = reading
        nums.append(reading)

print(f'Part one: {increasing}')
prev = None
increasing = 0

for i in range(len(nums) - 2):
    win = sum(nums[i:i + 3])

    if prev is not None and win > prev:
        increasing += 1
    
    prev = win

print(f'Part two: {increasing}')


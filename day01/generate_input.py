import random

depth = random.randint(100,500)
max_increase = random.randint(5,10)
max_decrease = random.randint(1,5)
percent_changing = random.random()*0.1 + 0.5

with open("depths.txt","w") as f:
    for i in range(2000):
        f.write(str(int(depth)) + "\n")
        if random.random() < percent_changing:
            depth = depth + max_increase * random.random()
        else:
            depth = depth - max_decrease * random.random()

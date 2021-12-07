def read_input():
    with open("input.txt",'r') as f:
        return [int(num) for num in f.readline().split(',')]

class LanternFish:
    state = 0
    def __init__(self, init_state):
        self.state = init_state
    
    def countdown(self):
        self.state -= 1
        if self.state == -1:
            self.state = 6
            return LanternFish(8)
        
        return None

def part_1(states,days):
    fishes = []
    for state in states:
        fishes.append(LanternFish(state))

    for day in range(days):
        new_fishes = []
        for fish in fishes:
            new_fish = fish.countdown()
            if new_fish is not None:
                new_fishes.append(new_fish)
        
        fishes = fishes + new_fishes
    
    print(len(fishes))

def part_2(states, days):
    fishes = [0] * 9
    for num in range(min(states),max(states) + 1):
        fishes[num] = states.count(num)

    for day in range(days):
        doubling = fishes[0]

        for n in range(8):
            fishes[n] = fishes[n + 1]
        
        fishes[8] = doubling
        fishes[6] = fishes[6] + doubling

    print(sum(fishes))



if __name__ == "__main__":
    states = [3,4,3,1,2]
    states = read_input()
    # part_1(states, 80)
    part_2(states, 256)
    
def read_input():
    with open("input.txt","r") as f:
        return [int(num) for num in f.readline().split(",")]

def fuel_cost_part_1(p1, p2):
    return abs(p1 - p2)

def fuel_cost_part_2(p1, p2):
    dist = abs(p1 - p2)
    return dist * (dist + 1) / 2

def find_min_fuel(crab_pos, fuel_fun):
    positions = list(range(min(crab_pos), max(crab_pos) + 1))
    min_fuel = sum([fuel_fun(crab, 0) for crab in crab_pos])
    
    for pos in positions:
        fuel = sum([fuel_fun(crab, pos) for crab in crab_pos])
        if fuel < min_fuel:
            min_fuel = fuel

    print(min_fuel)

if __name__ == "__main__":
    # crab_pos = [16,1,2,0,4,2,7,1,2,14]
    crab_pos = read_input()
    find_min_fuel(crab_pos, fuel_cost_part_1)
    find_min_fuel(crab_pos, fuel_cost_part_2)


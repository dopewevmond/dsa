# consider a car that can go a maximum distance of Lkm with a full tank before needing a refuel
# the car wants to move from A to B and there are gas stations along the way
# Consider the car moving from a source point A to a destination point B, with n gas stations
# at distances x1 < x2 < x3 < xn in kilometers from A along the path from A to B

# QUESTION: calculate the minimum number of refills to get from A to B, besides refill at A

# greedy choice is to refill at the farthest gas station from A less than L, denoted G
# then make G the new A and repeat
def fuel(distance, tank, stops):
    last_successful_refill = 0
    current_refill = 0
    num_refills = 0
    num_stops = len(stops)
    stops = [0, *stops, distance]

    while current_refill <= num_stops:
        while (current_refill <= num_stops) and (stops[current_refill+1] - stops[last_successful_refill] <= tank):
            current_refill += 1
        if current_refill == last_successful_refill:
            return -1
        if current_refill <= num_stops:
            num_refills += 1
        last_successful_refill = current_refill
    return num_refills  

print(fuel(950, 400, 4, [200, 375, 550, 750])) #prints 2
print(fuel(10, 3, 4, [1, 2, 5, 9])) #prints -1 since it is impossible
print(fuel(200, 250, 2, [100, 150])) #prints 1 
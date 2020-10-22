
import math;

num_elves = 3005290;

elves = [i+1 for i in range(num_elves)];

while len(elves) > 1:
    half_length = math.floor(len(elves) / 2);
    if (len(elves) % 2) == 0:
        elves = elves[0:half_length] + elves[(half_length+2)::3];
        next_elf = half_length - math.floor(half_length / 3) + 1;
        elves = elves[(next_elf-1):] + elves[:(next_elf-1)];
    else:
        elves = elves[0:half_length] + elves[(half_length+1)::3];
        next_elf = half_length - math.floor((half_length - 1) / 3) + 1;
        elves = elves[(next_elf-1):] + elves[:(next_elf-1)];

print(elves[0]);


# 4 - no-one in second half survives
# 6 - 6 survives, next up is at 3
# 8 - 7 survives, next up is at 4
# 10 - 8 survives, next up is at 5
# 12 - 9, 12 survive, next up is at 5
# 14 - 10, 13 survive, next up is at 6
# 16 - 11, 14 survive, next up is at 7
# 18 - 12, 15, 18 survive, next up is at 7
# elves[0:half_length] + elves[(half_length+2)::3]
# next up - half_length (at index half_length - 1)

# 3 - 3 survives, next up is at 2
# 5 - 4 survives, next up is at 3
# 7 - 5 survives, next up is at 4
# 9 - 6, 9 survive, next up is at 4
# 11 - 7, 10 survive, next up is at 5
# elves[0:half_length] + elves[(half_length+1)::3]
# next up - half_length (at index half_length - 1)
    
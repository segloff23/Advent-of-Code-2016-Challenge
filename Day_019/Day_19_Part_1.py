


num_elves = 3005290;

elves = [i+1 for i in range(num_elves)];

offset = 0;
while len(elves) > 1:
    if (len(elves) % 2) == 0:
        new_offset = offset;
    else:
        new_offset = (offset + 1) % 2;
    elves = elves[offset::2];
    offset = new_offset;

print(elves[0]);

with open('Day_20_Input.txt') as file:
    blockages = [line.strip().split('-') for line in file];  
for block in blockages:
    block[0] = int(block[0]);
    block[1] = int(block[1]);
blockages.sort(key = lambda x: x[0]) 

if blockages[0][0] > 0:
    min_IP = 0;
else:
    max_block = blockages[0][1];
    for i in range(1, len(blockages)):
        if blockages[i][0] <= (max_block + 1):
            max_block = max([max_block, blockages[i][1]]);
        else:
            min_IP = max_block + 1;
            break;

print('\nPart 1:');
print('Lowest IP: ', min_IP);
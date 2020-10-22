
def calc_checksum(data):
    checksum = [];
    for i in range(0, len(data)-1, 2):
        if data[i] == data[i+1]:
            checksum.append(1);
        else:
            checksum.append(0);
    if (len(checksum) % 2) == 0:
        checksum = calc_checksum(checksum.copy());
    return checksum;

puzzle_input = '11100010111110100';

fill_length = 272;
data = [];
for i in puzzle_input:
    data.append(int(i));
    
while len(data) < fill_length:
    data.append(0);
    for i in range(len(data)-2, -1, -1):
        data.append(1 - data[i])
        if len(data) >= fill_length:
            break;
checksum = calc_checksum(data);

print('\nPart 1:');
for i in checksum:
    print(i, end = '');
print();

fill_length = 35651584;
data = [];
for i in puzzle_input:
    data.append(int(i));
    
while len(data) < fill_length:
    data.append(0);
    for i in range(len(data)-2, -1, -1):
        data.append(1 - data[i])
        if len(data) >= fill_length:
            break;
checksum = calc_checksum(data);

print('\nPart 2:');
for i in checksum:
    print(i, end = '');
print();
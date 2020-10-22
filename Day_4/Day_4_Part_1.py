
import re;
import numpy as np;

with open('Day_4_Input.txt') as file:
    room_code_data = [re.findall('[a-z]+|\d+', line) for line in file];

sector_ID_sum = 0;
for room_code in room_code_data:
    name = room_code[:-2];
    sector_ID = int(room_code[-2]);
    checksum = room_code[-1];
    
    freq_list = np.zeros((26,));
    for word in name:
        for letter in word:
            freq_list[ord(letter) - ord('a')] += 1;
    
    valid = 1;
    for i in range(5):
        s = np.argmax(freq_list);
        if (ord(checksum[i]) - ord('a')) != s:
            valid = 0;
            break;
        freq_list[s] = 0;

    if valid:
        sector_ID_sum += sector_ID;

print('\nPart 1:');
print('Sector ID Sum: ', sector_ID_sum);
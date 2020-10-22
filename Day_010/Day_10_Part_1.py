
import re;

with open('Day_10_Input.txt') as file:
    instructions = [re.findall('value|bot|output|low|high|\d+', line.strip()) for line in file];
    
values = {};
transfers = {};
outputs = {};

for line in instructions:
    if line[0] == 'value':
        if int(line[3]) not in values:
            values[int(line[3])] = [int(line[1])];
        else:
            values[int(line[3])].append(int(line[1]));
    if line[0] == 'bot':
        if int(line[1]) not in transfers:
            transfers[int(line[1])] = [line[2:5], line[5:]];
        else:
            print('Error');
            
chip_search = (17, 61);
bot_search = 0;
key_found = 1;
while key_found:
    value_keys = [key for key in values];
    key_found = 0;
    for key in value_keys:
        chips = values[key];
        if len(chips) == 2:
            if (chip_search[0] in chips) and (chip_search[1] in chips):
                bot_search = key;
            key_found = 1;
            job = transfers[key];
            for step in job:
                if step[0] == 'low':
                    val = min(chips);
                else:
                    val = max(chips);
                if step[1] == 'bot':
                    if int(step[2]) not in values:
                        values[int(step[2])] = [val];
                    else:
                        values[int(step[2])].append(val);
                elif step[1] == 'output':
                    if int(step[2]) not in outputs:
                        outputs[int(step[2])] = [val];
                    else:
                        outputs[int(step[2])].append(val);
            values[key].clear();
value_product = outputs[0][0] * outputs[1][0] * outputs[2][0];

print('\nPart 1:');
print('Bot Number: ', bot_search);
print('\nPart 2:');
print('Value Product: ', value_product)












from re import findall;
from itertools import permutations;

def swap(string, a, b, option):
    if option == 'position':
        letter_a = string[int(a)];
        string[int(a)] = string[int(b)];
        string[int(b)] = letter_a;
    elif option == 'letter':
        index_a = string.index(a[1]);
        index_b = string.index(b[1]);
        string[index_a] = b[1];
        string[index_b] = a[1];
    else:
        print('Swap Error');
    return string;

def rotate_RL(string, direction, steps):
    if direction == 'right':
        for i in range(steps):
            string = [string[-1]] + string[0:-1:1]
    elif direction == 'left':
        for i in range(steps):
            string = string[1:] + [string[0]];
    else:
        print('Rotate Error');
    return string;

def rotate_X(string, letter):
    
    index_letter = string.index(letter[1]);
    if index_letter >= 4:
        string = rotate_RL(string, 'right', index_letter + 2);
    else:
        string = rotate_RL(string, 'right', index_letter + 1);
    return string;

def reverse(string, start, end):
    if start >= end:
        print('Reverse Error');
    else:
        string = string[0:start] + string[end:start:-1] + [string[start]] + string[(end+1):];
    return string;

def move(string, initial, final):
    if initial < final:
        string = string[0:initial] + string[(initial+1):(final+1)] + [string[initial]] + string[(final+1):]; 
    elif initial > final:
        string = string[0:final] + [string[initial]] + string[final:initial] + string[(initial+1):];
    return string;

with open('Day_21_Input.txt') as file:
    pattern = 'swap|position|letter|rotate|left|right|reverse|move|\d+| [a-z] ';
    instructions = [findall(pattern, line.strip() + ' ') for line in file];
    
want = 'fbgdceah';

potential_passwords = list(permutations(list('abcdefgh'))) 
for password in potential_passwords:
    string = list(password);
    for line in instructions:
        if line[0] == 'swap':
            string = swap(string, line[2], line[4], line[1]);
        elif line[0] == 'rotate':
            if line[1] == 'position':
                string = rotate_X(string, line[3]);
            else:
                string = rotate_RL(string, line[1], int(line[2]));
        elif line[0] == 'move':
            string = move(string, int(line[2]), int(line[4]));
        elif line[0] == 'reverse':
            string = reverse(string, int(line[2]), int(line[3]));
    
    if ''.join(string) == want:
        break;

print('\nPart 2:');
print('Password: ', ''.join(password));












    

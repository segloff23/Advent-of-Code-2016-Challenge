
import re;

def look_for_abba(word):
    
    found = 0;
    for letter in range(1, len(word)-2):
        if word[letter] == word[letter+1]:
            if word[letter-1] == word[letter+2]:
                if word[letter] != word[letter-1]:
                    found = 1;
    return found;


with open('Day_7_Input.txt') as file:
    IP_list = [re.findall('[a-z]+|\[[a-z]+\]', line.strip()) for line in file];
    
abba_IP_count = 0;
for IP in IP_list:
    abba_found = 0;
    for word in IP:
        if word[0] != '[':
            if look_for_abba(word):
                abba_found = 1;
        else:
            if look_for_abba(word):
                abba_found = 0;
                break;
    if abba_found:
        abba_IP_count += 1;

print('\nPart 1:');
print('ABBA IP Count: ', abba_IP_count);

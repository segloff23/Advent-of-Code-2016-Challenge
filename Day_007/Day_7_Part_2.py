
import re;

def look_for_aba(word):
    
    aba_set = [];
    for letter in range(1, len(word)-1):
        if word[letter-1] == word[letter+1]:
                if word[letter] != word[letter-1]:
                    aba_set.append(word[(letter-1):(letter+2)]);
    return aba_set;

def look_for_bab(word, aba):
    bab = aba[1] + aba[0] + aba[1];
    if re.search(bab, word):
        bab_found = 1;
    else:
        bab_found = 0;

    return bab_found;

with open('Day_7_Input.txt') as file:
    IP_list = [re.findall('[a-z]+|\[[a-z]+\]', line.strip()) for line in file];
    
ssl_IP_count = 0;
for IP in IP_list:
    aba_set = [];
    ssl_found = 0;
    for word in IP:
        if word[0] != '[':
            aba_set += look_for_aba(word);
    for word in IP:
        if word[0] == '[':
            for aba in aba_set:
                if look_for_bab(word, aba):
                    ssl_found = 1;
    if ssl_found:
        ssl_IP_count += 1;
                
print('\nPart 2:');
print('SSL IP Count: ', ssl_IP_count);

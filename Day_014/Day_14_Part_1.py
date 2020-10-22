

import hashlib;

def find_repeats(word, count):
    key = '';
    for i in range(len(word)-count+1):
        match_found = 1;
        for j in range(count):
            if word[i] != word[i+j]:
                match_found = 0;
                break;
        if match_found:
            key = word[i];
            break;
    return match_found, key;

salt = 'abc'; #ihaygndm';

integer_index = -1;
hashes_found = 0;
while hashes_found < 64:
    
    match_found = 0;
    while not match_found:
        integer_index += 1;
        message = salt + str(integer_index);
        word = hashlib.md5(message.encode()).hexdigest()
        match_found, key = find_repeats(word, 3);

    for i in range(1, 1001):
        message = salt + str(integer_index + i);
        new_word = hashlib.md5(message.encode()).hexdigest()
        match_found, new_key = find_repeats(new_word, 5);
        if key == new_key:
            hashes_found += 1;
            print(integer_index);
            break;
    
print('\nPart 1:');
print('Final Index: ', integer_index);
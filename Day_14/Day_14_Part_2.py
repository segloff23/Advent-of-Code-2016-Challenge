

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

def get_stretched_hash(message, repeats):
    
    word = hashlib.md5(message.encode()).hexdigest();
    for i in range(repeats):
        word = hashlib.md5(word.encode()).hexdigest();
    return word;

salt = 'ihaygndm';
repeats = 2016;

hash_list = [];
for i in range(0, 1001):
    message = salt + str(i);
    word = get_stretched_hash(message, repeats);
    hash_list.append(word);
    
integer_index = -1;
hashes_found = 0;
while hashes_found < 64:
    
    match_found = 0;
    while not match_found:
        integer_index += 1;
        word = hash_list[0];
        match_found, key = find_repeats(word, 3);
        if not match_found:
            message = salt + str(integer_index + 1001);
            word = get_stretched_hash(message, repeats);
            hash_list.pop(0);
            hash_list.append(word);
    for i in range(1, 1001):
        new_word = hash_list[i];
        match_found, new_key = find_repeats(new_word, 5);
        if key == new_key:
            hashes_found += 1;
            break;
    message = salt + str(integer_index + 1001);
    word = get_stretched_hash(message, repeats);
    hash_list.pop(0);
    hash_list.append(word);


print('\nPart 2:');
print('Final Index: ', integer_index);













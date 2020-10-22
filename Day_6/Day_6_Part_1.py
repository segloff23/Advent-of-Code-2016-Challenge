
with open('Day_6_Input.txt') as file:
    word_list = [line.strip() for line in file];

letter_count = len(word_list[0]);

message = '';
decoded_message = '';
for letter in range(letter_count):
    
    freq_list = [0 for i in range(26)];
    for word in word_list:
        freq_list[ord(word[letter]) - ord('a')] += 1;
    message += chr(freq_list.index(max(freq_list)) + ord('a'));
    decoded_message += chr(freq_list.index(min(freq_list)) + ord('a'));

print('\nPart 1:');
print('Message: ', message);
print('\nPart 2:');
print('Decoded Message: ', decoded_message);
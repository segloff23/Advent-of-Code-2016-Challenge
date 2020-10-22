

def get_string_length(text):
    
    length = 0;
    i = 0;
    while i < len(text):
        if text[i] == '(':
            j = i + 1;
            char_range_as_string = '';
            while text[j] != 'x':
                char_range_as_string += text[j];
                j += 1;
            char_range = int(char_range_as_string);
            j += 1;
            repetition_as_string = '';
            while text[j] != ')':
                repetition_as_string += text[j];
                j += 1;
            repetition = int(repetition_as_string);
            new_text = text[(j+1):(j+1+char_range)];
            length += get_string_length(new_text) * repetition;
            i = j + char_range + 1;
        else:
            length += 1;
            i += 1;
    return length;

with open('Day_9_Input.txt') as file:
    text = file.readline().strip();
    
text_length = get_string_length(text);   
print('\nPart 2:');
print('Decompressed Length: ', text_length);















with open('Day_9_Input.txt') as file:
    file_data = [line.strip() for line in file];


#file_data = ['X(10x2)(3x3)ABCYZA'];
decompressed_data = '';
for line in file_data:
    new_line = '';
    i = 0;
    while i < len(line):
        if line[i] == '(':
            char_range_as_string = line[i+1];
            j = i + 2;
            while line[j] != 'x':
                char_range_as_string += line[j]
                j += 1;
            j += 1;
            repetition_as_string = line[j];
            j += 1;
            while line[j] != ')':
                repetition_as_string += line[j];
                j += 1;
            char_range = int(char_range_as_string);
            repetition = int(repetition_as_string);
            base_string = line[(j+1):(j+1+char_range)];
            string = '';
            for k in range(repetition):
                string += base_string;
            new_line += string;
            i = j + char_range + 1;

        else:
            new_line += line[i];
            i += 1;
            
    decompressed_data += new_line;

print('\nPart 1:');
print('Decompressed Length: ', len(decompressed_data));





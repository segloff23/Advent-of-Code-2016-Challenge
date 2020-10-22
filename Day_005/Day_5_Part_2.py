
import hashlib;

door_ID = 'ojvtpuvg';

code = [-1 for i in range(8)];
integer_index = 0;
code_found = 0;
while code_found < 8:
    message = door_ID + str(integer_index);
    result = hashlib.md5(message.encode()).hexdigest()
    
    if result[0:5] == '00000':
        if result[5].isnumeric():
            index = int(result[5]);
            if index < 8:
                if code[index] == -1:
                    code[index] = result[6];
                    code_found += 1;
    integer_index += 1;
    
print('\nPart 2:');
print('Password: ', end = '');
for i in range(8):
    print(code[i], end = '');
print();
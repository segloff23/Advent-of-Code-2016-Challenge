
import hashlib;

door_ID = 'ojvtpuvg';

code = [-1 for i in range(8)];
integer_index = 0;
code_index = 0;
while code_index < 8:
    message = door_ID + str(integer_index);
    result = hashlib.md5(message.encode()).hexdigest()
    
    if result[0:5] == '00000':
        code[code_index] = result[5];
        code_index += 1;
    
    integer_index += 1;
    
print('\nPart 1:');
print('Password: ', end = '');
for i in range(8):
    print(code[i], end = '');
print();
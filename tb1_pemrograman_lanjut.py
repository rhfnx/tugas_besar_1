'''
Nama: Naufal Rahfi Anugerah
NIM: 41822010038
'''

import re

first_input = input().rstrip().split()
n = int(first_input[0])
m = int(first_input[1])

matrix = []
for _ in range(n):
    matrix_items = input()
    matrix.append(matrix_items)

decode_msg = ""
for i in range(m):
    for j in range(n):
        try:
            decode_msg += matrix[j][i]
        except IndexError:
            pass

pattern = r'(?<=[\w])[^\w]+(?=[\w])'
match_msg = re.findall(pattern, decode_msg)

for x in match_msg:
    decode_msg = decode_msg.replace(x, ' ', 1)
print(decode_msg)
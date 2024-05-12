'''
Nama: Naufal Rahfi Anugerah
NIM: 41822010038
'''

import re

def get_input_matrix():
    n, m = map(int, input().rstrip().split())
    matrix = [input() for _ in range(n)]
    return matrix, m

def decode_message(matrix, m):
    decode_msg = ""
    for i in range(m):
        for j in range(len(matrix)):
            try:
                decode_msg += matrix[j][i]
            except IndexError:
                pass
    return decode_msg

def clean_message(decode_msg):
    pattern = r'(?<=[\w])[^\w]+(?=[\w])'
    match_msg = re.findall(pattern, decode_msg)
    for x in match_msg:
        decode_msg = decode_msg.replace(x, ' ', 1)
    return decode_msg

def main():
    matrix, m = get_input_matrix()
    decoded_message = decode_message(matrix, m)
    cleaned_message = clean_message(decoded_message)
    print(cleaned_message)

if __name__ == "__main__":
    main()

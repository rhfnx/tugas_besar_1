'''
Nama: Naufal Rahfi Anugerah
NIM: 41822010038
'''

import re

def get_input_matrix(filename):
  try:
    with open(filename, 'r') as f:
      n, m = map(int, f.readline().rstrip().split())
      matrix = [line.rstrip() for line in f]
    return matrix, m
  except FileNotFoundError:
    print(f"Error: File '{filename}' not found.")
    exit()

def decode_message(matrix, m):
  decode_msg = ""
  for i in range(m):
    for j in range(len(matrix)):
      try:
        decode_msg += matrix[j][i]
      except IndexError:
        decode_msg += ' '
  return decode_msg

def clean_message(decode_msg):
  pattern = r'(?<=[\w])[^\w]+(?=[\w])'
  match_msg = re.findall(pattern, decode_msg)
  for x in match_msg:
    decode_msg = decode_msg.replace(x, ' ', 1)
  return decode_msg


filename = 'text.txt'
try:
    matrix, m = get_input_matrix(filename)
    decoded_message = decode_message(matrix, m)
    cleaned_message = clean_message((decoded_message))

    resultfile = open("result.txt","w")

    resultfile.write(cleaned_message)
    resultfile.close()

    print(f"Decoded Message:\n{cleaned_message}\nThe result is writen in result.txt!")
except Exception as e:
    print(f"An error occurred: {e}")

import sys

s = 'Hello'
b = bytes([201, 65, 127, 0,200])

sys.stdout.buffer.write(b)
#sys.stdout.write(b)
#print(s, end='') 
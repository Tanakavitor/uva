import struct
import sys

def rev(n):
    little_endian = struct.pack('<i', n)
    big_endian = struct.unpack('>i', little_endian)[0]
    return big_endian

for line in sys.stdin:
    n = int(line)
    print(f'{n} converts to {rev(n)}')
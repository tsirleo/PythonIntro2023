import io
import zipfile
import sys

volume = number = 0
for item in zipfile.ZipFile(io.BytesIO(bytearray.fromhex(sys.stdin.read())), 'r').infolist():
    if item.is_dir():
        continue
    else:
        number += 1
        volume += item.file_size
print(number, volume)

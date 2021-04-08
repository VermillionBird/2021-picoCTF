import sys

with open(sys.argv[1], 'rb') as f:
    invite = f.read()[-1000:]

with open(sys.argv[2], 'ab') as f:
    f.write(invite)

with open(sys.argv[3], 'ab') as f:
    f.write(invite)
import sys

newline_char = ['{', ';',]
with open(sys.argv[1], 'r') as old, open(sys.argv[2], 'w') as new:
    for line in old.readlines():
        for char in line:
            if char in newline_char:
                new.write(char)
                new.write('\n')
            elif char == '}':
                new.write(char)
                new.write('\n')
                new.write('\n')
            elif char == ',':
                new.write(' ')
                new.write(char)
            else:
                new.write(char)


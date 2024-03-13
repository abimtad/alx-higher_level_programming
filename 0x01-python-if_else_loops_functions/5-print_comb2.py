#!/usr/bin/python3
for num in range(0, 100):
    if num != 0:
        print(", ", end='')
    print("{:02}{}".format(num, '\n' if num == 99 else ''), end='')
    

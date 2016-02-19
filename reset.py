from serial import Serial
import time


p3_plus_mode=[
('#FXT0;#FXA3;','P3 into NON sticky mode')
]


sp=Serial('/dev/ttyUSB0',38400,timeout=1)
for a in p3_plus_mode:
    cmd=a[0]
    what=a[1]
    print(str.format("Command {:20} ",what),end='')
    rv = sp.write(bytes(cmd,'utf-8'))
    if int(rv) == len(cmd):
       print("\t\t\tOK")
    else:
       print("\t\t\tProblem")
    time.sleep(2)


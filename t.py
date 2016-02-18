from serial import Serial
import time

p3_plus_mode = [('#CTF+0','Centre frequency '),
                ('#FXT0;', 'P3 into Non-sticky mode'),
                ('#SPN000025;', 'P3 2.5Khz mode'),
                ('UP7;', 'K3 VFO-A Up 5Khz'),
                ('#FXT1;', 'P3 into sticky mode'),
                ('DN7', 'K3 VFO-A Down 5 Khz')]

sp = Serial('/dev/tty.usbserial-A7004VW8', 38400, timeout=1)
for a in p3_plus_mode:
    cmd = a[0]
    what = a[1]
    print(str.format("Command {:30} ", what), end='')
    rv = sp.write(bytes(cmd, 'utf-8'))
    if int(rv) == len(cmd):
        print("\t\t\tOK")
    else:
        print("\t\t\tProblem")
    time.sleep(1)

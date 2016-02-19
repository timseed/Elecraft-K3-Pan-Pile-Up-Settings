from serial import Serial
import time

#Note the Mac has 2 devices
#tty.* and a cu.*.
#So, what's the difference?
#Well, TTY devices are for calling into UNIX systems,
#whereas CU (Call-Up) devices are for calling out from them (eg, modems).
#We want to call-out from our Mac, so /dev/cu.* is the correct device to use.
#Note my Logger is using the TTY Interface


p3_plus_mode = [('#FXT0;#FXA0;','P3 reset Tracking Mode'),
                ('#SPN000022;', 'P3 2.2Khz mode'),
                ('UP4;', 'K3 VFO-A DOWN 1 Khz'),
                ('#FXT1;#FXA3;', 'P3 into sticky mode'),
                ('DN4;', 'K3 VFO-A UP 1 Khz')]

sp = Serial('/dev/ttyUSB0', 38400, timeout=1)
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

import pprint

from serial import Serial
import time


class k3_steps(object):

    def __init__(self):
        self.steps = []
        self.k3_hops = [(5000, '7'), (3000, '6'), (2000, '5'), (1000, '4'), (200, '9'),
                        (100, '8'), (50, '3'), (20, '2'), (10, '1'), (1, '0')]

    def bw(self, direction, wanted, cmd=''):
        if cmd == '':
            self.cmd = ''
        if direction not in ['UP', 'DN']:
            print("Error")
            Exception('Bad Direction Code')
        else:
            while wanted > 0:
                MAX_STEP = [x if x[0] <= wanted else tuple([0, '0']) for x in self.k3_hops]
                MAX_STEP.sort(reverse=True)
                MAX_STEP = MAX_STEP[0]
                wanted = wanted - MAX_STEP[0]
                #              print(str.format("Need to move {} Hz",wanted))
                cmd = cmd + str.format('{}{};', direction, MAX_STEP[1])
        return cmd


class k3_p3(object):
    """
    Note the Mac has 2 devices
    tty.* and a cu.*.
    So, what's the difference?
    Well, TTY devices are for calling into UNIX systems,
    whereas CU (Call-Up) devices are for calling out from them (eg, modems).
    We want to call-out from our Mac, so /dev/cu.* is the correct device to use.
    Note my Logger is using the TTY Interface

    """

    p3_plus_mode = [('#FXT0;#FXA0;', 'P3 reset Tracking Mode'),
                    ('#SPN000022;', 'P3 Scope Width mode'),
                    ('UP4;', 'K3 VFO-A Up ....'),
                    ('#FXT1;#FXA3;', 'P3 into sticky mode'),
                    ('DN4;', 'K3 VFO-A Down ...')]

    p3_reset_mode = [('#FXT0;#FXA3;', 'P3 into NON sticky mode')]

    def __init__(self, serial_port='TEST'):
        self._serial = serial_port

    def p3_span(self,
                p3_screen_width=2000,
                p3_offset=250):
        """
        p3_span set the P3 to a cutom width and setting
        :param p3_screen_width: Width in Hz of the P3 Screen
        :param p3_offset: Where the current signal want to be offset from
        :return: Nothing
        """

        steps = k3_steps()
        p3_jump = int((p3_screen_width - p3_offset) / 2)
        UP_CMD = steps.bw('UP', p3_jump)
        DN_CMD = steps.bw('DN', p3_jump)
        if self._serial == "TEST":
            do_nothing = 1
            sp = None
        else:
            sp = Serial(self._serial, 38400, timeout=1)

        for a in range(len(self.p3_plus_mode)):
            cmd = self.p3_plus_mode[a][0]
            what = self.p3_plus_mode[a][1]
            if a == 1:
                span = int((p3_screen_width / 100))
                cmd = str.format("#SPN{num:06d};".format(num=span))
            elif a == 2:
                cmd = UP_CMD
            elif a == 4:
                cmd = DN_CMD
            print(str.format("Command {:30} ", what), end='')
            if self._serial == 'TEST':
                print("%s" % cmd)
                rv = len(cmd)
            else:
                rv = sp.write(bytes(cmd, 'utf-8'))
            if int(rv) == len(cmd):
                print("\t\t\tOK")
            else:
                print("\t\t\tProblem")
            time.sleep(1)

    def p3_reset(self):

        if self._serial == "TEST":
            do_nothing = 1
            sp = None
        else:
            sp = Serial(self._serial, 38400, timeout=1)
        for a in self.p3_reset_mode:
            cmd = a[0]
            what = a[1]
            print(str.format("Command {:20} ", what), end='')
            if self._serial == "TEST":
                do_nothing = True
                rv = len(cmd)
            else:
                rv = sp.write(bytes(cmd, 'utf-8'))
            if int(rv) == len(cmd):
                print("\t\t\tOK")
            else:
                print("\t\t\tProblem")
            time.sleep(1)


if __name__ == "__main__":
    sn007 = k3_p3(serial_port="TEST")
    sn007.p3_span(4000, 250)

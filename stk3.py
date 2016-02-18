__author__ = 'timothyhseed'

from serial import Serial
import time

class stk3(object):

    def __init__(self,port,baud=38400,to=1):
        self.junk=0
        try:
            self.k3port=Serial(port,baud,timeout=to)
        except:
            print("Error Occured Initialising the Serial Port")
            raise

    def send(self,cmd):
        self.pause()
        try:
            print("Sending "+cmd)
            rv=self.k3port.write(cmd.encode('utf-8'))
            print(str.format("Got back {}",rv))
            if int(rv) == len(cmd):
                print("Command sent OK")
            else:
                print("Command {} NOT Ok",cmd)
        except ValueError:
            print("Bad Values Spent")
        except:
            print("Some other error occured when sending to Serial Port")

    def read(self):
        try:
            data_read=self.k3port.read_all()
            return  data_read.decode('utf-8')
        except:
            return "Err Reading"

    def close_port(self):
        if self.k3port is not None:
            self.k3port.close()
            self.k3port= None

    def pause(self):
        time.sleep(1)

if __name__ == "__main__":

    k3_serial=stk3('/dev/tty.usbserial-A7004VW8',38400,1)
    #sp=Serial('/dev/tty.usbserial-A7004VW8',38400,timeout=1)
    k3_serial.send("UP5;\n")
    print(str.format("K3 Output - {} ",k3_serial.read()))
    k3_serial.close_port()

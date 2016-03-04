import guidata
import os
from sys import platform
from guidata.qt.QtGui import QMainWindow, QSplitter
from guidata.configtools import get_icon
#_app = guidata.qapplication() # not required if a QApplication has already been created
from guidata.dataset.datatypes import (DataSet)
from guidata.dataset.dataitems import (ChoiceItem, FloatItem, StringItem, NumericTypeItem, ButtonItem)
from guidata.qthelpers import create_action, add_actions, get_std_icon
from guidata.dataset.qtwidgets import DataSetShowGroupBox, DataSetEditGroupBox
from pprint import pprint
import pickle
from k3 import k3_steps, k3_p3

class Processing(DataSet):

    def __init__(self, *args, **kwargs):
        super(Processing, self).__init__(*args, **kwargs)
        self.loadSettings()

    def __del__(self,*args,**kwargs):
        #super(Processing, self).__del__(*args, **kwargs)
        self.saveSettings()

    def hi(self,calling_obj,c,d):
      #We can access the classes variables when we want ...
      if self.choice=='1':
          self.saveSettings()
          cmd=str.format('\"Offset {} BW {}\"',self.offset,self.bandwidth)
          os.system("echo "+cmd)
          sn007 = k3_p3(serial_port=self.device)
          sn007.p3_span(self.bandwidth,self.offset)
      elif self.choice=='0':
          os.system("echo RESET")
          sn007 = k3_p3(serial_port=self.device)
          sn007.p3_reset()
      elif self.choice =='-1':
          os.system("echo QUIT")

    def guessOS(self):
        if platform.startswith('win'):
           self.device='Windows Device Needed'
        else:
           self.device='/dev/ttyUSB0'

    def saveSettings(self):
      try:
        data = { "device": self.device, "bandwidth": self.bandwidth,"offset":self.offset }
        pickle.dump( data, open( "p3lte.p", "wb" ) )
      except:
        pass

    def loadSettings(self):
      try:
        data = pickle.load( open( "p3lte.p", "rb" ) )
        self.device=data['device']
        self.bandwidth=data['bandwidth']
        self.offset=data['offset']
      except:
        pass

    device    = StringItem("Control Device ", "Device")
    offset    = FloatItem("Offset", default=200, min=0, max=5000, unit=u'Hz', slider=True)
    bandwidth = FloatItem("Bandwidth", default=1500, min=0, max=5000, unit=u'Hz', slider=True)
    choice = ChoiceItem("Action",
                        [('1', "Set P3"), ('0', "RESET"),('-1',"QUIT")])
    processButton = ButtonItem("DO IT", hi).set_pos(col = 0, colspan = 2)

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setWindowIcon(get_icon('python.png'))
        self.setWindowTitle("P3 Ctrl")
        # Instantiate dataset-related widgets:
        self.group1 = DataSetEditGroupBox("Activable dataset",
                                             Processing, comment='')
        self.group1.SIG_APPLY_BUTTON_CLICKED.connect(self.group1._items[0].hi)
        splitter = QSplitter(self)
        splitter.addWidget(self.group1)

        self.setCentralWidget(splitter)
        self.setContentsMargins(10, 5, 10, 5)


if __name__ == '__main2__':
    from guidata.qt.QtGui import QApplication
    import sys
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
else:
  import guidata
  _app = guidata.qapplication() # not required if a QApplication has already been created
  param = Processing()
  param.edit()

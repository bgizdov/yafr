from qt import *
from main import *
import sys

if __name__ == "__main__":
   app = QApplication(sys.argv)
   f = yafr()
   f.loadFolders()
   f.show()   
   app.setMainWidget(f)
   app.exec_loop()

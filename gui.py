import sys
from PyQt4 import QtGui, QtCore

'''
# these lines are enough to open a window but we are going to use a more formal way for creating GUI's i.e using classes

app=QtGui.QApplication(sys.argv)
screen=QtGui.QWidget()   # this is the display screen
screen.setGeometry(50,50,700,500)  # sets the location to [50,50] and width=700 & height=500 , this is not a necessary command
screen.setWindowTitle("My GUI")
screen.show()
sys.exit(app.exec())
'''

class Window(QtGui.QMainWindow):
	
	def __init__(self):
	    super().__init__()
	    self.setGeometry(100,100,800,500)
	    self.setWindowTitle('PyQt GUIs!')
	    self.setWindowIcon(QtGui.QIcon('/home/akshay/Downloads/gui2.png'))
	    self.home()
	    self.show()
	   
	def home(self):
	    btn =QtGui.QPushButton("Quit",self)
	    btn.clicked.connect(QtCore.QCoreApplication.instance().quit)
	    btn.resize(70,40)
	    btn.move(720,450)
	   

if __name__=='__main__':
    app=QtGui.QApplication(sys.argv)
    screen=Window()
    sys.exit(app.exec())

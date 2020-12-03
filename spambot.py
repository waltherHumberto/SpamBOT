
from PyQt5 import QtWidgets, uic
import time
import pyautogui
import sys

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('spaminterface.ui', self)
        self.show()
        self.pushButton.clicked.connect(lambda : self.rodabot()) # Inicia a conexão do botão inicia com o evento 

    def rodabot(self):
        # while(PyQt5.QKeyEvent() != ESC):
            time.sleep(3) # tempo de espera para o usuario clicar na caixa de mensagem
            f = self.lineEdit.text() 
            print(f)
            # while(True)
            for word in f :
                print("To mandando essa merda")
                pyautogui.typewrite(word)
                pyautogui.press('enter')


app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()


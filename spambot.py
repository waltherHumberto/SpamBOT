
from PyQt5 import QtWidgets, uic
import time
import pyautogui
import keyboard
import sys

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('spaminterface.ui', self)
        self.show()
        self.teladousuario.clear()
        self.teladousuario.append("Clique no botão iniciar para começar a spamar") 
        self.teladousuario.append("Você tem 4 segundos para clicar no local desejado") 
        self.pushButton.clicked.connect(lambda: self.rodabot()) # Inicia a conexão do botão inicia com o evento 

    def rodabot(self):
        print("entrou na funçao")
        
    
        time.sleep(4) # tempo de espera para o usuario clicar na caixa de mensagem
        while(not keyboard.is_pressed('ESC')):
            with  open("texto.txt","r") as f:
                
                for word in f :
                    self.teladousuario.append("To mandando essa merda")
                    print(word)
                    pyautogui.typewrite(word)
                    pyautogui.press('enter')
        self.teladousuario.append("parei de mandar ")
        return 
        
    def sair():
        quit()
    
app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()


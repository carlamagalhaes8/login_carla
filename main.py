from PyQt5 import uic, QtWidgets

app = QtWidgets.QApplication([])
janela = uic.loadUi("menu.ui")
tela_certo = uic.loadUi("deu_certo.ui")
tela_errado = uic.loadUi("deu_errado.ui")

def mudanca_tela():
    nome = janela.resp_nome.text()
    senha = janela.resp_senha.text()
   
    if nome == "carla" and senha == "1234":
        tela_certo.show()
        janela.close()
       
    else:
        tela_errado.show()
        janela.close()

janela.cadastrar.clicked.connect(mudanca_tela)

janela.show()
app.exec()
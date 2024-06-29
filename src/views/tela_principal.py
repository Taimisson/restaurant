from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget
import sys

from models.restaurante import Restaurante
from views.tela_cardapio import TelaCardapio
from views.tela_pedido import TelaPedido
from views.tela_cozinha import TelaCozinha
from views.tela_relatorio import TelaRelatorio

class TelaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sistema de Gerenciamento de Pedidos")
        self.restaurante = Restaurante()

        layout = QVBoxLayout()

        self.btn_cardapio = QPushButton("Gerenciar Cardápio")
        self.btn_pedido = QPushButton("Realizar Pedido")
        self.btn_cozinha = QPushButton("Gerenciar Cozinha")
        self.btn_relatorio = QPushButton("Ver Relatório de Vendas")

        self.btn_cardapio.clicked.connect(self.abrir_tela_cardapio)
        self.btn_pedido.clicked.connect(self.abrir_tela_pedido)
        self.btn_cozinha.clicked.connect(self.abrir_tela_cozinha)
        self.btn_relatorio.clicked.connect(self.abrir_tela_relatorio)

        layout.addWidget(self.btn_cardapio)
        layout.addWidget(self.btn_pedido)
        layout.addWidget(self.btn_cozinha)
        layout.addWidget(self.btn_relatorio)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def abrir_tela_cardapio(self):
        self.tela_cardapio = TelaCardapio(self.restaurante)
        self.tela_cardapio.show()
    
    def abrir_tela_pedido(self):
        self.tela_pedido = TelaPedido(self.restaurante)
        self.tela_pedido.show()
    
    def abrir_tela_cozinha(self):
        self.tela_cozinha = TelaCozinha(self.restaurante)
        self.tela_cozinha.show()
    
    def abrir_tela_relatorio(self):
        self.tela_relatorio = TelaRelatorio(self.restaurante)
        self.tela_relatorio.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = TelaPrincipal()
    janela.show()
    sys.exit(app.exec_())




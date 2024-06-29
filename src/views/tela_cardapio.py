from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QPushButton, QWidget, QLabel, QLineEdit, QListWidget
from controllers.controller_cardapio import ControllerCardapio

class TelaCardapio(QMainWindow):
    def __init__(self, restaurante):
        super().__init__()
        self.setWindowTitle("Gerenciar Cardápio")
        self.controller = ControllerCardapio(restaurante)

        layout = QVBoxLayout()

        self.lista_itens = QListWidget()
        self.atualizar_lista_itens()
        layout.addWidget(self.lista_itens)

        self.input_nome = QLineEdit()
        self.input_preco = QLineEdit()
        self.input_descricao = QLineEdit()

        layout.addWidget(QLabel("Nome:"))
        layout.addWidget(self.input_nome)
        layout.addWidget(QLabel("Preço:"))
        layout.addWidget(self.input_preco)
        layout.addWidget(QLabel("Descrição:"))
        layout.addWidget(self.input_descricao)

        self.btn_adicionar = QPushButton("Adicionar Item")
        self.btn_adicionar.clicked.connect(self.adicionar_item)
        layout.addWidget(self.btn_adicionar)

        self.btn_editar = QPushButton("Editar Item")
        self.btn_editar.clicked.connect(self.editar_item)
        layout.addWidget(self.btn_editar)

        self.btn_remover = QPushButton("Remover Item")
        self.btn_remover.clicked.connect(self.remover_item)
        layout.addWidget(self.btn_remover)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def atualizar_lista_itens(self):
        self.lista_itens.clear()
        itens = self.controller.listar_itens()
        for item in itens:
            self.lista_itens.addItem(f"{item.nome} - R${item.preco} - {item.descricao}")

    def adicionar_item(self):
        nome = self.input_nome.text()
        preco = float(self.input_preco.text())
        descricao = self.input_descricao.text()
        self.controller.adicionar_item(nome, preco, descricao)
        self.atualizar_lista_itens()

    def editar_item(self):
        selected_item = self.lista_itens.currentRow()
        if selected_item != -1:
            nome = self.input_nome.text()
            preco = float(self.input_preco.text())
            descricao = self.input_descricao.text()
            self.controller.editar_item(selected_item, nome, preco, descricao)
            self.atualizar_lista_itens()

    def remover_item(self):
        selected_item = self.lista_itens.currentRow()
        if selected_item != -1:
            self.controller.remover_item(selected_item)
            self.atualizar_lista_itens()

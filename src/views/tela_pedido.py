from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QPushButton, QWidget, QLabel, QListWidget, QLineEdit, QHBoxLayout, QFormLayout, QMessageBox

class TelaPedido(QMainWindow):
    def __init__(self, restaurante):
        super().__init__()
        self.setWindowTitle("Realizar Pedido")
        self.restaurante = restaurante

        layout = QVBoxLayout()

        self.lista_cardapio = QListWidget()
        self.atualizar_lista_cardapio()
        layout.addWidget(self.lista_cardapio)

        form_layout = QFormLayout()
        self.input_numero_mesa = QLineEdit()
        self.input_quantidade = QLineEdit()
        form_layout.addRow("Número da Mesa:", self.input_numero_mesa)
        form_layout.addRow("Quantidade:", self.input_quantidade)
        layout.addLayout(form_layout)

        self.btn_adicionar_item = QPushButton("Adicionar Item ao Pedido")
        self.btn_finalizar_pedido = QPushButton("Finalizar Pedido")
        self.btn_adicionar_item.clicked.connect(self.adicionar_item)
        self.btn_finalizar_pedido.clicked.connect(self.finalizar_pedido)

        layout.addWidget(self.btn_adicionar_item)
        layout.addWidget(self.btn_finalizar_pedido)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.itens_pedido = []

    def atualizar_lista_cardapio(self):
        self.lista_cardapio.clear()
        for item in self.restaurante.cardapio:
            self.lista_cardapio.addItem(f"{item.nome} - R${item.preco} - {item.descricao}")

    def adicionar_item(self):
        current_item = self.lista_cardapio.currentItem()
        if current_item:
            item_nome = current_item.text().split(" - ")[0]
            item = next((i for i in self.restaurante.cardapio if i.nome == item_nome), None)
            if item:
                quantidade = int(self.input_quantidade.text())
                self.itens_pedido.append((item, quantidade))
                QMessageBox.information(self, "Item Adicionado", f"{item.nome} x{quantidade} adicionado ao pedido.")
                self.input_quantidade.clear()

    def finalizar_pedido(self):
        numero_mesa = self.input_numero_mesa.text()
        if numero_mesa and self.itens_pedido:
            self.restaurante.realizar_pedido(numero_mesa, self.itens_pedido)
            QMessageBox.information(self, "Pedido Finalizado", "O pedido foi realizado com sucesso.")
            self.input_numero_mesa.clear()
            self.itens_pedido = []
        else:
            QMessageBox.warning(self, "Erro", "Número da mesa e itens do pedido são necessários.")

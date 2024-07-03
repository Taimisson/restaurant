from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QPushButton, QWidget, QLabel, QListWidget, QMessageBox

class TelaCozinha(QMainWindow):
    def __init__(self, restaurante):
        super().__init__()
        self.setWindowTitle("Cozinha")
        self.restaurante = restaurante

        layout = QVBoxLayout()

        # Adicionando listas de pedidos para cada status
        self.lista_pedidos_pedido = QListWidget()
        self.lista_pedidos_preparacao = QListWidget()
        self.lista_pedidos_entregue = QListWidget()

        layout.addWidget(QLabel("Pedidos:"))
        layout.addWidget(self.lista_pedidos_pedido)

        layout.addWidget(QLabel("Em Preparação:"))
        layout.addWidget(self.lista_pedidos_preparacao)

        layout.addWidget(QLabel("Entregues:"))
        layout.addWidget(self.lista_pedidos_entregue)

        self.btn_preparar = QPushButton("Iniciar Preparação")
        self.btn_finalizar = QPushButton("Finalizar Preparação")
        self.btn_preparar.clicked.connect(self.iniciar_preparacao)
        self.btn_finalizar.clicked.connect(self.finalizar_preparacao)

        layout.addWidget(self.btn_preparar)
        layout.addWidget(self.btn_finalizar)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.atualizar_lista_pedidos()

    def atualizar_lista_pedidos(self):
        self.lista_pedidos_pedido.clear()
        self.lista_pedidos_preparacao.clear()
        self.lista_pedidos_entregue.clear()

        pedidos_pedido = self.restaurante.listar_pedidos("Pedido")
        pedidos_preparacao = self.restaurante.listar_pedidos("Em Preparação")
        pedidos_entregue = self.restaurante.listar_pedidos("Entregue")

        for pedido in pedidos_pedido:
            self.lista_pedidos_pedido.addItem(str(pedido))
        for pedido in pedidos_preparacao:
            self.lista_pedidos_preparacao.addItem(str(pedido))
        for pedido in pedidos_entregue:
            self.lista_pedidos_entregue.addItem(str(pedido))

    def iniciar_preparacao(self):
        current_item = self.lista_pedidos_pedido.currentItem()
        if current_item:
            numero_pedido = int(current_item.text().split(",")[0].split(" ")[1])
            if self.restaurante.alterar_status_pedido(numero_pedido, "Em Preparação"):
                QMessageBox.information(self, "Preparação Iniciada", f"Preparação do pedido {numero_pedido} iniciada.")
                self.atualizar_lista_pedidos()

    def finalizar_preparacao(self):
        current_item = self.lista_pedidos_preparacao.currentItem()
        if current_item:
            numero_pedido = int(current_item.text().split(",")[0].split(" ")[1])
            if self.restaurante.alterar_status_pedido(numero_pedido, "Entregue"):
                QMessageBox.information(self, "Preparação Finalizada", f"Preparação do pedido {numero_pedido} finalizada.")
                self.atualizar_lista_pedidos()

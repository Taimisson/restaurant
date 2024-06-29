from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QLabel, QListWidget, QWidget

class TelaRelatorio(QMainWindow):
    def __init__(self, restaurante):
        super().__init__()
        self.setWindowTitle("Relatório de Vendas")
        self.restaurante = restaurante

        layout = QVBoxLayout()

        self.label_faturamento = QLabel(f"Faturamento Total: R${self.restaurante.calcular_faturamento()[0]:.2f}")
        layout.addWidget(self.label_faturamento)

        self.lista_vendas = QListWidget()
        layout.addWidget(self.lista_vendas)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.atualizar_lista_vendas()

    def atualizar_lista_vendas(self):
        _, vendas = self.restaurante.calcular_faturamento()
        self.lista_vendas.clear()
        for item_nome, quantidade in vendas.items():
            self.lista_vendas.addItem(f"{item_nome}: {quantidade}")

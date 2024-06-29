class Pedido: 
    def __init__(self, numero_pedido, mesa):
        self.numero_pedido = numero_pedido
        self.mesa = mesa
        self.itens = []
        self.status = "Pedido"
    
    def adicionar_item(self, item, quantidade = 1):
        self.itens.append((item, quantidade))

    def alterar_status(self, novo_status):
        self.status = novo_status

    def __str__(self):
        itens_str = "\n".join([f"{item.nome} x{quantidade}" for item, quantidade in self.itens])
        return f"Pedido {self.numero_pedido}, Mesa {self.mesa}, Status: {self.status}\nItens:\n{itens_str}"
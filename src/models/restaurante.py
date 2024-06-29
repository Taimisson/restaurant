from models.item_menu import ItemMenu
from models.pedido import Pedido
from models.fila_pedidos import FilaPedidos

class Restaurante:
    def __init__(self):
        self.cardapio = []
        self.fila_pedidos = FilaPedidos()
        self.numero_pedido_atual = 1

    def adicionar_item_cardapio(self, nome, preco, descricao):
        item = ItemMenu(nome, preco, descricao)
        self.cardapio.append(item)

    def realizar_pedido(self, mesa, itens_quantidade):
        pedido = Pedido(self.numero_pedido_atual, mesa) 
        for item, quantidade in itens_quantidade:
            pedido.adicionar_item(item, quantidade)
        self.fila_pedidos.adicionar_pedido(pedido)
        self.numero_pedido_atual += 1

    def alterar_status_pedido(self, numero_pedido, novo_status):
        return self.fila_pedidos.alterar_status(numero_pedido, novo_status)
    
    def listar_pedidos(self, status):
        return self.fila_pedidos.listar_pedidos(status)

    def calcular_faturamento(self):
        total_faturado = 0
        itens_vendidos = {}
        
        pedidos_entregues = self.fila_pedidos.listar_pedidos("Entregue")
        for pedido in pedidos_entregues:
            for item, quantidade in pedido.itens:
                total_faturado += item.preco * quantidade
                if item.nome in itens_vendidos:
                    itens_vendidos[item.nome] += quantidade
                else:
                    itens_vendidos[item.nome] = quantidade

        return total_faturado, itens_vendidos
    
    def __str__(self):
        cardapio_str = "\n".join([str(item) for item in self.cardapio])
        return f"Cardápio:\n{cardapio_str}\n\nPedidos:\n{self.fila_pedidos}"

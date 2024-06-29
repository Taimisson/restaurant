from models.pedido import Pedido

class ControllerPedidos:
    def __init__(self, restaurante):
        self.restaurante = restaurante

    def adicionar_pedido(self, mesa, itens_quantidade):
        self.restaurante.realizar_pedido(mesa, itens_quantidade)

    def alterar_status_pedido(self, numero_pedido, novo_status):
        return self.restaurante.alterar_status_pedido(numero_pedido, novo_status)

    def listar_pedidos(self, status):
        return self.restaurante.listar_pedidos(status)

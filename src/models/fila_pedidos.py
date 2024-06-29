class FilaPedidos:
    def __init__(self):
        self.pedidos = {"Pedido": [], "Em Preparação": [], "Entregue": []}

    def adicionar_pedido(self, pedido):
        self.pedidos["Pedido"].append(pedido)

    def alterar_status(self, numero_pedido, novo_status):
        for status, pedidos in self.pedidos.items():
            for pedido in pedidos:
                if pedido.numero_pedido == numero_pedido:
                    pedidos.remove(pedido)
                    pedido.alterar_status(novo_status)
                    self.pedidos[novo_status].append(pedido)
                    return True
        return False

    def listar_pedidos(self, status):
        return self.pedidos[status]
    
    def __str__(self):
        result = ""
        for status, pedidos in self.pedidos.items():
            result += f"{status}:\n"
            for pedido in pedidos:
                result += f" {pedido}\n"
        return result

import queue

class FilaPedidos:
    def __init__(self):
        # Inicializa a classe com três filas diferentes para os pedidos: "Pedido", "Em Preparação" e "Entregue"
        self.pedidos = {
            "Pedido": queue.Queue(),
            "Em Preparação": queue.Queue(),
            "Entregue": queue.Queue()
        }

    def adicionar_pedido(self, pedido):
        # Adiciona um novo pedido à fila de "Pedido"
        self.pedidos["Pedido"].put(pedido)

    def alterar_status(self, numero_pedido, novo_status):
        # Altera o status de um pedido específico
        for status, fila in self.pedidos.items():
            temp_fila = queue.Queue()  # Fila temporária para armazenar pedidos não correspondentes
            found = False  # Flag para indicar se o pedido foi encontrado
            while not fila.empty():
                pedido = fila.get()
                if pedido.numero_pedido == numero_pedido:
                    # Se o pedido correspondente for encontrado, altera o status e move para a nova fila
                    pedido.alterar_status(novo_status)
                    self.pedidos[novo_status].put(pedido)
                    found = True
                else:
                    # Se não for o pedido correspondente, coloca na fila temporária
                    temp_fila.put(pedido)
            self.pedidos[status] = temp_fila  # Restaura a fila original
            if found:
                return True  # Retorna True se o pedido foi encontrado e alterado
        return False  # Retorna False se o pedido não foi encontrado

    def listar_pedidos(self, status):
        # Retorna uma lista de pedidos para um status específico
        return list(self.pedidos[status].queue)
    
    def __str__(self):
        # Gera uma string representando todos os pedidos em cada status
        result = ""
        for status, fila in self.pedidos.items():
            result += f"{status}:\n"
            for pedido in list(fila.queue):
                result += f" {pedido}\n"
        return result

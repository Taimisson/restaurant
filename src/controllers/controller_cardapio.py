from models.item_menu import ItemMenu

class ControllerCardapio:
    def __init__(self, restaurante):
        self.restaurante = restaurante

    def adicionar_item(self, nome, preco, descricao):
        self.restaurante.adicionar_item_cardapio(nome, preco, descricao)

    def editar_item(self, indice, nome, preco, descricao):
        item = self.restaurante.cardapio[indice]
        item.nome = nome
        item.preco = preco
        item.descricao = descricao

    def remover_item(self, indice):
        item = self.restaurante.cardapio[indice]
        self.restaurante.cardapio.remove(item)

    def listar_itens(self):
        return self.restaurante.cardapio

class ItemMenu:
    def __init__(self, nome, preco, descricao):
        self.nome = nome
        self.preco = preco
        self.descricao = descricao
    
    def __str__(self):
        return f'{self.nome}: {self.preco} - {self.descricao}'
    
    
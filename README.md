# Gerenciamento de Pedidos de Restaurante

Este projeto é uma aplicação de gerenciamento de pedidos de um restaurante, desenvolvida utilizando Python e PySide6 para a interface gráfica. O programa permite a criação e gerenciamento de pedidos, bem como a visualização de relatórios de faturamento e quantidade de itens vendidos. A aplicação simula o fluxo de pedidos desde a criação até a entrega, passando pelos status de "Pedido", "Em Preparação" e "Entregue".

## Funcionalidades

- **Cardápio**: Possui informações dos itens disponíveis no restaurante.
- **Inserção de Pedidos**: Permite a inserção de pedidos com a quantidade de cada item e o número da mesa.
- **Gerenciamento de Status**: Os pedidos passam pelos status de "Pedido", "Em Preparação" e "Entregue".
- **Visualização de Filas**: Permite visualizar as filas de pedidos em cada status.
- **Relatórios**: Apresenta o faturamento total e a quantidade de cada item vendido no dia.

## Estrutura do Projeto

O projeto está organizado da seguinte forma:

```
restaurante/
│
├── src/
│   ├── controllers/
│   │   ├── controller_cardapio.py
│   │   └── controller_pedidos.py
│   ├── models/
│   │   ├── fila_pedidos.py
│   │   ├── item_menu.py
│   │   ├── pedido.py
│   │   └── restaurante.py
│   ├── views/
│   │   ├── tela_cardapio.py
│   │   ├── tela_cozinha.py
│   │   ├── tela_pedido.py
│   │   ├── tela_principal.py
│   │   └── tela_relatorio.py
│   └── main.py
├── README.md
└── requirements.txt
```

## Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/Taimisson/restaurant.git
   ```
2. Navegue até o diretório do projeto:
   ```bash
   cd restaurante
   ```
3. Crie um ambiente virtual:
   ```bash
   python -m venv env
   ```
4. Ative o ambiente virtual:
   - No Windows:
     ```bash
     .\env\Scripts\activate
     ```
   - No macOS/Linux:
     ```bash
     source env/bin/activate
     ```
5. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

## Uso

1. Execute o arquivo `main.py` para iniciar a aplicação:
   ```bash
   python src/main.py
   ```

## Estruturas de Dados

O gerenciamento de pedidos é feito utilizando um dicionário que armazena listas de pedidos de acordo com seu status. As chaves do dicionário são "Pedido", "Em Preparação" e "Entregue", e cada uma está associada a uma lista de pedidos.

## Classes Principais

### `Restaurante`

- `adicionar_item_cardapio(nome, preco, descricao)`: Adiciona um item ao cardápio.
- `realizar_pedido(mesa, itens_quantidade)`: Realiza um pedido e o adiciona à fila de pedidos.
- `alterar_status_pedido(numero_pedido, novo_status)`: Altera o status de um pedido.
- `listar_pedidos(status)`: Lista os pedidos de acordo com o status.
- `calcular_faturamento()`: Calcula o faturamento total e a quantidade de cada item vendido.

### `FilaPedidos`

- `adicionar_pedido(pedido)`: Adiciona um pedido à fila de "Pedidos".
- `alterar_status(numero_pedido, novo_status)`: Altera o status de um pedido.
- `listar_pedidos(status)`: Lista os pedidos de acordo com o status.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests.

## Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

**Desenvolvido por Taimisson C. Schardosim e Guilherme Lenzi**

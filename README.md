** Lista de Compras

Sistema de lista de compras em Python que roda no terminal. Permite adicionar itens com quantidade, marcar como comprado e remover, tudo por um menu interativo.

** Funcionalidades
Adicionar item (nome e quantidade)
Listar itens, com [x] para os comprados
Marcar item como comprado
Remover item
Validação de entradas (nome vazio, quantidade inválida, opção inválida)
Como executar:

Requer Python 3 instalado.

bash
python lista_compras.py
Exemplo de uso
Menu:
1. Adicionar item
2. Listar itens
3. Marcar item como comprado
4. Remover item
5. Sair
Digite uma opção: 2

Sua lista:
[x] arroz - quantidade: 2
[ ] feijão - quantidade: 1
Estrutura dos dados

Os itens ficam em um dicionário, com o nome do produto como chave:

python
{"arroz": {"quantidade": 2, "comprado": False}}

Os dados ficam apenas na memória: ao fechar o programa, a lista é apagada.

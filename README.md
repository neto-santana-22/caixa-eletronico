# Caixa Eletrônico em Python

Projeto acadêmico desenvolvido em Python com o objetivo de praticar
lógica de programação, estruturas de dados, funções, condicionais, laços
de repetição e validação de entradas.

O programa simula o funcionamento básico de um caixa eletrônico,
permitindo que o usuário acesse uma conta e realize operações bancárias
pelo terminal.

## Funcionalidades

-   **Login:** autenticação utilizando número da conta e senha.
-   **Consulta de saldo:** visualização do saldo disponível.
-   **Depósito:** adição de valores ao saldo da conta.
-   **Saque:** retirada de dinheiro com cálculo automático das cédulas
    disponíveis.
-   **Extrato:** consulta do histórico de movimentações.
-   **Validação de operações:** prevenção de depósitos e saques com
    valores inválidos.
-   **Menu interativo:** navegação entre as funcionalidades do sistema.

## Regras de Saque

O sistema disponibiliza as seguintes cédulas:

-   R\$ 100
-   R\$ 50
-   R\$ 20
-   R\$ 10

Para realizar um saque:

-   O valor deve ser maior que zero.
-   O saldo deve ser suficiente.
-   O valor solicitado deve ser compatível com as cédulas disponíveis.

Caso o valor não possa ser entregue exatamente, o saque será recusado.

## Contas para Teste

O projeto possui duas contas cadastradas diretamente no código.

  Conta   Senha    Saldo inicial
  ------- -------- ---------------
  12345   123456   R\$ 1.000,00
  67890   654321   R\$ 500,00

## Tecnologias e Conceitos

-   Python 3
-   Dicionários e listas
-   Funções
-   Estruturas condicionais (`if`, `elif`, `else`)
-   Laços de repetição (`while` e `for`)
-   Tratamento de exceções (`try/except`)
-   Divisão inteira (`//`) e resto (`%`)
-   Manipulação de strings
-   Histórico de operações

## Estrutura do Projeto

``` text
caixa-eletronico/
└── main.py
```

## Como Executar

**1. Clone o repositório:**

``` bash
git clone https://github.com/neto-santana-22/caixa-eletronico.git
```

**2. Entre na pasta:**

``` bash
cd caixa-eletronico
```

**3. Execute o programa:**

``` bash
python3 main.py
```

No Windows, também é possível utilizar:

``` bash
python main.py
```

## Objetivo Acadêmico

Este projeto foi desenvolvido para aplicar conhecimentos fundamentais de
programação por meio da construção de um sistema bancário simplificado.

O foco está na organização do código, implementação de regras de
negócio, validação de dados e utilização de estruturas de controle para
resolver problemas práticos.

------------------------------------------------------------------------

**Projeto acadêmico --- Caixa Eletrônico em Python.**

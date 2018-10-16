# GA

## Requisitos

- gcc
- numpy
- matplotlib

## Modo de uso

Compile o pacote com `make`, e execute o camando:
`ga.out <tamanho-da-população> <numero-de-geraçãoes> <taxa-de-mutação> <flag>`

- A taxa de mutação deve ser numerios inteiros, como 42 para 42% de chance de
mutação de cada gene.

- Use a flag 0 para mutar apenas os filhos do campeões do torneio, e 1 para
mutar toda a população em cada geração.

- Exporte o texto da saida padrão para um arquivo e use como argumento para o
script python para gerar os graficos de frequência para cada geração


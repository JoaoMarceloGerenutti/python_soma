''' =======================================
ESAMC -  Faculdade de Sorocaba
Programa usando FOR
Disciplina 	: Lógica de Programação e Algoritmos
Professor	: Francisco Tesifom Munhoz
Data	: 1º semestre de 2020
===========================================
Atividade	: Exercício 04.2
Autor	: João Marcelo Gerenutti
Data	: 31/05/2020
Comentários	: "Perguntar ao usuário quantos números deseja somar. Em seguida, ler estes N números e apresentar o valor da soma. (Fazer 2 versões deste programa: usando FOR e usando WHILE)."
Versão usando FOR
============================================
'''

# DECLARAÇÂO DE VARIAVEL
soma = 0
num_posicao = 1
num_1 = int
num_2 = int

# ENTRADA DE DADOS
quantidade = int(input("Digite quantos números voce deseja somar: "))

# SAIDA DE DADOS
print("---------------------------------------------")

# ENTRADA DE DADOS
for item in range(0, quantidade):

    # SAIDA DE DADOS
    print("Digite o", num_posicao, "º número")

    # PROCESSAMENTO DE DADOS
    num_posicao = num_posicao + 1

    # ENTRADA DE DADOS
    num = int(input("---> "))

    # PROCESSAMENTO DE DADOS
    num_1 = soma
    soma = soma + num
    num_2 = num

    # SAIDA DE DADOS
    print("A soma de", num_1, "+", num_2, "é: ", soma)
    print("---------------------------------------------")

# SAIDA DE DADOS
print("O valor da soma do(s)", quantidade, "números é", soma)
#ALUNOS: Arthur Baldissera Claumann Marcos  RM:550219
#       Sarah Ribeiro                       RM:97747 

import time #O import do time é para saber o tempo de execução das funções

# Armazenando pontuações como listas [nome, pontuação, dificuldade] dos médicos residentes.
pontuacoes_lista = []

def adicionar_pontuacao(nome, pontuacao, dificuldade):
    inicio = time.time()
    pontuacoes_lista.append([nome, pontuacao, dificuldade])
    fim = time.time()
    print(f"Tempo para adicionar na lista: {fim - inicio:.10f} segundos")

def mostrar_pontuacoes():
    print("Pontuações (Lista):")
    for p in pontuacoes_lista:
        print(f"Nome: {p[0]}, Pontuação: {p[1]}, Dificuldade: {p[2]}")

# Exemplos:
adicionar_pontuacao('Médico Residente 1', 100, 'Fácil')
adicionar_pontuacao('Médico Residente 2', 88, 'Médio')
mostrar_pontuacoes()

# Armazenando pontuações como dicionários {nome: [pontuacao, dificuldade]} dos médicos residentes.
pontuacoes_dic = {}

def adicionar_pontuacao_dic(nome, pontuacao, dificuldade):
    inicio = time.time()
    pontuacoes_dic[nome] = [pontuacao, dificuldade]
    fim = time.time()
    print(f"Tempo para adicionar no dicionário: {fim - inicio:.10f} segundos")

def mostrar_pontuacoes_dic():
    print("Pontuações (Dicionário):")
    for nome, dados in pontuacoes_dic.items():
        print(f"Nome: {nome}, Pontuação: {dados[0]}, Dificuldade: {dados[1]}")

# Exemplos:
adicionar_pontuacao_dic('Médico Residente 1', 85, 'Fácil')
adicionar_pontuacao_dic('Médico Residente 2', 90, 'Difícil')
mostrar_pontuacoes_dic()


def fase_treinamento():
    print("Iniciando fase de treinamento...")
    inicio = time.time()
    
    input("Passe o fio pela argola e pressione Enter quando terminar...")
    
    fim = time.time()
    duracao = fim - inicio
    print(f"Treinamento concluído em {duracao:.2f} segundos!")
    
    # Avaliação simples
    if duracao < 10:
        print("Excelente rapidez!")
    elif duracao < 20:
        print("Boa velocidade.")
    else:
        print("Precisa melhorar.")

# Exemplo de uso
fase_treinamento()

#!usr/bin/env python3
"""Exibe Relatório de crianças por atividade.

Imprimir a lista de crianças agrupadas por sala que frequentas cada um das atividades.
"""
__verssion__="0.1.1"

# Dados
sala1 = ["Gabriel","Maia","Gustavo","Manuel","Sofia", "Joana","Erik"]

sala2 = ["Joao","Antonio","Carlos","Maria","Isadora"]

aula_ingles = ["Erik","Maia","Gabriel","Joana","Carlos","Antonio"]

aula_musica = ["Gabriel","Carlos","Maria"]

aula_danca = ["Gustavo","Sofia","Erik","Joana","Antonio"]

atividades = [
    ("Inglês", aula_ingles),
    ("Música", aula_musica),
    ("Dança", aula_danca),
    ]


for nome_atividade, atividade in atividades:

    print(f"Alunos da atividade {nome_atividade}\n")

    atividade_sala1 = []
    atividade_sala2 = []

    # Sala1 que tem interseção com a atividade
    atividade_sala1 = set(sala1) & set(atividade)
    atividade_sala2 = set(sala2).intersection(set(atividade))

    print("  Sala 1", atividade_sala1)
    print("  Sala 2", atividade_sala2)
    print()
    print("#" * 40)



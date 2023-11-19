
from pandas import DataFrame

#!Criando labels: Acesso simplificado a linhas e colunas da estrutura [indexes]
#* Essa indexação de linhas e colunas servem para manipulação de tabelas (linhas e colunas)
#* LINHAS E COLUNAS CO-RELACIONADAS

l= [[1,2,3],[4,5,6], [7,8,9]]

#?Criando uma matriz com colunas A,B,C:
l_columns = DataFrame(l, columns= 'A B C'.split())
# print(l_columns)
#    A  B  C
# 0  1  2  3
# 1  4  5  6
# 2  7  8  9

#?Buscando a matris com coluna A:
l_columns['A']
# print(l_columns['A'])
# 0    1
# 1    4
# 2    7
# Name: A, dtype: int64


#?Buscando a linha da matriz A,B,C:
l_line = DataFrame(l, index= 'A B C'.split())
# print(l_line)
#    0  1  2
# A  1  2  3
# B  4  5  6
# C  7  8  9


#? Referenciando linhas e colunas da matriz:
l_dataframe = DataFrame(l, columns='A B C'.split(), index='l1 l2 l3'.split())
# print(l_dataframe)
#     A  B  C
# l1  1  2  3
# l2  4  5  6
# l3  7  8  9

#?Pegando somente uma linha da matriz:
l_dataframe_linha = l_dataframe.loc['l1']
# print(l_dataframe_linha)
# A    1
# B    2
# C    3
# Name: l1, dtype: int64

#? Pegando a linha e fazendo sua transposição:
l_dataframe_linha.transpose()
# print(l_dataframe_linha.transpose())
# A    1
# B    2
# C    3
# Name: l1, dtype: int64



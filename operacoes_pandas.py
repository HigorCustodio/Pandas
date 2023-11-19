from pandas import DataFrame


#?Posso realizar operações matemáticas também: 
#? Funciona com numeros no DataFrame todas as operações algebricas!
df1= DataFrame([[1, 2], [3, 4]], columns='a b'.split(), index='l1 l2'.split())

df1 * 2
# print(df1 * 2)
#     a  b
# l1  2  4
# l2  6  8

df1 / 2
# print(df1 / 2)
#       a    b
# l1  0.5  1.0
# l2  1.5  2.0

df1 + 2
# print(df1 + 2)
#     a  b
# l1  3  4
# l2  5  6    

df1 - 2
# print(df1 - 2)
# a  b
# l1 -1  0
# l2  1  2

df1 % 2
# print(df1 % 2)
#     a  b
# l1  1  0
# l2  1  0

df1 ** 2
# print(df1 ** 2)
#     a   b
# l1  1   4
# l2  9  16


#?Homogêneas por coluna ( dados do mesmo tipo ) e Heterogêneas por linha ( dados de tipos diferentes ):

df = DataFrame([[1, 'a'], [2, 'b']], columns='a b'.split(), index='l1 l2'.split())
# print(df)
# print(df.dtypes)
#     a  b
# l1  1  a
# l2  2  b
# a     int64
# b    object
# dtype: object

#? Com misto de strings e numeros não funcionam todas as operações!
df * 2
# print(df * 2)
#     a   b
# l1  2  aa
# l2  4  bb

#! Porém, se tiver strings algumas operações não podem ser realizadas como:
#* Divisão,  Adição, Subtração, Exponenciação e Resto de divisão!
# print(df / 2)
# print(df + 2)
# print(df - 2)
# print(df % 2)
# print(df ** 2)


#? Toda operação é imutavel, gerando um novo objeto!
#* DETALHE IMPORTANTE: TODA OPERAÇÃO COM O PANDAS GERA UM NOVO OBJETO!
# Ou seja, todo operacao no pandas resulta na agregação do novo valor a um novo objeto,
#!RECOMENDA-SE SEMPRE ATRIBUIR O VALOR DA PROXIMA OPERAÇÃO A UMA NOVA VARIAVEL!
df1
# print(df1)
#     a  b
# l1  1  2
# l2  3  4

df1_quadrado = df1 ** 2
# print(df1_quadrado)
#     a   b
# l1  1   4
# l2  9  16
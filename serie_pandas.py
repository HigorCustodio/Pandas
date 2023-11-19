from pandas import Series

#! SERIES : SÃO A BASE DE TUDO!!
# Series são estruturas como arrays unidimensionais, #!VETORES.
#Contam, porém, com #*labels (etiqutas).
# Labels : Etiquetas, como as chaves e com valores anexados
# exatamente como um dicionario PYTHON.

#Series:
# - Representação de um array 1d (uma dimensão) no pandas;
# - Homogeneo;
# - Permite operações albébricas;
# - Filtros;
# - Gráficos (Plots);
# - Agrupamento;

d = {
    'Eduardo': 29,
    'Fausto': 6,
    'Joaquina': 31
}
s = Series(d)
# print(s)
# Eduardo     29
# Fausto       6
# Joaquina    31
# dtype: int64
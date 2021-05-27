import numpy as np
import pandas as pd
#import dataTraining as DT


# importar os dados
df = None
df = pd.read_csv('datasets/brazil_covid19.csv')
#print(df)

# tratar os dados faltantes
df = df.dropna()
#print(df)
# remover linha duplicadas
#print(df.shape)
df = df.drop_duplicates()
#print(df.shape)
df = df.where(df != '?').dropna()
print(df)

# definição de x e y
x = df.loc[:, ['date', 'state', 'suspects']]
y = df.drop(columns=['hour', 'suspects'])

print(f'X <=\n {x}\n Y <=\n {y}')


# Média, variância, desvio padrão e mediana para x e y.

# agrupados por dia
x_mean_by_day = x.groupby(['date']).mean()
print(f'x  group by date <=\n {x.groupby(["date"])}')
print(f'x_mean_by_day <= {x_mean_by_day}')
std_by_day = df.groupby(['date']).std()

mean_by_state = df.groupby(['state']).mean()
std_by_state = df.groupby(['state']).std()

# quantos suspects se tornaram cases?
# quantos suspects se tornaram refuses?
# quantos suspects se tornaram deaths?



# O histograma de x e y. quem é x e y?

# O coeficiente de correlação de x e y.

# Fazer o teste de normalidade para  y e x.



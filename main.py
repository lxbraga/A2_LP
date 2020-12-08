from data_processing.Data_Cleaning_Classes import CleanFifa as dff
from data_processing.Data_Cleaning_Classes import CleanCovid as dfc
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn import datasets, linear_model, metrics, model_selection
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import warnings
import geopandas as gpd
warnings.filterwarnings("ignore")

covid = dfc().fetcher()
fifa = dff().fetcher()

# ANÁLISE EXPLORATÓRIA DOS DADOS DO FIFA
    # Quantidade de paí­ses presentes na fifa
fifa['Nationality'].nunique()

    # Quantidade de jogadores por paí­s
fifa['Nationality'].value_counts()

    # Média de idades
fifa['Age'].mean()

    # Quantidade de jogadores por idade
fifa['Age'].value_counts()

    # Média de idade por clube
fifa.groupby('Club').Age.mean()

    # Média de salário por jogador
fifa['Wage'].mean()

    # Média de salário por clube
fifa.groupby('Club').Wage.mean()

    # Gasto salarial por clube
fifa.groupby('Club').Wage.sum().sort_values(ascending = False)

    # Overall por idade
fifa.groupby('Age').Overall.agg(['min','max','mean'])

    # Potencial por idade
fifa.groupby('Age').Potential.agg(['min','max','mean'])

    # Melhores médias de Overall por clube
fifa.groupby('Club').Overall.mean().sort_values(ascending = False)

    # Jogadores com mais finalizações
fifa.sort_values(by='Finishing',ascending = False)

    # Jogadores com maior potência de chute
fifa.sort_values(by='ShotPower',ascending = False )

    # Jogadores mais rápidos
fifa.sort_values(by='SprintSpeed',ascending = False )

    # Visualização salário por idade
fig = plt.figure()
ax = plt.subplot(111)
fig11 = sns.lineplot(x="Wage", y="Age",data=fifa,label="Age", ci= None)
fig.savefig('imagens/fifa/vis_salarios/fig11.png')

    # Visualização salário por overall
fig = plt.figure()
ax = plt.subplot(111)
fig12 = sns.lineplot(x="Wage", y="Overall",data=fifa,label="Overall", ci= None)
fig.savefig('imagens/fifa/vis_salarios/fig12.png')

    # Visualização salário por potential
fig = plt.figure()
ax = plt.subplot(111)
fig13 = sns.lineplot(x="Wage", y="Potential",data=fifa,label="Potential", ci= None)
fig.savefig('imagens/fifa/vis_salarios/fig13.png')

#PRIMEIRA ANALISE DO FIFA
## Ordenando os valores e agroupando eles
# Agrupamos por time e ordenamos em ordem decrescente para descobrirmos os times no topo e no final em relação ao aproveitamento de pênaltis.#
fifa_penalties_club = fifa.groupby(["Club"]).mean()
fifa_penalties_club = fifa_penalties_club.sort_values(by = "Penalties", ascending = False)

#Agora que sabemos os times no topo e no final da tabela de pênaltis, podemos filtrar cada um; fifa_mp para Melhor Pênalti e fifa_pp para Pior Pênalti.
fifa_mp = fifa[fifa["Club"].isin(["Grêmio", "Internacional","FC Schalke 04", "Besiktas JK", "Atlético Mineiro"])]
fifa_pp = fifa[fifa["Club"].isin(["IF Brommapojkarna", "FC Nordsjælland","Trelleborgs FF", "Bray Wanderers", "Derry City"])]

fig = plt.figure()
ax = plt.subplot(111)
fig_errada = sns.lineplot(x = fifa_mp["ID"], y =fifa_mp["Finishing"], label = "Melhores times - finalizações"), sns.lineplot(x = fifa_pp["ID"], y =fifa_pp["Finishing"], label = "Piores times - finalizações")
fig.savefig('imagens/fifa/aprov_penaltis/ErradoPenalti-Finalizacao.png')



#Devemos criar e deletar as colunas de ID pois quando re-organizamos segundo cada atributo, devemos mudar os valores do ID; ex: a ordem de ID com atributo Curve é diferente do Strength, por exemplo.
## FINALIZAÇÃO por time - melhor aproveitamento e pior
fig = plt.figure()
ax = plt.subplot(111)
fifa_mp= fifa_mp.sort_values(by = "Finishing")
fifa_pp= fifa_pp.sort_values(by = "Finishing")
fifa_mp["ID"] = range(len(fifa_mp["Name"]))
fifa_pp["ID"] = range(len(fifa_pp["Name"]))
fig = plt.figure()
ax = plt.subplot(111)
fig1 = sns.lineplot(x = fifa_mp["ID"], y =fifa_mp["Finishing"], label = "Melhores times - finalizações"), sns.lineplot(x = fifa_pp["ID"], y =fifa_pp["Finishing"], label = "Piores times - finalizações")
fig.savefig('imagens/fifa/aprov_penaltis/Finalizacao.png')
del fifa_mp["ID"]
del fifa_pp["ID"]

## CURVA por time - melhor aproveitamento e pior
fifa_mp= fifa_mp.sort_values(by = "Curve")
fifa_pp= fifa_pp.sort_values(by = "Curve")
fifa_mp["ID"] = range(len(fifa_mp["Name"]))
fifa_pp["ID"] = range(len(fifa_pp["Name"]))
fig = plt.figure()
ax = plt.subplot(111)
fig2 = sns.lineplot(x = fifa_mp["ID"], y =fifa_mp["Curve"],label = "Melhores times - curvatura do chute"), sns.lineplot(x = fifa_pp["ID"], y =fifa_pp["Curve"],label = "Piores times - curvatura do chute")
fig.savefig('imagens/fifa/aprov_penaltis/Curvatura.png')
del fifa_mp["ID"]
del fifa_pp["ID"]

## FORÇA por time - melhor aproveitamento e pior
fifa_mp= fifa_mp.sort_values(by = "Strength")
fifa_pp= fifa_pp.sort_values(by = "Strength")
fifa_mp["ID"] = range(len(fifa_mp["Name"]))
fifa_pp["ID"] = range(len(fifa_pp["Name"]))
fig = plt.figure()
ax = plt.subplot(111)
fig3 = sns.lineplot(x = fifa_mp["ID"], y =fifa_mp["Strength"],label = "Melhores times - força do chute"), sns.lineplot(x = fifa_pp["ID"], y =fifa_pp["Strength"],label = "Piores times - força do chute")
fig.savefig('imagens/fifa/aprov_penaltis/ForcaDoChute.png')
del fifa_mp["ID"]
del fifa_pp["ID"]

## AGRESSÃO por time - melhor aproveitamento e pior
fifa_mp= fifa_mp.sort_values(by = "Aggression")
fifa_pp= fifa_pp.sort_values(by = "Aggression")
fifa_mp["ID"] = range(len(fifa_mp["Name"]))
fifa_pp["ID"] = range(len(fifa_pp["Name"]))
fig = plt.figure()
ax = plt.subplot(111)
fig4 = sns.lineplot(x = fifa_mp["ID"], y =fifa_mp["Aggression"],label = "Melhores times - agressão do jogador"), sns.lineplot(x = fifa_pp["ID"], y =fifa_pp["Aggression"],label = "Piores times - agressão do jogador")
fig.savefig('imagens/fifa/aprov_penaltis/Agressao.png')
del fifa_mp["ID"]
del fifa_pp["ID"]

#SEGUNDA ANÁLISE DO FIFA
## Analise Geral por IDADE - ["Wage", "Overall", "Stamina", "Jumping", "Agility", "Weight"]
# SALARIO
SalarioPorIdade = fifa.groupby('Age').Wage.agg(["min","max","mean"])
print(SalarioPorIdade)
SalarioPorIdade["Age"] = range(16,42)
fig = plt.figure()
ax = plt.subplot(111)
fig5 = sns.lineplot(x = SalarioPorIdade["Age"] , y =SalarioPorIdade["mean"],label = "Média do salário por Idade", color = "red")
fig.savefig('imagens/fifa/analise_idade/Salario_idade.png')

#NOTA GERAL
RatingPorIdade = fifa.groupby('Age').Overall.agg(['min','max','mean'])
RatingPorIdade["Age"] = range(16,42)
fig = plt.figure()
ax = plt.subplot(111)
fig6 = sns.lineplot(x = RatingPorIdade["Age"] , y =RatingPorIdade["mean"],label = "Média da nota geral por Idade", color = "blue" )
fig.savefig('imagens/fifa/analise_idade/NotaGeral_idade.png')

#STAMINA
StaminaPorIdade = fifa.groupby('Age').Stamina.agg(['min','max','mean'])
StaminaPorIdade ["Age"] = range(16,42)
fig = plt.figure()
ax = plt.subplot(111)
fig7 = sns.lineplot(x = StaminaPorIdade ["Age"] , y =StaminaPorIdade ["mean"],label = "Stamina por Idade", color = "green" )
fig.savefig('imagens/fifa/analise_idade/Stamina_idade.png')

#JUMPING - PULO
PuloPorIdade = fifa.groupby('Age').Jumping.agg(['min','max','mean'])
PuloPorIdade["Age"] = range(16,42)
fig = plt.figure()
ax = plt.subplot(111)
fig8 = sns.lineplot(x = PuloPorIdade["Age"] , y =PuloPorIdade["mean"],label = "Pulo por Idade", color = "black" )
fig.savefig('imagens/fifa/analise_idade/Pulo_idade.png')

#AGILITY - AGILIDADE
AgilidadePorIdade = fifa.groupby('Age').Agility.agg(['min','max','mean'])
AgilidadePorIdade["Age"] = range(16,42)
fig = plt.figure()
ax = plt.subplot(111)
fig9 = sns.lineplot(x = AgilidadePorIdade["Age"] , y =AgilidadePorIdade["mean"],label = "Agilidade por Idade", color = "purple" )
fig.savefig('imagens/fifa/analise_idade/Agilidade_idade.png')

#WEIGHT - PESO
PesoPorIdade = fifa.groupby('Age').Weight.agg(['min','max','mean'])
PesoPorIdade["Age"] = range(16,42)
fig = plt.figure()
ax = plt.subplot(111)
fig10 =sns.lineplot(x = PesoPorIdade["Age"] , y =PesoPorIdade["mean"],label = "Peso por Idade", color = "cyan" )
fig.savefig('imagens/fifa/analise_idade/Peso_idade.png')

# Regressão linear-------------------------------------
# criação de um modelo para prever a relação entre potencial do jogador e sua idade
x=fifa["Age"] # Variável independente
y=fifa["Potential"] # Variável dependente
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=0)
model = LinearRegression()
x_train=np.array(x_train)
y_train=np.array(y_train)
x_train=x_train.reshape(-1,1)
y_train=y_train.reshape(-1,1)
model.fit(x_train,y_train)
x_test=np.array(x_test)
x_test=x_test.reshape(-1,1)
y_pred= model.predict(x_test)

    # Visualizando dataset de treino
    # Onde os dados serão utilizados para refinir o sistema de predição
plt.scatter(x_train,y_train,color="red")
plt.xlabel("Age of Player")
plt.ylabel("Potential of Player")
fig = plt.Figure()
fig.set_canvas(plt.gcf().canvas)
ax = plt.subplot(111)
fig14 = plt.plot(x_train, model.predict(x_train),color="blue")
fig.savefig('imagens/fifa/regressoes/regressao_linear1_treino.png')

    # Visualizando dataset de teste
    # Onde os dados serão previstos com base no conjunto de treino, medindo a eficiência de previsão
plt.scatter(x_test,y_test,color="red")
plt.xlabel("Age of Player")
plt.ylabel("Potential of Player")
fig = plt.Figure()
fig.set_canvas(plt.gcf().canvas)
ax = plt.subplot(111)
fig15 = plt.plot(x_train, model.predict(x_train),color="blue")
fig.savefig('imagens/fifa/regressoes/regressao_linear1_teste.png')

    # Encontrando interseção da linha de regressão
model.intercept_

    # Encontrando coeficiente da regressão linear
    # é o grau de afinidade entre as variáveis, definindo se estão muito relacionadas (1) ou não possuem relação (0)
model.score(x_train,y_train)

    # Encontrando mse (mean squared error)
mse = metrics.mean_squared_error(y_test,y_pred)
print(mse)

    ## Podemos notar que não há uma relação entre o potencial do jogador e sua idade (através do R2 - model.score()), o que nos leva a buscar outro dado que se adeque melhor.

    ## Já nesse modelo, podemos notar que há relação positiva entre o potencial do jogador e seu salário (através do R2 - model.score())
# Regressão linear - prevendo potencial baseado no salário
x=fifa["Wage"] # Variável independente
y=fifa["Potential"] # Variável dependente
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=0)
model = LinearRegression()
x_train=np.array(x_train)
y_train=np.array(y_train)
x_train=x_train.reshape(-1,1)
y_train=y_train.reshape(-1,1)
model.fit(x_train,y_train)
x_test=np.array(x_test)
x_test=x_test.reshape(-1,1)
y_pred= model.predict(x_test)

    # Visualizando dataset de treino
    # Onde os dados serão utilizados para refinir o sistema de predição
plt.scatter(x_train,y_train,color="red")
plt.xlabel("Wage")
plt.ylabel("Potential of Player")
fig = plt.Figure()
fig.set_canvas(plt.gcf().canvas)
ax = plt.subplot(111)
fig16 = plt.plot(x_train, model.predict(x_train),color="blue")
fig.savefig('imagens/fifa/regressoes/regressao_linear2_treino.png')

    # Visualizando dataset de teste
    # Onde os dados serão previstos com base no conjunto de treino, medindo a eficiência de previsão
plt.scatter(x_test,y_test,color="red")
plt.xlabel("Wage")
plt.ylabel("Potential of Player")
fig = plt.Figure()
fig.set_canvas(plt.gcf().canvas)
ax = plt.subplot(111)
fig17 = plt.plot(x_train, model.predict(x_train),color="blue")
fig.savefig('imagens/fifa/regressoes/regressao_linear2_teste.png')

    # Encontrando interseção da linha de regressão
model.intercept_

    # Encontrando coeficiente da regressão linear
    # é o grau de afinidade entre as variáveis, definindo se estão muito relacionadas (1) ou não possuem relação (0)
model.score(x_train,y_train)

    # Encontrando mse (mean squared error)
mse = metrics.mean_squared_error(y_test,y_pred)
print(mse)    

    ## Foram utilizados dados para definir uma correlação entre o salário dos jogadores e sua idade, pontuação de overall e potencial
# Regressão múltipla - salário por idade, overall e potencial
x=fifa[["Age","Overall","Potential"]]
y=fifa["Wage"]

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)
model = LinearRegression()
model.fit(x_train,y_train)
model.predict(x_test)
y_pred= model.predict(x_test)

    # Visualizando valores atuais e previstos de salário por jogador
fig = plt.Figure()
fig.set_canvas(plt.gcf().canvas)
ax = plt.subplot(111)
fig18 = plt.scatter(y_test,y_pred), plt.xlabel("Actual Wage"), plt.ylabel("Predicted Wage")
fig.savefig('imagens/fifa/regressoes/regressao_multipla_teste.png')

    # Afinidade entre os dados avaliados
    # Há uma afinidade de 0.35 entre o salário dos jogadores e os demais dados avaliados
model.score(x_train,y_train)



## COVID ------------------------------------------
covid["Lat"] = ""
covid["Long"] = ""
for i in range(len(covid["Centroid"])):
    covid["Centroid"][i] = covid["Centroid"][i][6:-1]
    covid["Lat"][i] = covid["Centroid"][i].split(" ")[0] 
    covid["Long"][i] = covid["Centroid"][i].split(" ")[1] 

#Achamos no mapa o lugar dos aeroportos da basex
gdf = gpd.GeoDataFrame(covid, geometry=gpd.points_from_xy(covid["Lat"],covid["Long"]))
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
ax = world.plot(column='PercentOfBaseline',color='white', edgecolor='black',figsize=(15,9))
ax.set_title('Aeroportos analisados na tabela - Covid', fontdict= {'fontsize':25})
ax.set_axis_off()   
ax.get_figure()
gdf.plot(ax=ax, color='red')
plt.savefig("imagens/Covid/mapa .png")
plt.show()





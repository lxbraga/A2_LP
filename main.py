from Data_Cleaning import CleanFifa as dc
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn import datasets, linear_model, metrics, model_selection
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


fifa = dc().fetcher()

#PRIMEIRA ANALISE DO FIFA
## Ordenando os valores e agroupando eles
# Agrupamos por time e ordenamos em ordem decrescente para descobrirmos os times no topo e no final em relação ao aproveitamento de pênaltis.#
fifa_penalties_club = fifa.groupby(["Club"]).mean()
fifa_penalties_club = fifa_penalties_club.sort_values(by = "Penalties", ascending = False)

#Agora que sabemos os times no topo e no final da tabela de pênaltis, podemos filtrar cada um; fifa_mp para Melhor Pênalti e fifa_pp para Pior Pênalti.
fifa_mp = fifa[fifa["Club"].isin(["Grêmio", "Internacional","FC Schalke 04", "Besiktas JK", "Atlético Mineiro"])]
fifa_pp = fifa[fifa["Club"].isin(["IF Brommapojkarna", "FC Nordsjælland","Trelleborgs FF", "Bray Wanderers", "Derry City"])]

fig_errada = sns.lineplot(x = fifa_mp["ID"], y =fifa_mp["Finishing"], label = "Melhores times - finalizações"), sns.lineplot(x = fifa_pp["ID"], y =fifa_pp["Finishing"], label = "Piores times - finalizações")
figura = fig_errada.get_figure()
figura.savefig("ErradoPenalti-Finalizacao.png", dpi = 400)


#Devemos criar e deletar as colunas de ID pois quando re-organizamos segundo cada atributo, devemos mudar os valores do ID; ex: a ordem de ID com atributo Curve é diferente do Strength, por exemplo.
## FINALIZAÇÃO por time - melhor aproveitamento e pior
fifa_mp= fifa_mp.sort_values(by = "Finishing")
fifa_pp= fifa_pp.sort_values(by = "Finishing")
fifa_mp["ID"] = range(len(fifa_mp["Name"]))
fifa_pp["ID"] = range(len(fifa_pp["Name"]))
fig1 = sns.lineplot(x = fifa_mp["ID"], y =fifa_mp["Finishing"], label = "Melhores times - finalizações"), sns.lineplot(x = fifa_pp["ID"], y =fifa_pp["Finishing"], label = "Piores times - finalizações")
figura = fig1.get_figure()
figura.savefig("Finalizacao.png", dpi = 400)
del fifa_mp["ID"]
del fifa_pp["ID"]

## CURVA por time - melhor aproveitamento e pior
fifa_mp= fifa_mp.sort_values(by = "Curve")
fifa_pp= fifa_pp.sort_values(by = "Curve")
fifa_mp["ID"] = range(len(fifa_mp["Name"]))
fifa_pp["ID"] = range(len(fifa_pp["Name"]))
fig2 = sns.lineplot(x = fifa_mp["ID"], y =fifa_mp["Curve"],label = "Melhores times - curvatura do chute"), sns.lineplot(x = fifa_pp["ID"], y =fifa_pp["Curve"],label = "Piores times - curvatura do chute")
figura = fig2.get_figure()
figura.savefig("Curvatura.png", dpi = 400)
del fifa_mp["ID"]
del fifa_pp["ID"]

## FORÇA por time - melhor aproveitamento e pior
fifa_mp= fifa_mp.sort_values(by = "Strength")
fifa_pp= fifa_pp.sort_values(by = "Strength")
fifa_mp["ID"] = range(len(fifa_mp["Name"]))
fifa_pp["ID"] = range(len(fifa_pp["Name"]))
fig3 = sns.lineplot(x = fifa_mp["ID"], y =fifa_mp["Strength"],label = "Melhores times - força do chute"), sns.lineplot(x = fifa_pp["ID"], y =fifa_pp["Strength"],label = "Piores times - força do chute")
figura = fig3.get_figure()
figura.savefig("ForcaDoChute.png", dpi = 400)
del fifa_mp["ID"]
del fifa_pp["ID"]

## AGRESSÃO por time - melhor aproveitamento e pior
fifa_mp= fifa_mp.sort_values(by = "Aggression")
fifa_pp= fifa_pp.sort_values(by = "Aggression")
fifa_mp["ID"] = range(len(fifa_mp["Name"]))
fifa_pp["ID"] = range(len(fifa_pp["Name"]))
fig4 = sns.lineplot(x = fifa_mp["ID"], y =fifa_mp["Aggression"],label = "Melhores times - agressão do jogador"), sns.lineplot(x = fifa_pp["ID"], y =fifa_pp["Aggression"],label = "Piores times - agressão do jogador")
figura = fig4.get_figure()
figura.savefig("Agressao  .png", dpi = 400)
del fifa_mp["ID"]
del fifa_pp["ID"]

#SEGUNDA ANÁLISE DO FIFA
## Analise Geral por IDADE - ["Wage", "Overall", "Stamina", "Jumping", "Agility", "Weight"]
# SALARIO
SalarioPorIdade = fifa.groupby('Age').Wage.agg(["min","max","mean"])
print(SalarioPorIdade)
SalarioPorIdade["Age"] = range(16,42)
fig5 = sns.lineplot(x = SalarioPorIdade["Age"] , y =SalarioPorIdade["mean"],label = "Média do salário por Idade", color = "red")
figura = fig5.get_figure()
figura.savefig("Salario_idade.png", dpi = 400)

#NOTA GERAL
RatingPorIdade = fifa.groupby('Age').Overall.agg(['min','max','mean'])
RatingPorIdade["Age"] = range(16,42)
fig6 = sns.lineplot(x = RatingPorIdade["Age"] , y =RatingPorIdade["mean"],label = "Média da nota geral por Idade", color = "blue" )
figura = fig6.get_figure()
figura.savefig("NotaGeral_idade.png", dpi = 400)

#STAMINA
StaminaPorIdade = fifa.groupby('Age').Stamina.agg(['min','max','mean'])
StaminaPorIdade ["Age"] = range(16,42)
fig7 = sns.lineplot(x = StaminaPorIdade ["Age"] , y =StaminaPorIdade ["mean"],label = "Stamina por Idade", color = "green" )
figura = fig7.get_figure()
figura.savefig("Stamina_idade.png", dpi = 400)

#JUMPING - PULO
PuloPorIdade = fifa.groupby('Age').Jumping.agg(['min','max','mean'])
PuloPorIdade["Age"] = range(16,42)
fig8 = sns.lineplot(x = PuloPorIdade["Age"] , y =PuloPorIdade["mean"],label = "Pulo por Idade", color = "black" )
figura = fig8.get_figure()
figura.savefig("Pulo_idade.png", dpi = 400)

#AGILITY - AGILIDADE
AgilidadePorIdade = fifa.groupby('Age').Agility.agg(['min','max','mean'])
AgilidadePorIdade["Age"] = range(16,42)
fig9 = sns.lineplot(x = AgilidadePorIdade["Age"] , y =AgilidadePorIdade["mean"],label = "Agilidade por Idade", color = "purple" )
figura = fig9.get_figure()
figura.savefig("Agilidade_idade.png", dpi = 400)

#WEIGHT - PESO
PesoPorIdade = fifa.groupby('Age').Weight.agg(['min','max','mean'])
PesoPorIdade["Age"] = range(16,42)
fig10 =sns.lineplot(x = PesoPorIdade["Age"] , y =PesoPorIdade["mean"],label = "Peso por Idade", color = "cyan" )
figura = fig9.get_figure()
figura.savefig("Peso_idade.png", dpi = 400)

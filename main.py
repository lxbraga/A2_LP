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





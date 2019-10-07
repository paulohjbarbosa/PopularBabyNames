import pandas as pd 
import seaborn as sns 
import matplotlib.pyplot as plt
import numpy as np

#Leitura do arquivo
name_baby = pd.read_csv('C:/Temp/PopularBabyNames/src/Popular_Baby_Names.csv') 
#Renomeando as Colunas
name_baby.columns = ["anoNascimento","genero","etnia","nomeBebe","quantidade","ranque"]

name_baby.head()


#mostrando a média da coluna nota do arquivo Popular_Baby_Names.csv
print("Média",name_baby['anoNascimento'].mean().round(0))

#detalhando a coluna quantidade do arquivo Popular_Baby_Names.csv
name_baby.anoNascimento.describe().round(0)


#usando a biblioteca seaborn para gerar um gáfico de coluna utilizando a columa nota do arquivo Popular_Baby_Names.csv
sns.boxplot(name_baby.quantidade)

name_baby_genero = name_baby.groupby("nomeBebe").mean()["quantidade"]
name_baby_genero.plot(kind="hist")
name_baby_genero.describe()

print("Gênero")
name_baby.genero.value_counts()

name_baby.query("genero=='MALE'").nomeBebe.value_counts()

name_baby.query("genero=='FEMALE'").nomeBebe.value_counts()

mulheres_hispanicas = name_baby.query("genero=='FEMALE' & etnia == 'HISPANIC'")

sns.catplot(x = "genero", data = mulheres_hispanicas, kind="count")

plt.figure(figsize=(5,10))
sns.catplot(x = "genero", data = mulheres_hispanicas, kind="count", aspect=2)

quantidade_h = name_baby.query("genero=='MALE'")
quantidade_m = name_baby.query("genero=='FEMALE'")

plt.boxplot([quantidade_h.quantidade,quantidade_m.quantidade])

sns.boxplot(x = "quantidade", y = "genero", data =quantidade_h)

sns.boxplot(x = "quantidade", y = "genero", data =quantidade_m)

print(np.mean(quantidade_h.quantidade), np.mean(quantidade_m.quantidade))
print(np.std(quantidade_h.quantidade), np.std(quantidade_m.quantidade))
print(np.median(quantidade_h.quantidade), np.median(quantidade_m.quantidade))





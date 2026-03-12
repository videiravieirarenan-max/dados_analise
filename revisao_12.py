9como filtar uma coluna d evlaoresython
lista=[1,2,3,4,5,6,7]
print(lista)
#2 como pegar o 1 elemento de uma lista em python?
print(lista[0])
#3 como identificar um dicionário em python?
dict_1={"renan":20,"altura":183}
#4 Como pegar um elemento em dicionário?
print("renan"["altura"])
# 5 Como identificar uma lista de dicionário?
lista_2=(1,2,3,)
dict_2={"marca":"ford","modelo":"ecosport"}
#Como transformar uma lista dicionário em dataframe?
import pandas as pd
df= pd.dataframe(lista)

df=pd.dataframe([dicionario])
# 7 como consumir um arquivo csv no dataframe?
import pandas as pd
pd.dataframe(lista_2)
# importa excel
#df=dataframe(seuarquivo)
# 9 como filtrar uma coluna de valores4

filtro=df ["national_rank] > 4
df.loc[filtro,["filtro","country"]]

# 10 como filtrar uma coluna de string?
filtro= df ["institution"].str.contains()]
df[filtro]

filtro_1 = df ["national"] > 4
filtro2 = df ["instituion"].str.contains("^c") 
df[filtro & filtro2]
            
           


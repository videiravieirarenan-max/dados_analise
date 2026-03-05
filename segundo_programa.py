import pandas as pd
df = pd.read_csv("C:\\Users\\videi\\OneDrive\\Documents\\analisededados-renan\\notas.csv")
df.shape
df.columns
df.dtypes
df.isna().sum()
df.head()
df.tail()
df.shape
df.isnull().sum()
df.loc[:, "year"].unique()
df.loc[:,"country"].unique()
len(df.loc[:,"country"].unique())
df.loc[:,"country"].value_counts()  
df.columns
df.loc[:,"country"].mean()
df.loc[:,"score"].value_counts()
df.loc[:,"score"].max()
df.loc[:,"score"].min()
df.loc[:,"score"].median()
df.loc[:,"score"].groupby(df.loc[:,"country"]).mean()
df.loc[:,"score"].std()
df.columns[df.columns.str.contains("word rank")]
df.loc[0:9, ["institution", "world rank","years"]].sort_values("world rank")
df.loc[:, ["institution","world rank","years"]].sort_values("world rank")
df.loc[:, ["institution","world rank"]].sort_values("world rank")
filtro= df["country"]=="Brazil"
df.loc[filtro, ["institution","national_rank","country"]].sort_values()
filtro=(df["world_rank"]>=1) & (df["world_rank"]<=100)
df.loc[filtro, ["institution","national_rank","country","year"]].sort_values("world_rank")


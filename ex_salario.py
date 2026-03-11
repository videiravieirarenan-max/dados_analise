#1.	Quantas linhas e quantas colunas tem o dataset?
#2.	Qual a média salarial? Qual é o maior salário? O menor salário?
#3.	Crie um df com apenas as colunas job_title, salary, company_location, company_size, remote_ratio?
#4.	Qual é o maior e menor salário de um “Data Scientist”? Onde fica essas empresas?
#5.	Qual a profissão com a maior média salarial? E a menor?
#6.	Quais as profissões com a média salarial maior que a média geral?
#7.	Qual a localização com maior média salarial?
#8.	Quais as profissões que existem no Brasil (BR)?
#9.	Qual a média salarial no Brasil?
#10.	Quantas profissões existem no Brasil?
#11.	Qual a profissão que mais ganha no Brasil?
#12.	Quantas profissões tem nos US e que trabalham em empresas grandes (L)?
#13.	Qual é a média salarial das empresas médias (M) na Canada (CA)?
#14.	Qual é o país com mais profissões? E qual é o mais com menos?
#15.	Quem ganha mais que trabalha remoto, presencial ou híbrido?
#16.	Qual o país com maior numero de profissões trabalhando 100% remoto?

# 1 a 5

import pandas as pd
df.shape
arquivo = "ds_salaries.csv"
df=pd.read_csv(arquivo)
media_salario = df['salary_in_usd'].mean()
maior_salario = df['salary_in_usd'].max()
menor_salario = df['salary_in_usd'].min()

print("Média:", media_salario)
print("Maior:", maior_salario)
print("Menor:", menor_salario)

# 6 a 8

df2 = df[['job_title','salary_in_usd','company_location','company_size','remote_ratio']]
df2.head()



filtro_ds = df['job_title'] == 'Data Scientist'


df_ds = df.loc[filtro_ds, ['salary_in_usd', 'company_location']]
maior_salario_ds = df_ds['salary_in_usd'].max() 
menor_salario_ds = df_ds['salary_in_usd'].min()

print("Maior salário de Data Scientist:", maior_salario_ds)
print("Menor salário de Data Scientist:", menor_salario_ds)

media_salarial_por_profissao = df.groupby('job_title')['salary_in_usd'].
mean()sort_values(ascending=False)
media_salarial_geral = df['salary_in_usd'].mean()
prof_br = df[df['company_location'] == 'BR']['job_title'].unique()

#9.	Qual a média salarial no Brasil?
media_salarial_br = df[df['company_location'] == 'BR']['salary_in_usd'].mean()
print("Média salarial no Brasil:", media_salarial_br)

#10.	Quantas profissões existem no Brasil?
quantidade_profissoes_br = len(df[df['company_location'] == 'BR']['job_title'].unique())
print("Quantidade de profissões no Brasil:", quantidade_profissoes_br)

#11.	Qual a profissão que mais ganha no Brasil?
profissao_mais_ganha_br = df[df['company_location'] == 'BR'].groupby('job_title')['salary_in_usd'].mean().idxmax()
print("Profissão que mais ganha no Brasil:", profissao_mais_ganha_br)

#12.	Quantas profissões tem nos US e que trabalham em empresas grandes (L)?
quantidade_profissoes_us_large = len(df[(df['company_location'] == 'US') & (df['company_size'] == 'L')]['job_title'].unique())
print("Quantidade de profissões nos US em empresas grandes:", quantidade_profissoes_us_large)   

#13.	Qual é a média salarial das empresas médias (M) na Canada (CA)?
media_salarial_ca_medium = df[(df['company_location'] == 'CA') & (df['company_size'] == 'M')]['salary_in_usd'].mean()
print("Média salarial das empresas médias na Canada:", media_salarial_ca_medium)        

#14.	Qual é o país com mais profissões? E qual é o mais com menos?
profissoes_por_pais = df.groupby('company_location')['job_title'].nunique()    
pais_mais_profissoes = profissoes_por_pais.idxmax()
pais_menos_profissoes = profissoes_por_pais.idxmin()
print("País com mais profissões:", pais_mais_profissoes)
print("País com menos profissões:", pais_menos_profissoes)  

#15.	Quem ganha mais que trabalha remoto, presencial ou híbrido?
media_salarial_remoto = df[df['remote_ratio'] == 100]['salary_in_usd'].mean()
media_salarial_presencial = df[df['remote_ratio'] == 0]['salary_in  usd'].mean()
media_salarial_hibrido = df[(df['remote_ratio'] > 0) & (df['remote_ratio'] < 100)]['salary_in_usd'].mean()  

#16.	Qual o país com maior numero de profissões trabalhando 100% remoto?
profissoes_remoto_por_pais = df[df['remote_ratio'] == 100].groupby('company_location')['job_title'].nunique()
pais_mais_profissoes_remoto = profissoes_remoto_por_pais.idxmax()
print("País com maior número de profissões trabalhando 100% remoto:", pais_mais_profissoes_remoto)      
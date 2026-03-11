#Exercício 1: Criando um Dicionário
#Crie um dicionário chamado 'aluno' com as seguintes chaves:
#- 'nome': contendo um nome fictício,
#- 'idade': contendo a idade do aluno,
#- 'curso': contendo o curso que ele está matriculado.
#Após criar o dicionário, exiba seus valores no seguinte formato:
#Nome: <nome>
#Idade: <idade>
Curso: <curso>

aluno={"nome":"Osvaldo Aranha","idade":25,"curso":"Engenharia de Software"}
print(f"Nome: {aluno['nome']}")
print(f"Idade: {aluno['idade']}")
print(f"Curso: {aluno['curso']}")

#Exercício 2: Manipulação de Dicionário
#Dado o dicionário abaixo:
#produto = {
  #  "nome": "Teclado Mecânico",
  #  "preco": 350.00,
  #  "estoque": 10
#}
1. #Adicione uma nova chave chamada 'marca' com um valor de sua escolha.
2. #Atualize o preço do produto para R$ 320,00.
3. #Reduza o estoque em 2 unidades.
4. #Remova a chave 'marca' do dicionário.
5. #Exiba o dicionário atualizado.
produto = {
    "nome": "Teclado Mecânico",
    "preco": 350.00,
    "estoque": 10
}
produto["marca"]="Nike"
produto["preco"]=320.00
produto["estoque"]=produto["estoque"]-2
del produto["marca"]        
print(produto)

#Exercício 3: Iterando sobre um Dicionário
#Dado o dicionário:
#notas = {
   # "Alice": 8.5,
   # "Bruno": 7.0,
    #"Carla": 9.2,
    #"Daniel": 6.8}
#1. Itere sobre o dicionário e exiba os nomes dos alunos e suas respectivas notas.
#2. Calcule a média das notas e exiba o resultado.
notas={"alice":8.5,"bruno":7.0,"carla":9.2,"daniel":6.8
       }
for alunos,notas in notas.items():
    print(f"{alunos} tem nota {notas}")


    #Exercício 4: Soma de Valores
#Dado um dicionário com valores numéricos, percorra o dicionário e some todos os valores.
#Exemplo:
#numeros = {"a": 10, "b": 20, "c": 30}
#Saída esperada: 60

dic_numerico={"a":10,"b":20,"c":30}
soma = sum(dic_numerico.values())
print(soma)

#Exercício 5: Contagem de Itens Repetidos
#Dado uma lista de elementos, conte a frequência de cada elemento utilizando um dicionário.
#Exemplo:
#lista = ["maçã", "banana", "laranja", "maçã", "banana", "maçã"]
#Saída esperada: {'maçã': 3, 'banana': 2, 'laranja': 1}

lista = ["maçã", "banana", "laranja", "maçã", "banana", "maçã"]
frequencia = {}
for elemento in lista:
    frequencia[elemento] = frequencia.get(elemento, 0) + 1
print(frequencia)

#Exercício 6: Filtrando Dicionário
#Dado um dicionário contendo produtos e seus preços, filtre os produtos que custam mais de R$ 50,00.
#Exemplo:
#produtos = {"caneta": 10, "mochila": 80, "caderno": 45, "notebook": 3000}
#Saída esperada: {"mochila": 80, "notebook": 3000}

produtos={"caneta": 10, "mochila": 80, "caderno": 45, "notebook": 3000}
produtos_filtrados = {produto: preco for produto, preco in produtos.items() if preco > 50}
print(produtos_filtrados)

#Exercício 7: Tradutor Simples
#Crie um dicionário chamado 'tradutor' que contém algumas palavras em inglês como chaves e suas traduções para português como valores.
#Peça ao usuário para digitar uma palavra em inglês e exiba sua tradução, caso exista no dicionário.
#Se a palavra não estiver cadastrada, exiba "Palavra não encontrada".
tradutor = {
    "hello": "olá",
    "goodbye": "adeus",
    "thank you": "obrigado",
    "please": "por favor"
}
palavra = input("Digite uma palavra em inglês: ")
if palavra in tradutor:
    print(f"A tradução de '{palavra}' é '{tradutor[palavra]}'")
else:
    print("Palavra não encontrada")

#exercicio 8: dicionário de compras

lista_compras={"café": 70, "leite": 8, "banana_kg": 5, "pão": 3}
lista_compras.sum["queijo"] = 15
del lista_compras["pão"]
print(lista_compras)

#exercico 9: Dicionário Aninhado

turma={"Ana": {"idade": 17, "notas": [8, 9, 7]},
    "Pedro": {"idade": 18, "notas": [6, 7, 8]},
    "Mariana": {"idade": 17, "notas": [9, 10, 8]}
}
media_notas={"notas":(0+1+2)/3}

print(media_notas)

#exercicio 10: Exercício 10: Cadastro de Funcionários
#Crie um programa que permita cadastrar funcionários em uma empresa.
#O programa deve permitir adicionar funcionários com os seguintes dados:
 #- Nome
 #- Cargo
 #- Salário
#Os funcionários devem ser armazenados em um dicionário onde a chave é o nome e o valor é outro dicionário com os dados do funcionário.
#O programa deve permitir consultar funcionários pelo nome e exibir suas informações

funcionarios_empresa= {"nome": "João", "cargo": "Analista", "salário": 5000
"nome": "Maria", "cargo": "Gerente", "salário": 8000
}
#não sei como fazer isso!
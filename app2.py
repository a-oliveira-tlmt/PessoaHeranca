from Atividade import Pessoa
from datetime import date

import json

def main(args=[]):
    opcao = 1
    while opcao != 0:
        opcao = input("\n\nListar [1], Adicionar [2], Sair[0] >> ")
        try:
                pessoas = []
                
                # Leitura do Arquivo.
                f = open("pessoas.txt", 'r', encoding="utf8")

                # Parser do JSON em Objeto.
                jsonObjs = json.loads(f.read())
                
            if opcao == 1:   
                # Iteração dos elementos do JSON.
                for jsonObj in jsonObjs:
                    nome = jsonObj["nome"]
                    email = jsonObj["email"]
                    data = jsonObj["nascimento"].split("-")
                    nascimento = date(int(data[0]), int(data[1]), int(data[2]))
                    pessoa = Pessoa(nome, email, nascimento)
                    print(pessoa)
                    pessoas.append(pessoa)

            elif opcao == 2:
                
                print("Bem vindo!!")
                
                nomeNovo = input("INSIRA O SEU NOME >> ")
                emailNovo = input("INSIRA O SEU EMAIL >> ")
                nascNovo = input("INSIRA SUA DATA DE NASCIMENTO COM / >> ")
                
                pessoaNovo = Pessoa(nomeNovo, emailNovo, nascNovo)
                pessoas.append(pessoaNovo)

                pessoaNovoJson = {}
                pessoaNovoJson['nome'] = pessoaNovo.nome
                pessoaNovoJson['email'] = pessoaNovo.email
                pessoaNovoJson['nascimento'] = pessoaNovo.nascimento
                jsonObjs.append(pedroJson)

                with open('data.txt', 'w', encoding='utf-8') as f:
                    json.dump(jsonObjs, f, ensure_ascii=False, indent=4)

       except FileNotFoundError as err:
           print(err)
           print("Arquivo não encontrado!")

if __name__ == '__main__':
   main()

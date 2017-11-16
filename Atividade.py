from PessoaInterface import *
from datetime import date

class Pessoa(PessoaInterface):

    def __init__(self, nome, email, nascimento):
        self.nome = nome
        self.email = email
        self.nascimento = nascimento

    def cadastrar(self):
        print('Cadastrando Pessoa')
        #nomep = input('Digites seu nome: ')
        #emailp = input('Digite seu email: ')
        #nascimentop = input('Digite sua data de nascimento: ')

        p = Pessoa()
        p.nome = nomep
        p.email = emailp
        p.nascimento = nascimentop

        return p

    def __str__(self):
        result = '\n' +self.nome + '\n'+ self.email + '\n'+ self.nascimento
        return result

#Programar nstanciando em definição
# nasc = date(2017, 12, 13)
# \ pode usar para pular linha em py

import Pessoa
import os
def limpar():os.system('cls')

res = 0
limpar()
def pergunta():
    res = int(input("Deseja cadastrar uma nova pessoa? 1 - SIM ou 0 - NÂO: "))
    return res

cadastro = []

res = pergunta()
while(res == 1):
    nome = str(input("Insira nome do cadastrado: "))
    idade = int(input("Insira idade do cadastrado: "))
    cargo = str(input("Insira o cargo do cadastrado: "))
    salario = float(input("Insira o salário do cadastrado: "))
    
    cadastro.append(Pessoa.Pessoa(nome,idade,cargo,salario))
    res = pergunta()

def mostrar():
    print("{:<4}{:<10}{:<7}{:<10}{:<7}"
          .format("Nº","Nome","Idade","Cargo","Salário"))
    y = 1
    for x in cadastro:
        print("{:<4}{:<10}{:<7}{:<10}{:<7}"
              .format(y,
                  x.get_nome(),
                  x.get_idade(),
                  x.get_cargo(),
                  x.get_salario()
              ))
        y =+1


import re
import getpass
import time
import os

#Entrada do programa
while True:
        os.system("clear")

        print("""\033[1;31m


██████╗ ███╗   ███╗ █████╗ ██╗██╗      ██╗   ██╗ █████╗ ██╗     ██╗██████╗  █████╗ ████████╗ ██████╗ ██████╗
██╔════╝████╗ ████║██╔══██╗██║██║      ██║   ██║██╔══██╗██║     ██║██╔══██╗██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗
█████╗  ██╔████╔██║███████║██║██║█████╗██║   ██║███████║██║     ██║██║  ██║███████║   ██║   ██║   ██║██████╔╝
██╔══╝  ██║╚██╔╝██║██╔══██║██║██║╚════╝╚██╗ ██╔╝██╔══██║██║     ██║██║  ██║██╔══██║   ██║   ██║   ██║██╔══██╗
███████╗██║ ╚═╝ ██║██║  ██║██║███████╗  ╚████╔╝ ██║  ██║███████╗██║██████╔╝██║  ██║   ██║   ╚██████╔╝██║  ██║
 ╚══════╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚══════╝   ╚═══╝  ╚═╝  ╚═╝╚══════╝╚═╝╚═════╝ ╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝

                                        Versão 1.0


        \033[m""")


        print("\033[33mOBS = emails com extensão .br ainda não estão sendo aceitos!\033[m\n")

#Funcão de validação

        def validade_Email(email):
                valid = re.search(r'^[a-zA-Z0-9._-]+@[a-zA-Z0-20]+\.[a-zA-Z\.a-zA-Z]{1,3}$', email)
                return valid

# variaveis de input e verificação

        email = str(input("Email: "))
        senha = getpass.getpass("Senha: ")
        repita = getpass.getpass("Confirme sua senha: ")
        print("Conferindo email...\n")
        time.sleep(2)


        valid = validade_Email(email)

        if valid:
                print("Email válido")

        else:
                print("\033[31mERROR!\033[m Email inválido!")

        print("Conferindo senha...\n")
        time.sleep(2)

        if senha == repita:
                if valid:
                        print("Senha válida, pode entrar!\n")
                else:
                        print("\033[31mERROR!\033[m Email inválido e senha ignorada!")

        else:
                print("\033[31mERROR!\033[m Senha inserida está inválida ou desigual!")

        nov = str(input("Continuar S/N: ")).upper()[0]
        while nov.strip() not in "S" and nov.strip() not in "N":
                nov = str(input("\033[31mERROR!\033[m Continuar S/N: ")).upper()[0]

        if nov == "S":
                os.system("clear")
        elif nov == "N":
                print("Saindo...\n")
                time.sleep(1)
                break

print()
print("Você saiu!\n")

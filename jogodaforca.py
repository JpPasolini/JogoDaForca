from funcoes import limparTela
import time
while True:
    
    import os
    limparTela()
    desafiante = input("Nome do Desafiante: ")
    competidor = input("Nome do Competidor: ")
    os.system("cls")
    palavra = input("Palavra Chave: ")
    secreta = "*" * len(palavra)
    dica1 = input("Dica1: ")
    dica2 = input("Dica2: ")
    dica3 = input("Dica3: ")
    contadorDicas = 0
    totalErros = 0
    while True:
        os.system("cls")
        print("(1) Jogar")
        print("(2) Dica")
        print(f"A palavra secreta é: {secreta}")
        print(f"Total de Erros: {totalErros}")
        if totalErros == 6:
            print(f"O desafiante {desafiante} ganhou!")
            print(f"O competidor {competidor} perdeu!")
            time.sleep(2)
            break
        if "*" not in secreta:
            print(f"O competidor {competidor} ganhou!")
            print(f"O desafiante {desafiante} perdeu!")
            time.sleep(2)
            break

        opcao = input()
        
        if opcao == "1":
            tentativa = input("Informe a letra: ")
            posicao = 0
            acertou = False
            secreta = list(secreta)
            for letra in palavra:
                if letra == tentativa:
                    secreta[posicao] = letra
                    acertou = True
                posicao+=1
                
            secreta = ''.join(secreta)            
            if acertou == False:
                totalErros += 1

        elif opcao == "2":
            contadorDicas += 1
            if contadorDicas == 1:
                print(dica1)
                time.sleep(2)
            elif contadorDicas == 2:
                print(dica2)
                time.sleep(2)
            elif contadorDicas == 3:
                print(dica3)
                time.sleep(2)
            else:
                print("Você não tem mais dicas!")
                time.sleep(2)
                
        else:
            print("Opção Inválida!")
            time.sleep(2)
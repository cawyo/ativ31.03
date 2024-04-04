op = int(input("////////////\n1-Soma\n2-Subtração\n3-Multiplicação\n4-Divisão\n0-Encerrar\n////////////\nDigite a operação desejada: "))

if op == 0:
    print("Adeus...")

while op !=0:
    
    if op != 1 and op !=2 and op != 3 and op !=4 and op != 0:
        op = int(input("Digite uma operação válida: "))
        continue

    else:

        n1 = float(input("Digite o primeiro valor: "))
        n2 = float(input("Digite o segundo valor: "))

        if op == 1:
            resultado = n1+n2
            print(f"////////////\nO resultado da soma é {resultado}")
        elif op == 2:
            resultado = n1-n2
            print(f"////////////\nO resultado da subtração é {resultado}")
        elif op == 3:
            resultado = n1*n2
            print(f"////////////\nO resultado da multiplicação é {resultado}")
        else:
            resultado = n1/n2
            print(f"////////////\nO resultado da divisão é {resultado}")
        
        op = int(input("////////////\n1-Soma\n2-Subtração\n3-Multiplicação\n4-Divisão\n0-Encerrar\n////////////\nDigite a operação desejada: "))

        if op == 0:
            print("Adeus...")
            break
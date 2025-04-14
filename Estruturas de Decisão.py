
while True:
    estciv = input("Digite a letra correspondente ao seu estado civil: [C - CASADO, S - SOLTEIRO, D - DIVORCIADO, V - VIÚVO,O - OUTROS]: ").strip().upper()


    if estciv == "":
        print("Por gentileza responda uma das opções possíveis.")
    elif estciv not in ["C" , "S" , "D" , "V" , "O"]:
        print("Por gentileza responda uma das opções possíveis.")
    else:
        break
        
if estciv == "C":
    print("C - Casado")
elif estciv == "S":
    print("S - Solteiro")
elif estciv == "D":
    print("D - Divorciado")
elif estciv == "V":
    print("V - Viúvo") 
else:
    print("O - Outros")
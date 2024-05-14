while True:
    dist = input("Digite a distância: ")
    try:
        if dist.capitalize() == "Sair":
            print("Bye!")
            break
        else:
            dist = float(dist)

        if dist <= 200:
            preco = dist * 0.5
        elif (dist > 200) & (dist <= 400):
            preco = dist * 0.45
        elif dist > 400:
            preco = dist * 0.35
        print(f"O preço ficou em R${preco:.2f}")
        
    except:
        print("Valor inválido")
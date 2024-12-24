def arvore(altura):
    comprimento = altura * 2 - 1
    estrelas = 1
    for i in range(1, altura + 1):
        print(("*" * estrelas).center(comprimento))
        estrelas += 2
    print("*".center(comprimento))

arvore(9)
arvore(12)
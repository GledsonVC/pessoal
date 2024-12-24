import calendar

ano = int(input("Você deseja o calendário de que ano(YYYY): "))
mes = ''

while True:
    while True: # Loop para verificação se deseja preencher o mês
        desejo = input("Deseja informar o mês[S/N]? ").strip().upper()[0]
        if desejo in 'SN':
            break
        print('ERRO! Responda S ou N.')
    if desejo == "N":
        break
    else: # Loop para definir o mês
        while True:
            mes = int(input("Você deseja de qual mês(MM): "))
            if mes in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12):
                break
            print('ERRO! Responda um mês válido de 1 a 12.')    
        break

if mes:
    #Imprime o mês escolhido
    cal = calendar.monthcalendar(ano, mes)
    print(calendar.month_name[mes])
    print("Seg Ter Qua Qui Sex Sab Dom")
    for semana in cal:
        for dia in semana:
            if dia == 0:
                print("    ", end="")
            else:
                print(f"{dia:2d}  ", end="")
        print()
else:
    # Imprime todos os Meses do ano
    for mes in range(1,13):
            cal = calendar.monthcalendar(ano, mes)
            print(calendar.month_name[mes])
            print("Seg Ter Qua Qui Sex Sab Dom")
            for semana in cal:
                for dia in semana:
                    if dia == 0:
                        print("    ", end="")
                    else:
                        print(f"{dia:2d}  ", end="")
                print()

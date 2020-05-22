answer=0
calc=0
j=''
while True:
    while True:
        calc = input('\033[1;32mDigite o cálculo a ser feito:\n\033[m')
        if calc == 'c':
            calc=0.00
            print(calc)
        calc= str(eval(calc))
        print(f'Resposta:            \033[36m{float(calc):8f}\033[m')

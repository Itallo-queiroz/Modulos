#from cinematica import *
import cinematica as cn

while True:
    # mostrar menu na tela
    cn.mostrar_menu()

    opcao = input('\n\033[33m Opcção do usúario: \033[0m')

    match opcao:
        case '1':
            m = float(input('\n\033[33m Informe a massa em kg: \033[0m').replace(',', '.'))
            h = float(input('\033[33m Informe a altura em metros: \033[0m').replace(',', '.'))
            print(f'\n\033[33m Energia potencial: \033[0m {cn.calcular_ep(m, h)} J.')
            continue
        case '2':
            m = float(input('\n\033[33m Informe a massa em kg: \033[0m').replace(',', '.'))
            v = float(input('\033[33m Informe a velocidade em m\s: \033[0m').replace(',', '.'))
            print(f'\n\033[33mEnergia cinetica: \033[0m {cn.calcular_ec(m, v):,.2f} J.')
            continue
        case '3':
            print('\n\033[31 Programa encerrado. \033[0m')
            break
        case _:
            opcao('\n\033[31 Opção invalida. \033[0m')
            continue




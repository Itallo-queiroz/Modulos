# Menu
def mostrar_menu():
    print('\n\033[30m              MENU \n\033[0m')
    print('\033[30m 1 - Calcular energia potencial. \033[0m')
    print('\033[30m 2 - Calcular energia cinética. \033[0m')
    print('\033[30m 3 - Sair do programa. \033[0m')

def calcular_ep(m, h):
    ep = m * 9.8 * h
    return ep

def calcular_ec(m, v):
    ec = (m * (v ** 2))/2
    return ec

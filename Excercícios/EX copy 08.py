# Desenvolva um algoritmo que pergunte ao usuário o estado civil (solteiro, casado, divorciado, viúvo) e exiba uma mensagem correspondente.
estadocivil = (str(input('Qual é o seu estado civil:\n')))

match estadocivil:
    case 'solteiro':
        print('solteiro')
    case 'casado':
        print('casado')
    case 'divorciado':
        print('divorciado')
    case 'viúvo':
        print('viúvo')

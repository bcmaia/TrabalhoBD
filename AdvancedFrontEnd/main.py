import typer

from utils import Db, page



db = Db()
print(' pronto!\n\n', end='')


def noop(param : list[str]):
    pass

def hello(param : list[str]):
    print('Olá, Mundo!')

def search(param : list[str]):
    val = param[1]
    print('o valor eh ', val)
    
    # result = db.query(f'SELECT * from SITE WHERE :param1 = :param2 ;', {
    #     'param1': 'URL',
    #     'param2': val,
    # })

    result = db.query('SELECT * from SITE WHERE URL = http://inclusiotech.com;')

    print('RESULT: ')
    print(result)
    

commands = {
    'quit': { # Presente por motivos de completude
        'h': 'Finaliza a sessão.',
        'f': noop, 
    },
    'hello': {
        'h': 'Comando olá mundo :)',
        'f': hello, 
    },
    'search': {
        'h': 'Busca um site em nossa base de dados.',
        'f': search, 
    },
}





if '__main__' == __name__:
    print(
        '======================================================='
    + '\n======//  Bem-vindo ao Recursos Mínimos //============='
    + '\n======================================================='
        + '\n\n',
        end=''
    )

    print('Comandos disponíveis:')
    print('\n'.join([f'{k} \t:\t {v["h"]}' for k, v in commands.items()]))
    print('\n')

    while True:
        i = input('> ')

        params = [x for x in i.split(' ') if x]
        if not params: continue # Avoiding erros

        cmd = commands.get(params[0])

        print ('- ', end='')
        if commands['quit'] is cmd: break
        if None == cmd: 
            print('[ERRO] Comando não encontrado...\n')
            continue

        cmd['f'](params)

        print('')

    print('Finalizando sessão...\n')
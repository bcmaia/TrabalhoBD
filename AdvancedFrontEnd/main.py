import typer
from time import sleep

from services import Db, page


# DB conection
print('Conectando a base de dados... ', end='')
#db = Db()
print('Done!')



# print('\n\n')
# page.show('home')

# print('\n\nResultado de Pesquisa Exemplo:')
# print(db.query('select * from usuario'))
# print(db.query('select * from cliente'))


# db.disconnect()


def hello(name: str):
    print(f"Hello {name}")


def goodbye(name: str, formal: bool = False):
    if formal:
        print(f"Goodbye Ms. {name}. Have a good day.")
    else:
        print(f"Bye {name}!")



def test_cdm(param : list[str]):
    print('testing')

cmds = {
    'test': test_cdm
}

def main():
    i = input('> ')
    param = [x for x in i if not x]
    cmd = cmds[param[0]]

    typer.run(cmd, param)

if __name__ == "__main__":
    typer.run(main)

    
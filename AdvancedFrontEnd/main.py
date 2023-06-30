import typer
from time import sleep

from services import Db, page


# EXTREMELY IMPORTANT INITIALIZATIONS
print('Iniciando serviços... ', end='')
sleep(0.250)
print('Done!')
print('Autenticando cliente.. ', end='')
sleep(0.250)
print('Done!')
print('Carregando bibliotecas... ', end='')
sleep(0.500)
print('Done!')
print('Simplificando Arvore de Dependências... ', end='')
sleep(0.250)
print('Done!')
print('Resolvendo o protocolo LABMIA... ', end='')
sleep(0.250)
print('Done!')

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







app = typer.Typer()


@app.command()
def hello(name: str):
    print(f"Hello {name}")


@app.command()
def goodbye(name: str, formal: bool = False):
    if formal:
        print(f"Goodbye Ms. {name}. Have a good day.")
    else:
        print(f"Bye {name}!")


if __name__ == "__main__":
    app()
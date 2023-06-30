from time import sleep
from utils import Db, page

# DB conection
print('Conectando a base de dados... ', end='')
db = Db()
print('Done!\n')


page.show('home')

print('\n\nResultado de Pesquisa Exemplo:')
print(db.query('select * from usuario'))
print(db.query('select * from cliente'))



db.disconnect()





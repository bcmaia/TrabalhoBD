import os
from dotenv import load_dotenv

# IMPORTAÇÃO DAS BIBLIOTECAS NECESSÁRIAS PARA CONECTAR AO ORACLE
import oracledb
import getpass

print(oracledb.__version__)

# LEITURA DAS VARIÁVEIS DE AMBIENTE PARA BUSCAR CREDENCIAIS DA CONEXÃO
load_dotenv()
user = os.environ.get('BD_USER')
pw = os.environ.get('BD_PW')


# CONFIGURAÇÕES PARA ACESSA AO ORACLE

dsn = 'orclgrad1.icmc.usp.br/pdb_elaine.icmc.usp.br'    # ESPECIFICAÇÃO DE DSN (NÃO ALTERAR)

con = oracledb.connect(user=user, password=pw, dsn=dsn) # CONECTA-SE AO BANCO DE DADOS
print("Database version:", con.version)

# CRIAÇÃO DE UM PONTEIRO
cur = con.cursor()

# INICIANDO TRANSAÇÃO
con.begin()


cur.execute("select * from usuario")
res = cur.fetchall()
print(res)

cur.execute("select * from cliente")
res = cur.fetchall()
print(res)

# COMMITA EVENTUAIS ALTERAÇÕES PROMOVIDAS NA EXECUÇÃO DO CÓDIGO
con.commit()

# FECHA O PONTEIRO E A CONEXÃO
cur.close()
con.close()
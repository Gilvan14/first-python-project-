import sqlite3
conexao = sqlite3.connect("bancodedados.db")
c = conexao.cursor()
c.execute('''CREATE TABLE "primeiro_ano" (
	"Nome_completo"	TEXT,
	"Sexo"	TEXT,
	"Origem"	TEXT,
	"Data_de_nascimento"	TEXT,
	"Estado_atual"	TEXT,
	"Serie"	TEXT,
	"Endereco"	TEXT,
	"Nome_da_mae"	TEXT,
	"Profissao_mae"	TEXT,
	"CPF_mae"	TEXT,
	"Istrucao_mae"	TEXT,
	"Nome_pai"	TEXT,
	"Profissao_pai"	TEXT,
	"CPF_pai"	TEXT,
	"Instrucao_pai"	TEXT
);''')
conexao.commit()
conexao.close()

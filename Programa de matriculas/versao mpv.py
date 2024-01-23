import sqlite3
import pandas as pd
import tkinter as tk

#funcoes

def cadastrarr():
    #transformando as  entrys em string
    serie = entry_serie.get()
    nome = entry_nome.get()
    data = entry_data.get()
    sexo = entry_sexo.get()
    origem = entry_nasci.get()
    endereco = entry_endereco.get()
    uf = entry_uf.get()
    nomemae = entry_mae.get()
    profissaomae = entry_promae.get()
    nivelmae = entry_nimae.get()
    cpfmae = entry_cpfmae.get()
    nomepai = entry_pai.get()
    profissaopai = entry_propai.get()
    nivelpai = entry_nipai.get()
    cpfpai = entry_cpfpai.get()
    registro = entry_registro.get()

    #escholhendo a tebela
    
    conexao = sqlite3.connect("bancodedados.db")
    c = conexao.cursor()
    c.execute("INSERT INTO primeiro_ano VALUES (:nome_completo,:sexo, :origem,:data_de_nascimento,:estado_atual, :serie, :endereco, :nome_da_mae, :profissao_mae, :cpf_mae, :istrucao_mae, :nome_pai,:profissao_pai, :cpf_pai,:instrucao_pai, :registro)", 
    {'nome_completo':nome.upper(), 
    'sexo':sexo.upper(), 
    'origem':origem.upper() ,
    'data_de_nascimento':data,
    'estado_atual':uf.upper(), 
    'serie':serie, 
    'endereco':endereco.upper(), 
    'nome_da_mae':nomemae.upper(),
    'profissao_mae':profissaomae.upper(),
    'cpf_mae':cpfmae, 
    'istrucao_mae':nivelmae.upper(),
    'nome_pai':nomepai.upper(),
    'profissao_pai':profissaopai.upper(),
    'cpf_pai':cpfpai.upper(),
    'instrucao_pai':nivelpai.upper(),
    'registro':registro})
        
    conexao.commit()
    conexao.close()
        
  #deletando oq ja digitado com a funcao delete e passando os parametros da string
        
    entry_nome.delete(0,"end")
    entry_data.delete(0,"end")
    entry_sexo.delete(0,"end")
    entry_nasci.delete(0,"end")
    entry_endereco.delete(0,"end")
    entry_uf.delete(0,"end")
    entry_mae.delete(0,"end")
    entry_promae.delete(0,"end")
    entry_nimae.delete(0,"end")
    entry_cpfmae.delete(0,"end")
    entry_pai.delete(0,"end")
    entry_propai.delete(0,"end")
    entry_nipai.delete(0,"end")
    entry_cpfpai.delete(0,"end")
    entry_registro.delete(0, "end")

# interface grafica
janela = tk.Tk()
janela.title("Cadastro de Alunos")
janela.geometry("1100x700")
janela.minsize()
janela.maxsize()


#labels

class labels:
    label_nome = tk.Label(janela, text="NOME COMPLETO", font='ramabhadra 15')
    label_nome.grid(column=0, row=0, padx=10, pady=10)

    label_data = tk.Label(janela,text= "DATA DE NASCIMENTO:", font="ramabhadra 15") 
    label_data.grid(column=0, row=1, padx=10, pady=10)

    label_sexo = tk.Label(janela, text="SEXO M OU F:", font="ramabhadra 15")
    label_sexo.grid(column=2, row=0, padx=10, pady=10)

    label_nasci = tk.Label(janela, text="LOCAL DE ORIGEM:", font="ramabhadra 15")
    label_nasci.grid(column=4,row=0, padx=10, pady=10)

    label_endereço = tk.Label(janela, text="ENDEREÇO COMPLETO:", font="ramabhadra 15")
    label_endereço.grid(column=0, row=2, padx=10, pady=10)

    label_uf = tk.Label(janela, text="UF:", font="ramabhadra 15")
    label_uf.grid(column=2, row=1, padx=10, pady=10)

    label_serie = tk.Label(janela, text="SERIE:", font="ramabhadra 15")
    label_serie.grid(column=4, row=1, padx=10, pady=10)

    label_registro = tk.Label(janela, text="REGISTRO DE NASCIMENTO:", font="ramabhadra 15")
    label_registro.grid(column=2, row=2, padx=10, pady=10)

    label_mae = tk.Label (janela, text="NOME DA MAE:", font="ramabhadra 15")
    label_mae.grid(column=0, row=3, padx=10, pady=10)

    label_promae = tk.Label(janela, text="PROFISSAO MAE:", font="ramabhadra 15")
    label_promae.grid(column=2,row=3,padx=10, pady=10)

    label_nimae = tk.Label(janela, text="NIVEL DE INSTRUÇÃO MAE:", font="ramabhadra 15")
    label_nimae.grid(column=0,row=4,padx=10, pady=10)

    label_cpfmae = tk.Label(janela, text="CPF DA MAE:",font="ramabhadra 15")
    label_cpfmae.grid(column=4, row=3, padx=10, pady=10)

    label_pai = tk.Label (janela, text="NOME DO PAI:", font="ramabhadra 15")
    label_pai.grid(column=0, row=5, padx=10, pady=10)

    label_propai = tk.Label(janela, text="PROFISSAO PAI:", font="ramabhadra 15")
    label_propai.grid(column=2,row=5,padx=10, pady=10)

    label_nipai= tk.Label(janela, text="NIVEL DE INSTRUÇÃO PAI:", font="ramabhadra 15")
    label_nipai.grid(column=0,row=6,padx=10, pady=10)

    label_cpfpai = tk.Label(janela, text="CPF DO PAI:",font="ramabhadra 15")
    label_cpfpai.grid(column=4, row=5, padx=10, pady=10)

#entrys


entry_nome = tk.Entry(janela, text="a",borderwidth=5, relief="ridge")
entry_nome.grid(column=1, row=0, padx=10, pady=10, ipadx=50)
 
entry_data = tk.Entry(janela, text="b",borderwidth=5, relief="ridge")
entry_data.grid(column=1, row=1, padx=10, pady=10,columnspan=1, ipadx=50)

entry_sexo = tk.Entry(janela, text="", relief="ridge", borderwidth=5)
entry_sexo.grid(column=3, row=0, padx=10, pady=10)

entry_nasci = tk.Entry(janela, text="LOCAL DE ORIGEM:", relief="ridge", borderwidth=5)
entry_nasci.grid(column=5,row=0, padx=10, pady=10)

entry_endereco = tk.Entry (janela, text="f",borderwidth=5, relief="ridge")
entry_endereco.grid(column=1, row=2, padx=10, pady=10,ipadx=50)

entry_uf = tk.Entry(janela, text="", relief="ridge", borderwidth=5)
entry_uf.grid(column=3, row=1, padx=10, pady=10)

entry_serie = tk.Entry(janela, text="", relief="ridge", borderwidth=5)
entry_serie.grid(column=5, row=1, padx=10, pady=10)

entry_registro = tk.Entry(janela, text="", relief="ridge", borderwidth=5)
entry_registro.grid(column=3, row=2,padx=10, pady=10, ipadx=188, columnspan=100)

entry_mae = tk.Entry(janela, text="", relief="ridge", borderwidth=5)
entry_mae.grid(column=1, row=3, padx=10, pady=10, ipadx=50)

entry_promae = tk.Entry(janela, text="", relief="ridge", borderwidth=5)
entry_promae.grid(column=3,row=3,padx=10, pady=10)

entry_cpfmae = tk.Entry(janela, text="CPF DA MAE:", relief="ridge", borderwidth=5)
entry_cpfmae.grid(column=5, row=3, padx=10, pady=10)

entry_nimae = tk.Entry(janela, text="", relief="ridge", borderwidth=5)
entry_nimae.grid(column=1, row=4, padx=10, pady=10, ipadx=50)

entry_pai = tk.Entry(janela, text="", relief="ridge", borderwidth=5)
entry_pai.grid(column=1, row=5, padx=10, pady=10, ipadx=50)

entry_propai = tk.Entry(janela, text="", relief="ridge", borderwidth=5)
entry_propai.grid(column=3,row=5,padx=10, pady=10)

entry_cpfpai = tk.Entry(janela, text="CPF DO PAI:", relief="ridge", borderwidth=5)
entry_cpfpai.grid(column=5, row=5, padx=10, pady=10)

entry_nipai = tk.Entry(janela, text="", relief="ridge", borderwidth=5)
entry_nipai.grid(column=1, row=6, padx=10, pady=10, ipadx=50)
    

#botoes
class botes:
    botao_cadastrar = tk.Button(janela, text="CADASTRAR", command=cadastrarr, borderwidth=5, relief="raised")
    botao_cadastrar.grid (column=2, row=7, padx=10, pady=10, ipadx=100, columnspan=100)

janela.mainloop()

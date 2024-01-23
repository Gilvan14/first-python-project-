import customtkinter as ctk 
import sqlite3
import pandas as pd
import tkinter as tk

#cirando a tela
tela = ctk.CTk()
tela.title("Cadastro de alunos - Versão BETA 1.0")
tela.geometry("1100x700")

tela.maxsize(1100,700)
tela._apply_appearance_mode("system")

#definindo fontes

fonte = ctk.CTkFont(family="waree", size=15)
fonte2 = ctk.CTkFont(family="dyuthi", size =15)

#magens

imagem =tk.PhotoImage(file="logobaden.png").subsample(9,9)

#nova janela

janela = ctk.CTkFrame(tela, fg_color="#808080", border_color="black", border_width=3, corner_radius=10)
janela.place(x=0,y=0)

#funcoes dos botoes


def declaracoes():
    janelad = ctk.CTk()
    janelad.geometry("1000x600")

def cadastrar():
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
    
    conexao = sqlite3.connect("bancodedados.odb")
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
    entry_uf.delete(0, "end")
    entry_mae.delete(0,"end")
    entry_promae.delete(0,"end")
    entry_nimae.delete(0,"end")
    entry_cpfmae.delete(0,"end")
    entry_pai.delete(0,"end")
    entry_propai.delete(0,"end")
    entry_nipai.delete(0,"end")
    entry_cpfpai.delete(0,"end")
    entry_registro.delete(0, "end")


class labels(): 

    imagem = ctk.CTkLabel(janela, image=imagem, text="").grid(column=0, row=0, padx=2, pady=2)

    label_nome = ctk.CTkLabel(janela, text="NOME COMPLETO:", font=fonte2, text_color="black")
    label_nome.grid(column=1, row=0, padx=10, pady=10)
    
    label_data = ctk.CTkLabel(janela,text= "DATA DE NASCIMENTO:", font=fonte2, text_color="black") 
    label_data.grid(column=1, row=1, padx=10, pady=10)

    label_sexo = ctk.CTkLabel(janela, text="SEXO M OU F:",font=fonte2, text_color="black")
    label_sexo.grid(column=3, row=0, padx=10, pady=10)

    label_nasci = ctk.CTkLabel(janela, text="LOCAL DE ORIGEM:", font=fonte2, text_color="black")
    label_nasci.grid(column=5,row=0, padx=10, pady=10)

    label_endereço = ctk.CTkLabel(janela, text="ENDEREÇO COMPLETO:", font=fonte2, text_color="black")
    label_endereço.grid(column=1, row=2, padx=10, pady=10)

    label_uf = ctk.CTkLabel(janela, text="UF:", font=fonte2, text_color="black")
    label_uf.grid(column=5, row=1, padx=10, pady=10)

    label_serie = ctk.CTkLabel(janela, text="SERIE:", font=fonte2, text_color="black")
    label_serie.grid(column=3, row=1, padx=10, pady=10)

    label_registro = ctk.CTkLabel(janela, text="REGISTRO DE NASCIMENTO:", font=fonte2, text_color="black")
    label_registro.grid(column=3, row=2, padx=10, pady=10)

    label_mae = ctk.CTkLabel(janela, text="NOME DA MAE:", font=fonte2, text_color="black")
    label_mae.grid(column=1, row=3, padx=10, pady=10)

    label_promae = ctk.CTkLabel(janela, text="PROFISSAO MAE:", font=fonte2, text_color="black")
    label_promae.grid(column=3,row=3,padx=10, pady=10)

    label_nimae = ctk.CTkLabel(janela, text="NIVEL DE INSTRUÇÃO MAE:", font=fonte2, text_color="black")
    label_nimae.grid(column=1,row=4,padx=10, pady=10)

    label_cpfmae = ctk.CTkLabel(janela, text="CPF DA MAE:", font=fonte2, text_color="black")
    label_cpfmae.grid(column=5, row=3, padx=10, pady=10)

    label_pai = ctk.CTkLabel (janela, text="NOME DO PAI:", font=fonte2, text_color="black")
    label_pai.grid(column=1, row=5, padx=10, pady=10)

    label_propai = ctk.CTkLabel(janela, text="PROFISSAO PAI:", font=fonte2, text_color="black")
    label_propai.grid(column=3,row=5,padx=10, pady=10)

    label_nipai= ctk.CTkLabel(janela, text="NIVEL DE INSTRUÇÃO PAI:", font=fonte2, text_color="black")
    label_nipai.grid(column=1,row=6,padx=10, pady=10)

    label_cpfpai = ctk.CTkLabel(janela, text="CPF DO PAI:",font=fonte2, text_color="black")
    label_cpfpai.grid(column=5, row=5, padx=10, pady=10)
# entrys

entry_nome = ctk.CTkEntry(janela, corner_radius=10, border_color="black", fg_color="#ccccff", text_color="black")
entry_nome.grid(column=2, row=0, padx=10, pady=10, ipadx=50)

entry_data = ctk.CTkEntry(janela, corner_radius=10, border_color="black", fg_color="#ccccff", text_color="black")
entry_data.grid(column=2, row=1, padx=10, pady=10, ipadx=50)

entry_sexo = ctk.CTkEntry(janela, corner_radius=10, border_color="black", fg_color="#ccccff", text_color="black")
entry_sexo.grid(column=4, row=0, padx=10, pady=10, ipadx=10)

entry_nasci = ctk.CTkEntry(janela, corner_radius=10, border_color="black", fg_color="#ccccff", text_color="black")
entry_nasci.grid(column=6, row=0, padx=10, pady=10, ipadx=10)

entry_endereco = ctk.CTkEntry(janela, corner_radius=10, border_color="black", fg_color="#ccccff", text_color="black")
entry_endereco.grid(column=2, row=2, padx=10, pady=10, ipadx=50)

entry_uf = ctk.CTkEntry(janela, corner_radius=10, border_color="black", fg_color="#ccccff", text_color="black")
entry_uf.grid(column=4, row=1, padx=10, pady=10, ipadx=10)

entry_serie = ctk.CTkEntry(janela, corner_radius=10, border_color="black", fg_color="#ccccff", text_color="black")
entry_serie.grid(column=6, row=1, padx=10, pady=10, ipadx=10)

entry_registro = ctk.CTkEntry(janela, corner_radius=10, border_color="black", fg_color="#ccccff", text_color="black")
entry_registro.grid(column=4, row=2, padx=10, pady=10, ipadx=50)

entry_mae = ctk.CTkEntry(janela, corner_radius=10, border_color="black", fg_color="#ccccff", text_color="black")
entry_mae.grid(column=2, row=3, padx=10, pady=10, ipadx=50)

entry_promae = ctk.CTkEntry(janela, corner_radius=10, border_color="black", fg_color="#ccccff", text_color="black")
entry_promae.grid(column=4, row=3, padx=10, pady=10, ipadx=50)

entry_nimae = ctk.CTkEntry(janela, corner_radius=10, border_color="black", fg_color="#ccccff", text_color="black")
entry_nimae.grid(column=2, row=4, padx=10, pady=10, ipadx=50)

entry_cpfmae = ctk.CTkEntry(janela, corner_radius=10, border_color="black", fg_color="#ccccff", text_color="black")
entry_cpfmae.grid(column=6, row=3, padx=10, pady=10, ipadx=30)

entry_pai = ctk.CTkEntry(janela, corner_radius=10, border_color="black", fg_color="#ccccff", text_color="black")
entry_pai.grid(column=2, row=5, padx=10, pady=10, ipadx=50)

entry_propai = ctk.CTkEntry(janela, corner_radius=10, border_color="black", fg_color="#ccccff", text_color="black")
entry_propai.grid(column=4, row=5, padx=10, pady=10, ipadx=50)

entry_nipai = ctk.CTkEntry(janela, corner_radius=10, border_color="black", fg_color="#ccccff", text_color="black")
entry_nipai.grid(column=2, row=6, padx=10, pady=10, ipadx=50)

entry_cpfpai = ctk.CTkEntry(janela, corner_radius=10, border_color="black", fg_color="#ccccff", text_color="black")
entry_cpfpai.grid(column=6, row=5, padx=10, pady=10, ipadx=30)




#botoes
botao_declaracoes = ctk.CTkButton(janela, text="DECLARAÇÕES", corner_radius=7,anchor="CENTER" , font= fonte, command=declaracoes)
#botao_declaracoes.grid(column=3, row=7, pady=10, padx=10)

botao_cadastrar = ctk.CTkButton(janela, text="REGISTRAR", corner_radius=15 , font= fonte, command=cadastrar, width=20).grid(column=1, row=7, padx=10, pady=10)





tela.mainloop()

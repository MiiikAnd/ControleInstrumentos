import psycopg2
from tkinter import *

def salvar_produto(codigo, descricao):
    try:
        connection = psycopg2.connect(
            database="your_database",
            user="your_username",
            password="your_password",
            host="127.0.0.1",
            port="5432"
        )
        cursor = connection.cursor()
        postgres_insert_query = """ INSERT INTO produtos (codigo, descricao) VALUES (%s,%s)"""
        record_to_insert = (codigo, descricao)
        cursor.execute(postgres_insert_query, record_to_insert)
        connection.commit()
        print("Produto salvo com sucesso!")
    except (Exception, psycopg2.Error) as error:
        print("Erro ao conectar ao PostgreSQL", error)
    finally:
        if connection:
            cursor.close()
            connection.close()

def salvar():
    codigo = codigo_entry.get()
    descricao = descricao_entry.get()
    salvar_produto(codigo, descricao)

root = Tk()

Label(root, text="Código do Produto").grid(row=0)
Label(root, text="Descrição do Produto").grid(row=1)

codigo_entry = Entry(root)
descricao_entry = Entry(root)

codigo_entry.grid(row=0, column=1)
descricao_entry.grid(row=1, column=1)

Button(root, text='Salvar', command=salvar).grid(row=3, column=1, sticky=W, pady=4)

root.title("Cadastro de mateirias")
root.geometry("500x500")
mainloop()

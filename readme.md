# Cadastro de Clientes com Streamlit

Este aplicativo permite o cadastro de clientes, armazenando as informações em arquivos JSON e CSV. Isso torna a estrutura flexível, adequada tanto para aplicações web quanto para análise de dados.

## Funcionalidades

- **Entrada de Dados**: O usuário pode inserir seu nome, endereço, data de nascimento e tipo de cliente.
- **Armazenamento**: Os dados são salvos em um arquivo `clientes.json` e um arquivo CSV `cliente.csv`.
- **Validação**: O sistema verifica se o cliente já está cadastrado antes de adicionar.

## Como Usar
1- Execute o aplicativo Streamlit.
2- Preencha os campos obrigatórios.
3- Clique em “Enviar” para cadastrar o cliente.

## Código

``` python
import streamlit as st
from datetime import datetime
import json
import os
import time
from streamlit import rerun

st.title("Cadastro de Clientes")

# Campos de entrada
if 'nome' not in st.session_state:
    st.session_state.nome = ""
if 'endereco' not in st.session_state:
    st.session_state.endereco = ""

st.session_state.nome = st.text_input("Digite seu nome:", value=st.session_state.nome)
st.session_state.endereco = st.text_input("Endereço:", value=st.session_state.endereco)
data_formatada = "DD/MM/YYYY"
ano_nascimento = st.date_input("Data de Nascimento:", value=datetime.today(), format=data_formatada).strftime("%d/%m/%Y")
tipo_cliente = st.selectbox("Tipo do Cliente", ["Pessoa Física", "Pessoa Jurídica"])

botao_cadastro = st.button("Enviar")

if botao_cadastro:
    cliente = {
        "Nome": st.session_state.nome,
        "Endereço": st.session_state.endereco,
        "Data de Nascimento": ano_nascimento,
        "Tipo do Cliente": tipo_cliente
    }
    
    if not os.path.isfile("clientes.json"):
        with open("clientes.json", "w", encoding="utf-8-sig") as arquivo:
            json.dump([], arquivo)
        with open("cliente.csv", "w", encoding="utf-8-sig") as arquivocsv:
            arquivocsv.write("Nome;Endereço;Data de Nascimento;Tipo do Cliente\n")
    
    with open("clientes.json", "r+", encoding="utf-8-sig") as arquivo:
        dados_existentes = json.load(arquivo)
        cliente_existente = any(
            c["Nome"] == cliente["Nome"] and 
            c["Endereço"] == cliente["Endereço"] and 
            c["Data de Nascimento"] == cliente["Data de Nascimento"] 
            for c in dados_existentes
        )
        
        if not cliente_existente:
            dados_existentes.append(cliente)
            arquivo.seek(0)
            json.dump(dados_existentes, arquivo, ensure_ascii=False, indent=4)
            
            with open("cliente.csv", "a", encoding="utf-8-sig") as arquivocsv:
                arquivocsv.write(';'.join([st.session_state.nome, st.session_state.endereco, ano_nascimento, tipo_cliente]) + "\n")
            mensagem = st.empty()
            mensagem.success("Cliente Cadastrado com Sucesso!")
            time.sleep(2)
            mensagem.empty()
            
        else:
            mensagem = st.empty()
            mensagem.error("Cadastro já existe")
            time.sleep(2)
            mensagem.empty()
    time.sleep(2)
    st.session_state.nome = ""  # Limpa o nome
    st.session_state.endereco = ""  # Limpa o nome
    st.rerun()

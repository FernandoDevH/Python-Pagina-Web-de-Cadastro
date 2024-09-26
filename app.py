import streamlit as st
from datetime import datetime
import time
import json
import os

st.title("Cadastro de Clientes")

# Campos de entrada
nome = st.text_input("Digite seu nome:")  # Campo para o nome do cliente
endereco = st.text_input("Endereço:")  # Campo para o endereço do cliente
data_formatada = "DD/MM/YYYY"
ano_nascimento = st.date_input("Data de Nascimento:", value=datetime.today(), format=data_formatada).strftime("%d/%m/%Y")  # Campo para a data de nascimento
tipo_cliente = st.selectbox("Tipo do Cliente", ["Pessoa Física", "Pessoa Jurídica"])  # Seleção do tipo de cliente

botao_cadastro = st.button("Enviar")  # Botão para enviar os dados

if botao_cadastro:  # Verifica se o botão foi clicado
    # Criar um objeto com os dados do cliente
    cliente = {
        "Nome": nome,
        "Endereço": endereco,
        "Data de Nascimento": str(ano_nascimento),
        "Tipo do Cliente": tipo_cliente
    }
    
    # Verifica se o arquivo JSON já existe
    if not os.path.isfile("clientes.json"):  # Se o arquivo "clientes.json" não existir
        # Se não existir, cria uma lista vazia
        with open("clientes.json", "w", encoding="utf-8-sig") as arquivo:
            json.dump([], arquivo)  # Cria um arquivo JSON vazio

    # Lê os dados existentes do arquivo JSON
    with open("clientes.json", "r+", encoding="utf-8-sig") as arquivo:
        dados_existentes = json.load(arquivo)  # Carrega os dados existentes do arquivo JSON
        dados_existentes.append(cliente)  # Adiciona o novo cliente à lista de dados existentes
        arquivo.seek(0)  # Move o cursor para o início do arquivo para sobrescrever
        json.dump(dados_existentes, arquivo, ensure_ascii=False, indent=4)  # Salva os dados com indentação para melhor legibilidade

    # Salvar os dados em um arquivo CSV
    # Salvar os dados em um arquivo CSV
# Verifica se o arquivo já existe para não repetir os cabeçalhos
    if not os.path.isfile("cliente.csv"):  # Se o arquivo não existir
     with open("cliente.csv", "w", encoding="utf-8-sig") as arquivo:
        # Escreve os cabeçalhos das colunas
        arquivo.write("Nome;Endereço;Data de Nascimento;Tipo do Cliente\n")

# Adiciona os dados do cliente
    with open("cliente.csv", "a", encoding="utf-8-sig") as arquivo:
    # Escreve os dados do cliente em uma nova linha
        arquivo.write(';'.join([nome, endereco, ano_nascimento, tipo_cliente]) + "\n")

    # Mensagem de sucesso
    mensagem_sucesso = st.empty()  # Cria um espaço vazio para a mensagem
    mensagem_sucesso.success("Cliente Cadastrado com Sucesso!")  # Exibe a mensagem de sucesso
    time.sleep(3)  # Espera de 3 segundos
    mensagem_sucesso.empty()  # Limpa a mensagem de sucesso
    nome = ""
    endereco = ""
    ano_nascimento = datetime.today()  # Reseta a data de nascimento para a data atual
    tipo_cliente = "Pessoa Física"  # Reseta o tipo de cliente para o padrão

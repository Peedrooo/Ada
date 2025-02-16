import json
import os
import unicodedata

import pandas as pd
from IPython.display import display

# Verifica diretório atual
print("Diretório atual:", os.getcwd())

# Função para remover acentos
def remover_acentos(texto):
    if isinstance(texto, str):
        texto = unicodedata.normalize('NFKD', texto)  
        return ''.join(c for c in texto if not unicodedata.combining(c))  
    return texto 

def extract_discipline(curso):
    # Caminho absoluto do arquivo
    caminho_arquivo = os.path.abspath("src/data/grade_fga.xlsx")
    print("Tentando abrir:", caminho_arquivo)

    # Carregar o arquivo Excel em um DataFrame
    df = pd.read_excel(caminho_arquivo, sheet_name="ListaOferta3", engine="openpyxl")
    df = df.applymap(remover_acentos)
    df_discipline = df[df["CURSO RESPONSAVEL"] == curso]
    df_discipline = df_discipline.drop_duplicates(subset=["DISCIPLINA"])
    df_ordenado = df_discipline.sort_values(by="FLUXO")
    return df_ordenado

def extract_all_discipline():
    # Caminho absoluto do arquivo
    caminho_arquivo = os.path.abspath("src/data/grade_fga.xlsx")
    print("Tentando abrir:", caminho_arquivo)

    # Carregar o arquivo Excel em um DataFrame
    df = pd.read_excel(caminho_arquivo, sheet_name="ListaOferta3", engine="openpyxl")
    df = df.applymap(remover_acentos)
    # df_discipline = df[df["CURSO RESPONSAVEL"] in ['Software', 'Ciencias Naturais Aplicadas',\
    #                                                 'Aeroespacial', 'Automotiva', 'Eletronica', 'Energia']]
    df_discipline = df.drop_duplicates(subset=["DISCIPLINA"])
    df_ordenado = df_discipline.sort_values(by="FLUXO")
    return df_ordenado

def convert_json(df):
    df = df.drop(df.columns[[1] + list(range(3, 11)) + list(range(12, 14))], axis=1)
    df = df.rename(columns={'DISCIPLINA': 'name', 'FLUXO': 'flow', 'CURSO RESPONSAVEL': 'course'})
    
    # Converte fluxo para inteiro
    df['flow'] = df['flow'].fillna(0).astype(int)
    df = df.assign(type='comum')
    df = df.assign(workload=60)
    
    display(df)

    # Converte dataframe para json 
    json_output = json.dumps(df.to_dict(orient="records"), indent=2, ensure_ascii=False)
    with open('json_output.txt', 'w') as f:
        f.write(json_output)

if __name__ == "__main__":
    # df = pd.DataFrame()
    dataFrame = extract_all_discipline()
    convert_json(dataFrame)
    
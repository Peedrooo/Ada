import pandas as pd
import os

# Verifica diretório atual
print("Diretório atual:", os.getcwd())

# Caminho absoluto do arquivo
caminho_arquivo = os.path.abspath("src/data/grade_fga.xlsx")
print("Tentando abrir:", caminho_arquivo)

# Carregar o arquivo Excel em um DataFrame
df = pd.read_excel(caminho_arquivo, sheet_name="ListaOferta3", engine="openpyxl")

df_software = df[df["CURSO RESPONSAVEL"] == "Software"]
df_software = df_software.drop_duplicates(subset=["DISCIPLINA"])
df_ordenado = df_software.sort_values(by="FLUXO")
print(df_ordenado)
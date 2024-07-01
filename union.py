import os
import pandas as pd
import xlsxwriter

# Defina o caminho da pasta que contém as planilhas coletadas para serem unificadas
pasta_entrada = 'C:/Projetos/LISTAS_PRESENCA/2023/_COLETA/'
# Defina o caminho e nome do arquivo onde ser gravado o resultado final unificado
arquivo_saida = 'C:/Projetos/LISTAS_PRESENCA/2023/_RESULTADO/RES_LISTAS_PRESENCA_2023.xlsx'

# Lista para armazenar os DataFrames de cada planilha
planilhas = []

# Percorre todos os arquivos da pasta
for arquivo in os.listdir(pasta_entrada):
    # Verifica se o arquivo é um arquivo Excel
    if arquivo.endswith('.xlsx') or arquivo.endswith('.xls'):
        # Cria o caminho completo do arquivo
        caminho_arquivo = os.path.join(pasta_entrada, arquivo)
        # Lê a planilha e adiciona ao DataFrame
        df = pd.read_excel(caminho_arquivo)
        # Adiciona o DataFrame à lista
        planilhas.append(df)

# Concatena todas as planilhas em um único DataFrame
df_unificado = pd.concat(planilhas, ignore_index=True)

# Converte o dataframe como texto
df_unificado = df_unificado.astype(str)

# Salva o DataFrame unificado em um novo arquivo Excel
df_unificado.to_excel(arquivo_saida, sheet_name='Resultado Coleta', index=False, header=True,  engine='xlsxwriter',
                        engine_kwargs={'options': {'strings_to_numbers': False}})

print(f'As planilhas forma unificadas no arquivo: {arquivo_saida}')
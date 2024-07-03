# pip install pandas
# pip install openpyxl

import pandas as pd
import os

# PARÂMETROS

# Coluna para especificar o programa (Usualmente o nome da pasta disponibilizada)
coluna_programa = 'Semana ENEF 2024 - [Portfólio do Instituto Sicoob] Se Liga Finanças - Workshop - Finanças Pessoais'
# Definir o diretório onde estão as planilhas (usa as barras invertidas /)
diretorio_planilhas = 'C:/Projetos/LISTAS_PRESENCA/01062024a30062024/Semana ENEF 2024/[Portfólio do Instituto Sicoob] Se Liga Finanças - Workshop - Finanças Pessoais/'
# Definir o diretório onde será salvo o resultado coletado de cada programa (usa as barras invertidas /)
diretorio_coleta = 'C:/Projetos/LISTAS_PRESENCA/01062024a30062024/_COLETA/'


# Função para tratar o CPF para a coluna CPF_TRATADO
def tratar_cpf(cpf):
    # Remover espaços, pontos e traços
    cpf_tratado = ''.join(filter(str.isdigit, str(cpf)))
    # Preencher com zeros à esquerda até 11 caracteres
    cpf_tratado = cpf_tratado.zfill(11)
    return cpf_tratado

# Função para ler as planilhas e extrair a coluna CPF
def extrair_cpfs(diretorio):
    # Lista para armazenar os dados
    dados = []

    # Iterar sobre todos os arquivos no diretório
    for arquivo in os.listdir(diretorio):
        if arquivo.endswith('.xlsx'):
            # Caminho completo do arquivo
            caminho_arquivo = os.path.join(diretorio, arquivo)
            
            try:    
                # Ler a planilha
                planilha = pd.read_excel(caminho_arquivo)
                
                # Verificar se a coluna "CPF" ou "CPF/CNPJ" existe
                if 'CPF' in planilha.columns:
                    coluna = 'CPF'
                elif 'CPF/CNPJ' in planilha.columns:
                    coluna = 'CPF/CNPJ'
                else:
                    coluna = None
                
                # Se uma das colunas existir, extrair os CPFs
                if coluna:
                    cpfs = planilha[coluna].dropna().tolist()
                    
                    # Adicionar os dados na lista
                    for cpf in cpfs:
                        dados.append({
                            'Nome do arquivo': arquivo, 
                            'COOP': arquivo[:4],
                            'Programa': coluna_programa, 
                            'CPF': cpf,
                            'CPF_TRATADO': tratar_cpf(cpf)
                            })
            except Exception as e:
                # Imprimir o erro e o nome do arquivo
                print(f"Erro ao ler o arquivo {arquivo}: {e}")

    # Criar um DataFrame com os dados
    df = pd.DataFrame(dados)
    
    return df

# Chamar a função e gerar o DataFrame
df_cpfs = extrair_cpfs(diretorio_planilhas)

# Exibir o DataFrame
#print(df_cpfs)

# Para salvar o DataFrame em um arquivo Excel ou CSV
df_cpfs.to_excel(diretorio_coleta+'CPF_'+coluna_programa+'.xlsx', index=False)
# ou
# df_cpfs.to_csv('COLETA/CPF_'+coluna_programa+'.csv', index=False)
import pandas as pd
from validate_docbr import CPF


# Definir o caminho para a planilha
caminho_planilha = 'C:/Projetos/LISTAS_PRESENCA/01.09.2024a31.09.2024/_RESULTADO/RES_LISTAS_PRESENCA_01.09.2024a31.09.2024.xlsx'


# Função para verificar se o CPF é válido
def cpf_valido(cpf):
    cpf_obj = CPF()
    return cpf_obj.validate(cpf)


# Ler a planilha
df = pd.read_excel(caminho_planilha)

# Verificar se a coluna CPF_TRATADO existe
if 'CPF_TRATADO' in df.columns:
    # Validar os CPFs e adicionar a nova coluna
    df['CPF_VALIDO'] = df['CPF_TRATADO'].apply(cpf_valido)

    # Exibir o DataFrame resultante
    print(df)

    # Se quiser salvar o DataFrame em um arquivo Excel ou CSV
    df.to_excel('C:/Projetos/LISTAS_PRESENCA/01.09.2024a31.09.2024/_RESULTADO/RES_LISTAS_PRESENCA_2024-09_com_CPFS_Validados.xlsx', index=False)

else:
    print("A coluna 'CPF_TRATADO' não foi encontrada na planilha.")

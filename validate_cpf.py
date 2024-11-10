import pandas as pd
from validate_docbr import CPF

# Definir o caminho para a planilha após unificá-las (union.py)
planilha_unificada = 'C:/Projetos/LISTAS_PRESENCA/01.10.2024 a 31.10.2024/_RESULTADO/UNIAO_LISTAS_PRESENCA_01.10.2024_a_31.10.2024.xlsx'
# Definir o caminho para a planilha resultado fina (com a validação dos CPF)
planilha_resultado = 'C:/Projetos/LISTAS_PRESENCA/01.10.2024 a 31.10.2024/_RESULTADO/RES_LISTAS_PRESENCA_2024-10_com_CPFS_Validados_BKP.xlsx'

# Função para verificar se o CPF é válido
def cpf_valido(cpf):
    cpf_obj = CPF()
    return cpf_obj.validate(cpf)

# Ler a planilha
df = pd.read_excel(planilha_unificada)

# Verificar se a coluna CPF_TRATADO existe
if 'CPF_TRATADO' in df.columns:
    # Validar os CPFs e adicionar a nova coluna
    df['CPF_VALIDO'] = df['CPF_TRATADO'].apply(cpf_valido)

    # Exibir o DataFrame resultante
    print(df)

    # Se quiser salvar o DataFrame em um arquivo Excel ou CSV
    df.to_excel(planilha_resultado, index=False)

else:
    print("A coluna 'CPF_TRATADO' não foi encontrada na planilha.")

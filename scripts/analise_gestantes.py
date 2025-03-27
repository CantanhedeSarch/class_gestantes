import pandas as pd

file_path = 'C:/Users/Lúcia/class_gestantes/class_gestantes/dados/Banco_Geral_Gestantes.xlsx'

df = pd.read_excel(file_path)

print(df)

def classificar_atalah(imc_atual):
    if imc_atual < 18.5:
        return "Baixo Peso"
    elif 18.5 <= imc_atual < 25.0:
        return "Adequado"
    elif 25.0 <= imc_atual < 30.0:
        return "Sobrepeso"
    else:
        return "Obesidade"

df['Classificação Atalah'] = df['IMC_ATUAL'].apply(classificar_atalah)

print(df[['NOME DA GESTANTE', 'IMC_ATUAL', 'Classificação Atalah']])

df.to_excel('C:/Users/Lúcia/class_gestantes/class_gestantes/dados/gestantes_classificacao_atalah.xlsx', index=False)
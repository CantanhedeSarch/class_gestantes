### **Análise de Perfil Gestacional com Python (Metodologia de Atalah)**

Este é o meu passo a passo para configurar o ambiente Python, carregar dados de uma planilha Excel e realizar a análise gestacional com base na metodologia de Atalah.

---

### **1. Pré-requisitos**

Antes de começar, eu preciso garantir que tenho os seguintes itens instalados:

- **Python 3.x**: [Baixar Python](https://www.python.org/downloads/)
- **pip**: O gerenciador de pacotes para Python (normalmente já vem com o Python).

---

### **2. Instalando as Bibliotecas Necessárias**

Eu vou precisar das bibliotecas `pandas` para manipular dados e `openpyxl` para lidar com arquivos Excel.

### Passo 1: Instalar Pandas e Openpyxl

No terminal (ou prompt de comando no Windows), eu executo os seguintes comandos:

```bash
pip install pandas openpyxl
```

---

### **3. Criando um Ambiente Virtual (Opcional)**

Criar um ambiente virtual ajuda a isolar as dependências do meu projeto. Aqui está como faço isso:

### Passo 1: Criar o Ambiente

No terminal, eu executo:

```bash

python -m venv nome_do_ambiente

```

### Passo 2: Ativar o Ambiente

- No **Windows**:
    
    ```bash
    
    nome_do_ambiente\Scripts\activate
    ```
    
- No **Linux/Mac**:
    
    ```bash
    
    source nome_do_ambiente/bin/activate
    ```
    

Agora, o meu ambiente virtual está ativado.

---

### **4. Carregando e Visualizando os Dados**

Com o ambiente preparado e as bibliotecas instaladas, vou carregar a planilha com o pandas.

### Passo 1: Carregar a Planilha Excel

No meu código Python, eu importo o `pandas` e carrego a planilha:

```python

import pandas as 
file_path = 'caminho/para/sua/planilha.xlsx'
df = pd.read_excel(file_path)

```

### Passo 2: Visualizar os Dados

Eu vejo uma prévia dos dados para entender sua estrutura:

```python

print(df.head())

```

---

### **5. Aplicando a Metodologia de Atalah**

Agora, vou criar uma função para classificar o IMC de acordo com a metodologia de Atalah e aplicá-la aos meus dados.

### Passo 1: Definir a Função de Classificação

Eu uso a função abaixo para classificar o IMC pré-gestacional:

```python

def classificar_atalah(imc_pre):
    if imc_pre < 18.5:
        return "Baixo Peso"
    elif 18.5 <= imc_pre <= 24.9:
        return "Adequado"
    elif 25.0 <= imc_pre <= 29.9:
        return "Sobrepeso"
    else:
        return "Obesidade"
```

### Passo 2: Aplicar a Função aos Dados

Agora, aplico a função para classificar o IMC de cada gestante:

```python

df['Classificação Atalah'] = df['IMC_ATUAL'].apply(classificar_atalah)

```

---

### **6. Visualizando e Salvando o Resultado**

Eu vejo as primeiras linhas para conferir as classificações:

```python

print(df[['NOME DA GESTANTE', 'IMC_ATUAL', 'Classificação Atalah']])

```

Se eu quiser salvar o resultado em um novo arquivo Excel, faço o seguinte:

```python

df.to_excel('C:/Users/Lúcia/analise-gestantes/dados/gestantes_classificacao_atalah.xlsx', index=False)

```

---

### **Resumo dos Comandos**

1. Instalo as bibliotecas:
    
    ```bash
    
    pip install pandas openpyxl
    
    ```
    
2. Carrego e visualizo a planilha:
    
    ```python
    
    import pandas as pd
    df = pd.read_excel('sua_planilha.xlsx')
    print(df.head())
    
    ```
    
3. Defino e aplico a classificação:
    
    ```python
    
    def classificar_atalah(imc_pre):
        if imc_pre < 18.5:
            return "Baixo Peso"
        elif 18.5 <= imc_pre <= 24.9:
            return "Adequado"
        elif 25.0 <= imc_pre <= 29.9:
            return "Sobrepeso"
        else:
            return "Obesidade"
    df['Classificação Atalah'] = df['IMC_ATUAL'].apply(classificar_atalah)
    print(df[['NOME DA GESTANTE', 'IMC_ATUAL', 'Classificação Atalah']])
    
    ```
    
4. Salvo o resultado:
    
    ```python
    
    df.to_excel('C:/Users/Lúcia/analise-gestantes/dados/gestantes_classificacao_atalah.xlsx', index=False)
    
    ```

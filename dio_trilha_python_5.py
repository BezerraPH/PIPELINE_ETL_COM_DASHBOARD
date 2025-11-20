# Esse script realiza um processo ETL (Extract, Transform, Load) em um conjunto de dados de vendas do Xbox Game Pass.
# Ele carrega os dados de um arquivo CSV, limpa e transforma os dados, e salva o resultado em um novo arquivo JSON.

# bibliotecas necessárias para realizar a transformação dos dados
import pandas as pd
import numpy as np
import unidecode

# --- FUNÇÃO DE SIMULAÇÃO LLM ---
def generate_llm_message_placeholder(name):
    """
    Simula a geração de uma mensagem de marketing personalizada por um LLM.
    
    A persona solicitada: 'Você é um especialista em markting de jogos.'
    O conteúdo: 'Crie uma mensagem sobre os jogos que você precisa jogar antes de morrer.'
    Restrição: Máximo de 100 caracteres.
    """
    games = "Halo Infinite, Forza Horizon 5, Minecraft"
    # Cria uma mensagem que simula a persona e o conteúdo
    base_message = f"E ai, {name}! Separei ótimos jogos do GAMEPASS pra você: {games}"
    
    # Trunca a mensagem para garantir que não exceda 100 caracteres
    return base_message[:250]

#----------------------------PARTE 1: LOAD - Carregando os dados do arquivo CSV em um DataFrame----------------------------

# o caminho do arquivo a ser lido pelo pandas
df = pd.read_csv("data/base.csv", encoding="utf-16", sep=";") #se fo o caso, acrescentar o enconding e o separador: (...csv', encoding='latin1', sep=';')
#caso precise salvar como UTF-8
# df.to_csv("data/base_utf8.csv", index=False, encoding="utf-8")

# exibindo as primeiras linhas do DataFrame e informações gerais sobre ele
# print(df.head())
# print(df.info())
# print(df.columns)


#----------------------------PARTE 2: TRANSFORM - Limpando e transformando os dados----------------------------

# Limpando os nomes das colunas, removendo quebras de linha e espaços extras
df.columns = df.columns.str.replace('\n', ' ').str.strip()

# Removendo acentuação dos nomes dos jogos na coluna 'Name'
df['Name'] = df['Name'].apply(lambda x: unidecode.unidecode(str(x)))

# Função placeholder para gerar mensagens personalizadas usando LLM
df['Personalized Message'] = df['Name'].apply(generate_llm_message_placeholder)

# renomeando colunas para facilitar o acesso
df = df.rename(columns={
    'EA Play Season Pass Price': 'EA_Play_Price',
    'Minecraft Season Pass Price': 'Minecraft_Price'
})


# na planilha utilizada, algumas colunas numéricas vieram como objeto (string) e precisam ser convertidas
# foi utilizado o str.replace para substituir o R$ por espaço vazio e a vírgula por ponto assim, o pandas consegue converter a coluna para numérico
df['Total Value'] = (df['Total Value']
                     .str.replace('R$', '') # Remove 'R$'
                     .str.replace(',', '.') # Troca vírgula por ponto
                     .str.replace('-','0') # Troca '-' por 0
                     .str.strip() #remove os espaços extras
                     .astype(float) # Converte para float
                     ) 

df['Coupon Value'] = (df['Coupon Value']
                     .str.replace('R$', '') # Remove 'R$'
                     .str.replace(',', '.') # Troca vírgula por ponto
                     .str.replace('-','0') # Troca '-' por 0
                     .str.strip() #remove os espaços extras
                     .astype(float) # Converte para float
                     ) 

df['Minecraft_Price'] = (df['Minecraft_Price']
                     .str.replace('R$', '') # Remove 'R$'
                     .str.replace(',', '.') # Troca vírgula por ponto
                     .str.replace('-','0') # Troca '-' por 0
                     .str.strip() #remove os espaços extras
                     .astype(float) # Converte para float
                     ) 

df['EA_Play_Price'] = (df['EA_Play_Price']
                     .str.replace('R$', '') # Remove 'R$'
                     .str.replace(',', '.') # Troca vírgula por ponto
                     .str.replace('-','0') # Troca '-' por 0
                     .str.strip() #remove os espaços extras
                     .astype(float) # Converte para float
                     )

df['Subscription Price'] = (df['Subscription Price']
                     .str.replace('R$', '') # Remove 'R$'
                     .str.replace(',', '.') # Troca vírgula por ponto
                     .str.replace('-','0') # Troca '-' por 0
                     .str.strip() #remove os espaços extras
                     .astype(float) # Converte para float
                     )

# configurando uma nova coluna com o valor líquido, subtraindo o valor do cupom do valor total
df['Net Value'] = df['Total Value'] - df['Coupon Value']

# criando uma nova coluna categórica baseada na coluna Net Value. Se o valor for maior que 40, é considerado 'High Value', caso contrário, 'Standard'
df['Value Category'] = np.where(
    df['Net Value'] > 40,
    'High Value',
    'Standard'
)


#----------------------------PARTE 3: LOAD - Salvando o DataFrame transformado em um arquivo JSON----------------------------

# salvando o arquivo transformado em formato JSON com indentação para melhor legibilidade
df.to_json('data/xbox_sales_transformed.json', orient='records', indent=4, force_ascii=False) 
print("ETL concluído. O arquivo 'data/xbox_sales_transformed.json' foi gerado.")
print("\nPrimeiras 5 linhas do DataFrame Transformado (apenas para verificação):")
print(df[['Name', 'Personalized Message', 'Plan', 'Net Value', 'Value Category']].head())

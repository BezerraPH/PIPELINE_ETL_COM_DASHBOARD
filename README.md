---

# 🚀 PIPELINE_ETL_COM_DASHBOARD  

## 🎮 Análise de Valor e Personalização de Assinaturas Xbox Game Pass  

Este projeto demonstra a construção completa de um **pipeline ETL (Extract, Transform, Load)** aplicado à análise de dados de vendas de assinaturas do **Xbox Game Pass**.  

O objetivo é ir além da simples manipulação de dados, integrando a **simulação de Inteligência Artificial Generativa (LLM)** para enriquecer os dados e fornecer **insights de negócio** através de um **Dashboard Web interativo**.  

Este projeto é uma evolução prática do **Desafio de Projeto da Santander Dev Week 2023 (DIO)**, aplicando a mesma metodologia em um novo domínio: **Gaming/Subscriptions**.  

---

## ✨ Destaques do Projeto  

- **Automação ETL em Python** → Processamento robusto de dados semi-estruturados (CSV), com foco em limpeza de dados monetários e padronização.  
- **Simulação de LLM para Marketing** → Geração de mensagens curtas e personalizadas, simulando a criação por modelos de linguagem (ex.: GPT/Gemini).  
- **Engenharia de Dados Aplicada** → Criação de métricas de negócio como **Net Value** e **Value Category (High Value / Standard)**.  
- **Dashboard Interativo e Responsivo** → Visualização dos resultados em HTML + Tailwind CSS, com gráficos dinâmicos via Chart.js.  

---

## ⚙️ Tecnologias Utilizadas  

| Categoria            | Tecnologia             | Uso no Projeto                                                                 |
|----------------------|------------------------|-------------------------------------------------------------------------------|
| **Linguagem Principal** | Python                 | Orquestração do pipeline, limpeza de dados e geração do JSON final             |
| **Data Science**     | Pandas, NumPy, Unidecode | Manipulação de DataFrames, cálculos de métricas e normalização de strings      |
| **Formato de Saída** | JSON                   | Estrutura eficiente para consumo direto pelo Dashboard Web                     |
| **Frontend**         | HTML5, JavaScript      | Estrutura do Dashboard e lógica de carregamento assíncrono                     |
| **Visualização**     | Chart.js               | Renderização dos gráficos de análise de vendas e rentabilidade                 |
| **Estilização**      | Tailwind CSS           | Framework utilitário para design moderno e responsivo                          |

---

## 📐 Metodologia do Pipeline ETL  

O projeto está dividido em três etapas sequenciais, gerenciadas pelo script **`xbox_etl_pipeline.py`**:  

### 1. Extract (Extração)  
- Fonte: `base.csv` (simulação de dados de assinaturas).  
- Processamento: leitura do arquivo, ajuste de codificação e limpeza inicial do cabeçalho para garantir nomes de colunas padronizados.  

### 2. Transform (Transformação)  
Principais operações:  
- **Limpeza Monetária** → Conversão de strings com símbolos (`R$ 15,00`, `-`) para `float`.  
- **Cálculo de Net Value** → Receita líquida = Valor Total - Cupom.  
- **Categorização** → Definição da `Value Category` (High Value ou Standard).  
- **Enriquecimento (LLM Simulado)** → Geração da coluna `Personalized Message` com mensagens de marketing personalizadas.  

### 3. Load (Carregamento)  
- Exportação para `data/xbox_sales_transformed.json` no formato **lista de objetos (orient='records')**.  
- Consumo Web: `index.html` carrega o JSON, permitindo visualização rápida e sem erros de separador CSV.  

---

## 💻 Como Rodar o Projeto  

### Pré-requisitos  
- Python 3.x  
- Bibliotecas necessárias:  
  ```bash
  pip install pandas numpy unidecode
  ```

### Passos  
1. **Executar o ETL**  
   ```bash
   python xbox_etl_pipeline.py
   ```  

2. **Visualizar o Dashboard**  
   Inicie um servidor web local:  
   ```bash
   python -m http.server 8000
   ```  
   Abra o navegador em: [http://localhost:8000/index.html](http://localhost:8000/index.html)  

---

## 📸 Dashboard Interativo  

O Dashboard fornece uma visão **360º da base de assinantes**, com recursos como:  
- Inspeção de dados brutos (tabela oculta).  
- Gerenciamento de mensagens (simulação de envio).  

| Gráfico                        | Insight de Negócio                                                                 |
|--------------------------------|------------------------------------------------------------------------------------|
| **Distribuição dos Planos**    | Popularidade dos planos e potencial de upsell                                       |
| **Contagem por Categoria**     | Segmentação em High Value vs. Standard → campanhas de retenção e investimento       |
| **Receita Líquida Média**      | Identificação do plano mais rentável (após descontos/cupons)                        |

---

## 🌐 Projeto Publicado  

Este projeto está disponível online através do **GitHub Pages**:  
👉 [https://bezerraph.github.io/PIPELINE_ETL_COM_DASHBOARD/](https://bezerraph.github.io/PIPELINE_ETL_COM_DASHBOARD/)   

<img width="1906" height="882" alt="image" src="https://github.com/user-attachments/assets/54796e6f-812b-4a5e-be30-849cd1285b9b" /> 

---

## 📬 Contato  

Conecte-se comigo e confira meu trabalho:  
- 🔗 [LinkedIn](https://www.linkedin.com/in/pedro-oliveira-a16a99273/)    

---

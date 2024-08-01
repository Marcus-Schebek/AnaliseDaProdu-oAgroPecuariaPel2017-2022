import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# Caminho para o arquivo CSV final
file_path = 'Produção Agropecuária e Extração - Tabela Final.csv'

# Leitura do arquivo CSV
data = pd.read_csv(file_path)

# Converter "-" para NaN para facilitar a remoção
data.replace("-", pd.NA, inplace=True)

# Eliminar linhas que têm apenas valores NaN em todas as colunas dos anos
years = [str(year) for year in range(2017, 2023)]
data = data.dropna(subset=years, how='all')

# Eliminar valores NaN remanescentes para garantir a integridade dos dados
data = data.dropna()

# Título da aplicação
st.title('Produção Agropecuária e Extração ao Longo dos Anos')

# Seleção do item para visualização
item = st.selectbox('Selecione um item para visualizar a produção:', data['name'].unique())

# Filtrar os dados para o item selecionado
filtered_data = data[data['name'] == item]

# Exibir os dados em formato de tabela
st.write(f"Dados para {item}:")
st.dataframe(filtered_data)

# Plotar a produção ao longo dos anos
values = filtered_data[years].values.flatten()

plt.figure(figsize=(10, 5))
plt.plot(years, values, marker='o', linestyle='-', color='b')
plt.xlabel('Ano')
plt.ylabel('Produção')
plt.title(f'Produção de {item} ao Longo dos Anos')
plt.grid(True)

# Exibir o gráfico no Streamlit
st.pyplot(plt)

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("BD_PARTOS_original..xlsx") 
st.title("Relatório de Análise de Dados")
st.text("Visão Geral")
col1, col2 = st.columns(2, gap="large")
with col1:
    col1.metric(label="Total de Partos", value=int(df.PARTOS.sum()))
    contagem_uti = df['UTI_RN'].value_counts()
    fig, ax = plt.subplots(figsize=(5, 5))
    ax.bar(contagem_uti.index.astype(str), contagem_uti.values, color='#f1c40f')
    ax.set_title('Encaminhados para UTI', color='#e67e22', fontweight='bold', loc='left')
    ax.set_ylabel('Quantidade')
    ax.set_xlabel('Encaminhado (1=Sim / 0=Não)')
    st.pyplot(fig)

with col2:
    legenda = {1: 'Vaginal', 2: 'Cesárea'}
    df['DESCRICAO_PARTO'] = df['TIPO_PARTO'].map(legenda)
    contagem = df['DESCRICAO_PARTO'].value_counts()
    total_cesareas = contagem.get('Cesárea', 0)
    st.metric(label="Total de Partos Cesáreos", value=int(total_cesareas))


    contagem_epi = df['EPISIOTOMIA'].value_counts()
    fig_epi, ax_epi = plt.subplots()
    cores_epi = ['#3498db', '#e67e22'] 

    ax_epi.pie(
    contagem_epi, 
    labels=['Não', 'Sim'], 
    autopct='%1.1f%%', 
    startangle=90, 
    colors=cores_epi, 
    wedgeprops={'width': 0.4} 
    )
    ax_epi.set_title('Episiotomia', color='#e67e22', fontweight='bold', loc='left')
    st.pyplot(fig_epi)

st.markdown("---")
st.subheader("Distribuição de Peso dos Recém-Nascidos")
fig_largo, ax_largo = plt.subplots(figsize=(15, 5))
ax_largo.hist(df['PESO_NASCER'], bins=50, color='#3498db', edgecolor='white', alpha=0.8)
ax_largo.set_title('Frequência de Pesos (em gramas)', fontsize=14, fontweight='bold', color='#2c3e50')
ax_largo.set_xlabel('Peso (g)')
ax_largo.set_ylabel('Quantidade de Bebês')
ax_largo.grid(axis='y', linestyle='--', alpha=0.3)
ax_largo.set_facecolor('#f8f9fa') 
st.pyplot(fig_largo)

col1, col_espaco, col2 = st.columns([1, 0.15, 1]) 
with col1:
     st.markdown("<h4 style='text-align: center; color: #e67e22;'>Uso de Analgesia</h4>", unsafe_allow_html=True)
     fig1, ax1 = plt.subplots(figsize=(5, 4))
     counts = df.ANALGESIA.value_counts()
     ax1.pie(counts, labels=counts.index, autopct='%1.1f%%', startangle=90)
     plt.tight_layout()
     st.pyplot(fig1)

with col2:
    st.markdown("<h4 style='text-align: center; color: #e67e22;'>Média de APGAR1</h4>", unsafe_allow_html=True)
    fig2, ax2 = plt.subplots(figsize=(5, 4))
    df.groupby('TIPO_PARTO')['APGAR1'].mean().plot(kind='bar', ax=ax2, color='skyblue')
    plt.tight_layout()
    st.pyplot(fig2)


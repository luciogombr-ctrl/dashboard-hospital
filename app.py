import streamlit as st
import pandas as pd
import numpy as np

# -----------------------------
# CONFIGURAÇÃO DA PÁGINA
# -----------------------------
st.set_page_config(
    page_title="Dashboard Hospitalar",
    page_icon="🏥",
    layout="wide"
)

# -----------------------------
# DADOS FICTÍCIOS
# -----------------------------
np.random.seed(42)

dados = pd.DataFrame({
    "Paciente": [f"Paciente {i}" for i in range(1, 21)],
    "Idade": np.random.randint(1, 90, 20),
    "Tempo Internação": np.random.randint(1, 15, 20),
    "Setor": np.random.choice(
        ["UTI", "Emergência", "Pediatria", "Clínico"],
        20
    ),
    "Custo": np.random.randint(500, 10000, 20)
})

# -----------------------------
# TÍTULO
# -----------------------------
st.title("🏥 Dashboard Hospitalar")
st.markdown("Visão geral do hospital em tempo real")

# -----------------------------
# MÉTRICAS
# -----------------------------
total_pacientes = len(dados)
media_idade = int(dados["Idade"].mean())
media_internacao = int(dados["Tempo Internação"].mean())
custo_total = dados["Custo"].sum()

col1, col2, col3, col4 = st.columns(4)

col1.metric("Pacientes", total_pacientes)
col2.metric("Idade Média", media_idade)
col3.metric("Internação Média", f"{media_internacao} dias")
col4.metric("Custo Total", f"R$ {custo_total:,.2f}")

# -----------------------------
# GRÁFICOS
# -----------------------------
st.subheader("Pacientes por Setor")

setor = dados["Setor"].value_counts()

st.bar_chart(setor)

# -----------------------------
# TABELA
# -----------------------------
st.subheader("Lista de Pacientes")

st.dataframe(dados, use_container_width=True)

# -----------------------------
# GRÁFICO DE CUSTOS
# -----------------------------
st.subheader("Custos por Paciente")

st.line_chart(dados["Custo"])

# -----------------------------
# RODAPÉ
# -----------------------------
st.markdown("---")
st.caption("Dashboard Hospitalar Simples usando Streamlit")
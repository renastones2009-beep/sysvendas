import streamlit as st
import pandas as pd
import plotly.express as px

tb_vendas=pd.read_csv("Aula4/vendas.csv")

st.title("Sistema de Vendas")

st.sidebar.write("## Cadastro de Vendas")

str_dt=st.sidebar.date_input("Selecione a data",min_value=pd.to_datetime("today"))
str_sel=st.sidebar.selectbox("Selecione o vendedor", ["Ana", "Buno", "Flavio", "Gabriel", "Gustavo", "João", "Juliana", "Lucas", "Marcos", "Matheus", "Rafael", "Vinicius"])
str_prod=st.sidebar.selectbox("Selecione o produto", ["Notebook", "Celphone", "Phone", "Tablet", "Monitor", "Teclado", "Mouse", "Fone de Ouvido", "Câmera", "Impressora"])
str_qtd=st.sidebar.number_input("Selecione a quantidade", min_value=1, step=1)
str_val=st.sidebar.number_input("Selecione o valor", min_value=0.0, step=0.01)
btn_cadastrar=st.sidebar.button("Cadastrar Venda")

if btn_cadastrar:
    if str_qtd<=0 or str_val<=0:
        st.error("Quantidade e valor devem ser maiores que zero!")
    else:
        lst_nova_venda=[str(str_dt), str(str_sel), str(str_prod), str(str_qtd), float(str_val)]
        tb_vendas.loc[len(tb_vendas)]=lst_nova_venda
        tb_vendas.to_csv("Aula4/vendas.csv", index=False)
        st.success("Venda cadastrada com sucesso!")

st.write("## Vendas Cadastradas")

st.dataframe(tb_vendas)

st.write("## Dashboard")

str_fat_total=tb_vendas["valor"].sum()
st.metric("Faturamento Total", f"R${str_fat_total}")

graf1=px.bar(tb_vendas, x="vendedor", y="valor", color="produto")
st.plotly_chart(graf1)
graf2=px.pie(tb_vendas, names="produto", values="valor", hole=0.5)
st.plotly_chart(graf2)
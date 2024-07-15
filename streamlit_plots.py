import streamlit as st
import matplotlib.pylab as plt
import seaborn as sns

def mostrar_graficos():
    
    st.title("Graficos con matplotlib")
    df = sns.load_dataset(name="tips")
    with st.expander(label="Expandir información", expanded=False):
        st.dataframe(df)

    fig = plt.figure()
    sns.countplot(x=df["sex"])
    with st.expander(label="Expandir Gráfico", expanded=False):
        st.pyplot(fig)

if __name__=="__main__":
    mostrar_graficos()
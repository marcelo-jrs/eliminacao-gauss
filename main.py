import streamlit as st
import numpy as np

st.set_page_config(
    page_title="Calculadora",
    page_icon="calc.png",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'About': """
        # Calculo numérico
        - Eliminação de gauss
        - LU + permutação
        - Gauss-Seidel
        """
    }
)

matriz_A4 = np.array([[1.0, 6.0, 2.0, 4.0],
          [3.0, 19.0, 4.0, 15.0],
          [1.0, 4.0, 8.0, -12.0],
          [5.0, 33.0, 9.0, 3.0]])

matriz_A3 = np.array([[4.0, -1.0, 0.0], 
                     [1.0, 3.0, -1.0], 
                     [2.0, 0.0, 5.0]])

matriz_B3 = np.array([3.0, 6.0, -2.0])

matriz_B4 = np.array([8.0, 25.0, 18.0, 72.0])

x3 = np.array([0.0, 0.0, 0.0])
x4 = np.array([0.0, 0.0, 0.0, 0.0])



metodo = st.sidebar.radio(
    "Qual método vai utilizar?",
    ("Eliminação de gauss", "Gauss-Seidel")
)

if metodo == "Eliminação de gauss":
    column_size = st.sidebar.radio(
    "Quantas linhas terá a matriz?",
    (3, 4)
    )
    if column_size == 3:
        st.sidebar.subheader("Insira a matriz A: ")
        matriz_A3 = st.sidebar.data_editor(matriz_A3, hide_index=True)
        st.sidebar.subheader("Insira a matriz B: ")
        matriz_B3 = st.sidebar.data_editor(matriz_B3, hide_index=True)
    elif column_size == 4:
        st.sidebar.subheader("Insira a matriz A: ")
        matriz_A4 = st.sidebar.data_editor(matriz_A4, hide_index=True)
        st.sidebar.subheader("Insira a matriz B: ")
        matriz_B4 = st.sidebar.data_editor(matriz_B4, hide_index=True)
elif metodo == "Gauss-Seidel":
    #(A, b, x0, epsilon=1e-5, max_iterations=100)
    column_size = st.sidebar.radio(
    "Quantas linhas terá a matriz?",
    (3, 4)
    )
    if column_size == 3:
        max_iterations = st.sidebar.slider("Máximo de Iterações:", 0, 1000, 250)
        epsilon = st.sidebar.slider("Épsilon:",0.0, 1.0, 0.05)
        st.sidebar.subheader("Insira a matriz A: ")
        matriz_A3 = st.sidebar.data_editor(matriz_A3, hide_index=True)
        st.sidebar.subheader("Insira a matriz B: ")
        matriz_B3 = st.sidebar.data_editor(matriz_B3, hide_index=True)
        st.sidebar.subheader("Insira o palpite: ")
        x3 = st.sidebar.data_editor(x3, hide_index=True)
    elif column_size == 4:
        max_iterations = st.sidebar.slider("Máximo de Iterações:", 0, 1000, 250)
        epsilon = st.sidebar.slider("Épsilon:",0.0, 1.0, 0.05)
        st.sidebar.subheader("Insira a matriz A: ")
        matriz_A4 = st.sidebar.data_editor(matriz_A4, hide_index=True)
        st.sidebar.subheader("Insira a matriz B: ")
        matriz_B4 = st.sidebar.data_editor(matriz_B4, hide_index=True)
        st.sidebar.subheader("Insira o palpite: ")
        x4 = st.sidebar.data_editor(x4, hide_index=True)
        
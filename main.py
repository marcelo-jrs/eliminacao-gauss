import streamlit as st
import numpy as np
from algoritmos import seidel
from algoritmos import gauss

st.set_page_config(
    page_title="Calculadora",
    page_icon="calc.png",
    layout="wide",
    menu_items={
        'About': """
        # Calculo numérico
        - Eliminação de gauss
        - LU + permutação
        - Gauss-Seidel
        """
    }
)



tab1, tab2, tab3 = st.tabs(["Parâmetros", "Resultados", "Sobre"])
col1, col2, col3, col4 = st.columns(4)
container_radio = st.container()
container_matrizA = st.container()
container_matrizB = st.container()

with tab1:
    column_size = st.radio(
    "Quantas linhas terá a matriz?",
    (3, 4)
    )


def user_input_matriz(column_size):
    with tab1:
        if column_size == 3:
            st.write("Insira a matriz A: ")
            a11 = st.number_input("a11",value=4.0 ,key="a11")
            a12 = st.number_input("a12",value=-1.0, key="a12")
            a13 = st.number_input("a13",value=0.0, key="a13")
            a21 = st.number_input("a21",value=1.0, key="a21")
            a22 = st.number_input("a22",value=3.0, key="a22")
            a23 = st.number_input("a23",value=-1.0, key="a23")
            a31 = st.number_input("a31",value=2.0, key="a31")
            a32 = st.number_input("a32",value=0.0, key="a32")
            a33 = st.number_input("a33",value=5.0, key="a33")

            matriz_A = np.array([[a11, a12, a13],
                                [a21, a22, a23],
                                [a31, a32, a33]])
            
            st.write("Insira a matriz B: ")
            b11 = st.number_input("b11",value=3.0 ,key="b11")
            b12 = st.number_input("b12",value=6.0 ,key="b12")
            b13 = st.number_input("b13",value=-2.0 ,key="b13")

            matriz_B = np.array([b11, b12, b13])

            return matriz_A, matriz_B
        elif column_size == 4:
            c11 = st.number_input("a11",value=10.0 ,key="c11")
            c12 = st.number_input("a12",value=-1.0 ,key="c12")
            c13 = st.number_input("a13",value=2.0 ,key="c13")
            c14 = st.number_input("a14",value=0.0 ,key="c14")
            c21 = st.number_input("a21",value=-1.0 ,key="c21")
            c22 = st.number_input("a22",value=11.0 ,key="c22")
            c23 = st.number_input("a23",value=-1.0 ,key="c23")
            c24 = st.number_input("a24",value=3.0 ,key="c24")
            c31 = st.number_input("a31",value=2.0 ,key="c31")
            c32 = st.number_input("a32",value=-1.0 ,key="c32")
            c33 = st.number_input("a33",value=10.0 ,key="c33")
            c34 = st.number_input("a34",value=-1.0 ,key="c34")
            c41 = st.number_input("a41",value=0.0 ,key="c41")
            c42 = st.number_input("a42",value=3.0 ,key="c42")
            c43 = st.number_input("a43",value=-1.0 ,key="c43")
            c44 = st.number_input("a44",value=8.0 ,key="c44")

            matriz_C = np.array([[c11, c12, c13, c14],
                                [c21, c22, c23, c24],
                                [c31, c32, c33, c34],
                                [c41, c42, c43, c44]])

            st.write("Insira a matriz B: ")
            d11 = st.number_input("b11",value=6.0 , key="d11")
            d12 = st.number_input("b12",value=25.0 , key="d12")
            d13 = st.number_input("b13",value=-11.0 , key="d13")
            d14 = st.number_input("b14",value=15.0 , key="d14")

            matriz_D = np.array([d11, d12, d13, d14])

            return matriz_C, matriz_D

def user_input_seidel(column_size):
    with tab1:
        st.subheader("Preencha caso for usar o método de gauss-seidel")
        max_iterations = st.slider("Máximo de Iterações:", 0, 1000, 250)
        epsilon = st.slider("Épsilon:",0.0, 1.0, 0.05)
        if column_size == 3:
            x11 = st.number_input("x11", key="x11")
            x12 = st.number_input("x12", key="x12")
            x13 = st.number_input("x13", key="x13")

            x0 = np.array([x11, x12, x13])
        elif column_size == 4:
            x11 = st.number_input("x11", key="x11")
            x12 = st.number_input("x12", key="x12")
            x13 = st.number_input("x13", key="x13")
            x14 = st.number_input("x14", key="x14")

            x0 = np.array([x11, x12, x13, x14])
        
        return max_iterations, epsilon, x0


matrizA, matrizB = user_input_matriz(column_size)

max_iterations, epsilon, x0 = user_input_seidel(column_size)

seidel.gauss_seidel(max_iterations, epsilon, x0, matrizA, matrizB)
gauss.eliminacao_gauss(matrizA, matrizB)

seidel_click = st.button("Executar gauss-seidel", key="seidel_click")
gauss_click = st.button("Executar eliminação de gauss", key="gauss_click")

if seidel_click:
    results = seidel.gauss_seidel(max_iterations, epsilon, x0, matrizA, matrizB)
    with tab2:
        st.dataframe(results)
if gauss_click:
    results = gauss.eliminacao_gauss(matrizA, matrizB)
    l, u, p = gauss.decomposicao_LU(matrizA)

    with tab2:
        st.subheader("Solução para o sistema: ")
        st.dataframe(results)
        st.write("matriz L")
        st.dataframe(l)
        st.write("matriz U")
        st.dataframe(u)
        st.write("matriz de permutação")
        st.dataframe(p)
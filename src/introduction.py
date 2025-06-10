import streamlit as st
import time
from src.helpers import create_participant

def show_intro():

    st.image("ppges.png", use_container_width=True)  # Ensure the image is displayed properly

    # Introduction page
    st.title("Atividade Interativa - Introdução ao Big Data")
    st.write("Bem-vindo(a) a atividade interativa do grupo de Introdução ao Big Data!")
    st.write("Por favor, insira seu nome para continuar:")

    # Input field for student name
    name = st.text_input("Nome:")
    age = st.text_input("Idade:")
    sexo = st.selectbox("Sexo:", ["Masculino", "Feminino", "Outro"])
    interest = st.text_input("Área de Interesse (Ex: Engenharia de Materiais):")

    # Submit button
    if st.button("Continuar", type="primary"):
        if name:
            create_participant(name, age, sexo, interest)  # Assuming age and interest are not required for this step
            st.session_state['name'] = name
            st.session_state['sexo'] = sexo
            st.success("Nome salvo com sucesso! Redirecionando para as aulas...")
            with st.spinner("Carregando aulas..."):
                time.sleep(3)  
            st.rerun()
        else:
            st.error("Por favor, insira um nome válido.")
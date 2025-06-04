import streamlit as st
from src.helpers import create_participant

def show_intro():

    # Introduction page
    st.title("Introdução ao Big Data 🚀")
    st.write("Por favor, insira seu nome para continuar:")

    # Input field for student name
    name = st.text_input("Nome:")
    age = st.text_input("Idade:")
    interest = st.text_input("Interesse:")

    # Submit button
    if st.button("Enviar"):
        if name:
            create_participant(name, age, interest)  # Assuming age and interest are not required for this step
            st.session_state['name'] = name
            st.success("Nome salvo com sucesso! Redirecionando para as aulas...")
            
            st.rerun()
        else:
            st.error("Por favor, insira um nome válido.")
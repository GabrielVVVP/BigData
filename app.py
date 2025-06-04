import streamlit as st
from src.helpers import initialize_database
from src.application import show_app
from src.introduction import show_intro

st.set_page_config(page_title="Big Data - Introdução à Cibernética", layout="wide")

initialize_database()

def main():

    if 'name' in st.session_state:
        show_app()
    else:
        show_intro()

if __name__ == "__main__":
    main()   

import streamlit as st

st.title("First Streamlit App 👋")
st.markdown(
    """ 

Es una aplicacion WEB que permite calcular la edad de una persona a partir de su fecha de nacimiento.

Se requiere ingresar el nombre del usuario y la fecha de nacimiento en formato ddmmaaaa, 
sin caracteres que separen los numeros.

    """
)

NombreUsuario = st.text_input("Nombre del usuario")
Fecha = st.text_input("Fecha de nacimiento sin caracteres que separen los numeros, formato ddmmaaaa")


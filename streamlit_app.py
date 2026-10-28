import streamlit as st
import datetime

st.title("First Streamlit App 👋")
st.markdown(
    """ 

Es una aplicacion WEB que permite calcular la edad de una persona a partir de su fecha de nacimiento.

Se requiere ingresar el nombre del usuario y la fecha de nacimiento en formato ddmmaaaa, 
sin caracteres que separen los numeros.

    """
)

NombreUsuario = st.text_input("Nombre del usuario")
Fecha = st.date_input("Seleccione fecha de nacimiento sin caracteres que separen los numeros, formato aaaa/mm/dd:", datetime.date.today())

st.write("La fecha ingresada es: ", Fecha , "por el usuario:", NombreUsuario)
st.write(NombreUsuario)


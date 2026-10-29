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

fecha_minima = datetime.date(1900, 1, 1)
fecha_maxima = datetime.date(2050, 12, 31)

NombreUsuario = st.text_input("Nombre del usuario")
fecha_seleccionada = st.date_input(
    label="Seleccione fecha de nacimiento sin caracteres que separen los numeros, formato aaaa/mm/dd:",
    value=datetime.date.today(),  # Fecha inicial por defecto
    min_value=fecha_minima,       # Desbloquea los años hacia atrás
    max_value=fecha_maxima        # Desbloquea los años hacia adelante
)

edad = datetime.date.today() - fecha_seleccionada

st.write("La fecha ingresada es: ", fecha_seleccionada , "por el usuario:", NombreUsuario)
st.write(NombreUsuario)

st.write("Fecha elegida:", fecha_seleccionada)
st.write("Edad:", edad)


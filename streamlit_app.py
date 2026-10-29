import streamlit as st
from datetime import *
from dateutil.relativedelta import *


st.title("First Streamlit App 👋")
st.markdown(
    """ 

Es una aplicacion WEB que permite calcular la edad de una persona a partir de su fecha de nacimiento.

Se requiere ingresar el nombre del usuario y la fecha de nacimiento en formato ddmmaaaa, 
sin caracteres que separen los numeros.

    """
)
fecha_minima = datetime.date(1990, 1, 1)

fecha_maxima = datetime.date.today()
st.subheader("Resultado:", fecha_maxima)

NombreUsuario = st.text_input("Nombre del usuario")
fecha_seleccionada = st.date_input(
    label="Seleccione fecha de nacimiento sin caracteres que separen los numeros, formato aaaa/mm/dd:",
    value=datetime.date.today(),  # Fecha inicial por defecto
    min_value=fecha_minima,       # Desbloquea los años hacia atrás
    max_value=fecha_maxima        # Desbloquea los años hacia adelante
)

if fecha_seleccionada > fecha_maxima:
  st.error("La fecha seleccionada debe ser anterior a la fecha de hoy.")
else:
  diferencia = relativedelta(fecha_seleccionada, fecha_maxima)
  anios = diferencia.yearsr
  st.subheader("Resultado:")
  st.write(f"**Años completos:** {anios} años")
  st.write(
      f"Detalle exacto: {diferencia.years} años, {diferencia.months} meses y"
      f" {diferencia.days} días."
  )
st.write("La fecha ingresada es: ", fecha_seleccionada , "por el usuario:", NombreUsuario)
st.write(NombreUsuario)

st.write("Fecha elegida:", fecha_seleccionada)
st.write("Edad (en dias): ", edad)
st.write("Edad (en años): ", anios)


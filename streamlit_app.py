import streamlit as st
import datetime
from dateutil.relativedelta import *

 
st.title("First Streamlit App 👋")
st.markdown(
    """ 

Es una aplicacion WEB que permite calcular la edad de una persona a partir de su fecha de nacimiento.

Se requiere ingresar el nombre del usuario y la fecha de nacimiento en formato ddmmaaaa, 
sin caracteres que separen los numeros.

    """
)
 
FechaMinima = datetime.date(1900,1,1)
FechaMaxima = datetime.date.today()
st.write("Fecha máxima:", FechaMaxima)

NombreUsuario = st.text_input("Nombre del usuario")
FechaSeleccionada = st.date_input(
    label="Seleccione fecha de nacimiento sin caracteres que separen los numeros, formato aaaa/mm/dd:",
    value=datetime.date.today(),  # Fecha inicial por defecto
    min_value=FechaMinima,       # Desbloquea los años hacia atrás
    max_value=FechaMaxima        # Desbloquea los años hacia adelante
)

if FechaSeleccionada > FechaMaxima:
  st.error("La fecha seleccionada debe ser anterior a la fecha de hoy.")
else:
  diferencia = relativedelta(FechaMaxima, FechaSeleccionada)
  anios = diferencia.years
  st.subheader("Resultado:")
  st.write(f"**Años completos:** {anios} años")
  st.write(
      f"Detalle exacto: {diferencia.years} años, {diferencia.months} meses y"
      f" {diferencia.days} días."
  )
    
st.write("La fecha ingresada es: ", FechaSeleccionada , "por el usuario:", NombreUsuario)
edad = (FechaMaxima - FechaSeleccionada)
st.write("Fecha elegida:", FechaSeleccionada)
st.write("Edad (en dias): ", edad)
st.write("Edad (en semanas): ", diferencia.years * 52 + diferencia.months * 4 + diferencia.days // 7)

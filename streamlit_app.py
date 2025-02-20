import streamlit as st

st.title("🎈Esta es mi nueva aplicacion")
st.write(
    "### Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

cantidad = st.slider ("selecciona la cantidad")

st.write(f'la cantidad seleccionada es: {cantidad}')

for i in range(cantidad):
    st.button(f'{i}')
import streamlit as st

def main():
    st.title("Mi aplicacion")
    st.write("¡Bienvenido!")
    
    # Entrada de usuario
    nombre = st.text_input("Ingresa tu nombre:")
    estado_animo = st.selectbox("¿Cómo te sientes hoy?", ["Feliz", "Triste", "Motivado", "Cansado"])
    
    if st.button("Mostrar mensaje"):
        st.success(f"Hola {nombre}, parece que hoy te sientes {estado_animo}.")
    
if __name__ == "__main__":
    main()

import streamlit as st
import random

# Configuración de la página
st.set_page_config(page_title="Mundo Musical", page_icon="🎵", layout="centered")

# Título principal con emoji
st.title("🎶 ¡Bienvenido a Mundo Musical! 🎧")

# Sidebar con opciones
st.sidebar.header("📌 Menú de Navegación")
option = st.sidebar.radio("Selecciona una opción:", ["🏠 Inicio", "🎼 Géneros Musicales", "🎤 Artistas Destacados", "ℹ️ Acerca de"])

# Contenido según la opción seleccionada
def show_home():
    st.subheader("🏡 Página de Inicio")
    st.write("Explora el maravilloso mundo de la música. 🎼")
    if st.button("🎵 Descubre una canción sorpresa"):
        songs = ["🎸 Bohemian Rhapsody - Queen", "🎤 Billie Jean - Michael Jackson", "🎶 Rolling in the Deep - Adele", "🥁 Smells Like Teen Spirit - Nirvana"]
        st.success(f"Recomendación: {random.choice(songs)}")

def show_genres():
    st.subheader("🎼 Géneros Musicales")
    genres = ["🎷 Jazz", "🎸 Rock", "🎹 Clásica", "🎵 Pop", "🥁 Hip-Hop", "🎶 Reggaetón"]
    for genre in genres:
        st.write(genre)

def show_artists():
    st.subheader("🎤 Artistas Destacados")
    artists = ["🎸 Jimi Hendrix", "🎤 Beyoncé", "🎹 Mozart", "🎶 The Beatles", "🥁 Eminem", "🎵 Shakira"]
    for artist in artists:
        st.write(artist)

def show_about():
    st.subheader("ℹ️ Acerca de")
    st.write("Esta aplicación está dedicada a todos los amantes de la música. 🎶")

if option == "🏠 Inicio":
    show_home()
elif option == "🎼 Géneros Musicales":
    show_genres()
elif option == "🎤 Artistas Destacados":
    show_artists()
elif option == "ℹ️ Acerca de":
    show_about()
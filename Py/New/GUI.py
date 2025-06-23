# app.py
import streamlit as st
import pandas as pd

# Simulace dat
data = {
    'Název': ['Elixír síly', 'Elixír zdraví', 'Elixír neviditelnosti'],
    'Cena': [100, 50, 200],
    'Sklad': [10, 25, 5]
}

df = pd.DataFrame(data)

st.title("🧪 Přehled elixírů")

# Filtr dle ceny
max_price = st.slider('Maximální cena elixíru', min_value=0, max_value=500, value=200)
filtered_df = df[df['Cena'] <= max_price]

# Zobrazení interaktivní tabulky
st.dataframe(filtered_df, use_container_width=True)

# Detail po kliknutí
selected = st.selectbox('Vyber elixír pro detail', filtered_df['Název'])
if selected:
    st.write("📦 Detail elixíru:")
    st.write(filtered_df[filtered_df['Název'] == selected])

# Tlačítko
if st.button("📝 Vypiš text do terminálu"):
    print("Test")
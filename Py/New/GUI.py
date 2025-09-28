# app.py
import streamlit as st
from Tables import *


#df = init_pots_dict()
df = get_recipe_book()

st.title("🧪 Přehled elixírů")

# Filtr dle ceny
#max_weight = st.slider('Maximální hmotnost elixíru', min_value=0.0, max_value=2.0, value=0.1)
#filtered_df = df[df['weight'] <= max_weight]
filtered_df = df


# Zobrazení interaktivní tabulky
st.dataframe(filtered_df, use_container_width=True)

"""
# Detail po kliknutí
selected = st.selectbox('Vyber elixír pro detail', filtered_df['Name'])
if selected:
    st.write("📦 Detail elixíru:")
    st.write(filtered_df[filtered_df['Name'] == selected])
"""
    

# Tlačítko
if st.button("📝 Vypiš text do terminálu"):
    print("Test 2 asdasd as")

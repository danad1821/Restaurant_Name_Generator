import streamlit as st
from langchain_helper import get_restaurant_name_and_items

st.title("Restaurant Name Generator")

cuisine = st.sidebar.selectbox("Pick your Cuisine", ('Lebanese', 'French', 'Italian', 'Mexican', 'Indian'))

def regenerate():
    get_restaurant_name_and_items(cuisine)

if cuisine:
    response = get_restaurant_name_and_items(cuisine)
    st.header(response['restaurant_name'])
    menu_items = response['menu_items'].split(',')
    st.write("**Menu Items:**")
    for item in menu_items:
        st.write("-", item)
    st.button("Regenerate", on_click=regenerate)
import streamlit as st
from pie import create_pie
from bar import create_bar
from hbar import create_hbar
from userfeedback import feedback

def buttons():
    if st.button("Different Item Types in Inventory"):
        create_pie()

    if st.button("Breakdown of Item Brands in Inventory"):
        create_hbar()

    if st.button("Different Item Types Purchased"):
        create_bar()

    if st.button("Userfeedback - Male and Female"):
        feedback()

    
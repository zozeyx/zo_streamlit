import streamlit as st

st.text_input('ID')
st.text_input('Password')
st.text_input('First Name')
st.text_input('Middle Name')
st.number_input('Pick your age', 0, 100)
st.radio('Pick your gender', ['Male', 'Female'])



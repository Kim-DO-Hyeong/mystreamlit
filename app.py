import streamlit as st

x=st.slider('Select a value',0,100)
st.write(x,'squared is',x*x)

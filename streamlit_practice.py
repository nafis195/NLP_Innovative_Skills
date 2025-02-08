import streamlit as st
import os

st.write({"key": "value"})
st.write(123)

3+4

pressed = st.button("press me")
print(pressed)

pressed2 = st.button("second button")
print("second:", pressed2)



st.title("Super Simple Title")
st.header("This is a header")
st.subheader("this is subheader")
st.markdown("This is _markdown_")
st.caption("this is caption")
code_eample = """
def main():
    print("Hello World")
"""
st.code(code_eample, language="python")
st.divider()

st.image(os.path.join(os.getcwd(), "static", "Dida1.png"), width=100)
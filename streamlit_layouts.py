import streamlit as st


# sidebar layout 
st.sidebar.title("This is sidebar")
st.sidebar.write("You can place elements like sidebars, buttons, and text here.")
sidebar_input = st.sidebar.text_input("Enter something in the sidebar")

# tabs layout
tab1, tab2, tab3 = st.tabs(["Tab 1", "Tab 2", "Tab 3"])
with tab1:
    st.write("You are in Tab 1")
with tab2:
    st.write("You are in Tab 2")
with tab3:
    st.write("You are in Tab 3")

# column layout
col1, col2 = st.columns(2)
with col1: 
    st.header("Column 1")
    st.write("Content for column 1")
with col2:
    st.header("Column 2")
    st.write("Content for column 2")

# containers example
with st.container(border=True):
    st.write("This is inside a container")
    st.write("You can thunk of containers as a grouping for elements")
    st.write("Containers halp manage sections of the page")

# empty placholder
placeholder = st.empty()
placeholder.write("This is an empty placeholder, useful for dynamic content.")
if st.button("Update Placeholder"):
    placeholder.write("The content of this placeholder has been updated.")

# expander
with st.expander("Expander for more details"):
    st.write("This is additional information that is hidden by default.")
    st.write("You can use expanders to keep your interface cleaner.")

# popover/tooltip
st.write("Hover over this button for a tooltip")
st.button("Button with Tooltip", help="This is a tooltip or popover on hover")

# sidebar input handling
if sidebar_input:
    st.write(f"You entered: {sidebar_input}")
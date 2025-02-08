import streamlit as st


# a simple counter variable without session state
# counter = 0

# st.write(f"Counter value: {counter}")

# # button to increament the counter
# if st.button("Increament"):
#     counter += 1
#     st.write(f"Counter value: {counter}")
# else:
#     st.write(f"Counter stays at {counter}")





# a simple counter variable with session state
if "counter" not in st.session_state:
    st.session_state.counter = 0

if st.button("Increament"):
    st.session_state.counter += 1
    st.write(f"Counter incremented to {st.session_state.counter}")

if st.button("Reset"):
    st.session_state.counter = 0

st.write(f"Counter value: {st.session_state.counter}")

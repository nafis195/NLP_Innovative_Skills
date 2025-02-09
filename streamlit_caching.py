import streamlit as st
import time


# @st.cache_data(ttl=60) # cache this for 60 seconds
# def fetch_data():
#     # Simulate a slow operation
#     time.sleep(5)
#     return "Data fetched from the server!"

# st.write("Fetching Data")
# data = fetch_data()
# st.write(data)






file_path = "example.txt"

@st.cache_resource
def get_file_handler():
    file = open(file_path, "a+")
    return file

# use the cached file handler
file_handler = get_file_handler()

# write to the file using the cached handler
if st.button("Write to File"):
    file_handler.write("New line of text\n")
    file_handler.flush()  # Ensure the data is written to the file immediately"
    st.success("Wrote a new line to the file!")

# read and display the file content
if st.button("Read File"):
    file_handler.seek(0)  # Reset the file pointer to the beginning
    content = file_handler.read()
    st.write(content)

# always close the file when done, it is useful for resource cleanup
st.buttion("Close File", on_click=file_handler.close)
import streamlit as st
import functions

todos = functions.get_todos()

st.title('My Todo App')
st.subheader("This is my ToDo app")
st.write("This app is to increase your productivity")

#st.checkbox("Buy Grocery")
#st.checkbox("Throw the trash ")


for todo in todos:
    st.checkbox(todo)

st.text_input(label="", placeholder="Add new todo...")
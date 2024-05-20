import streamlit as st
import pandas as pd

#Buttons
primary_btn = st.button(label="Primary", type="primary")
second_btn = st.button(label="Secondary", type="secondary")

if primary_btn:
    st.write("Hello from primary")

if second_btn:
    st.write("Hello from secondary")


#Checkbox
st.divider()
checkbox = st.checkbox("Remember me")

if checkbox:
    st.write("I will remeber you")
else:
    st.write("I will forget you")

# Radio
st.divider()

df = pd.read_csv("../charting_elements/data/sample.csv")

radio = st.radio("Choose a column", options=df.columns[1:], index=0, horizontal=True)
st.write(radio)

# Selectbox
st.divider()
select = st.selectbox("Choose a column", options=df.columns[1:], index=0)
st.write(select)


# Mutliselect
st.divider()

multiselect = st.multiselect("Choose as many columns as you want", 
                             options=df.columns[1:], default=["col1"], max_selections=3)

st.write(multiselect)

# Slider
st.divider()

slider = st.slider("Pick a number", min_value=0, max_value=10, value=0, step=1)
st.write(slider)


# Text input
st.divider()

text_input = st.text_input("What's your name", placeholder="Jhon Doe")
st.write(f"Your name is {text_input}")

# Number input
st.divider()

number_input = st.number_input("Pick a number", min_value=0, max_value=10, value=0, step=1)
st.write(f"You picked {number_input}")

# Text Area
st.divider()

text_area = st.text_area("What do you want to tell me?", height=200, placeholder="Write your message here")
st.write(text_area)
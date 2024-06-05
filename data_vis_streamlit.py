# import streamlit as st

# st.title('Data Visualization with Streamlit')
# tab1, tab2 = st.tabs(['Tottenham', 'Arsenal'])

# st.sidebar.title('this is sidebar')
# with tab1:
#     st.header('Tottenham Hotspur 2020/2021 Premier League Season')
#     st.checkbox('Show Data')
# with tab2:
#     st.header('Arsenal 2020/2021 Premier League Season')
#     st.image('https://upload.wikimedia.org/wikipedia/en/thumb/5/53/Arsenal_FC.svg/1200px-Arsenal_FC.svg.png', width=100)
#     st.subheader('Player Stats')

import streamlit as st
import math

st.title("PoK")
inp = st.text_input("boooo")
st.text(inp)
st.text("hello")



# # Make a list of empty slots
# empty_slots = [st.empty() for _ in range(5)]

# # Use the fifth slot to show chat box
# chat_input = empty_slots[3].text_input("Your message here")

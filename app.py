import streamlit as st
import utils
import pickle

model = pickle.load(open('model.pkl','rb'))

st.header('Duplicate Question checker')

q1 = st.text_input('Question 1')
q2 = st.text_input('Question 2')

if st.button('Check'):
    query = utils.query_point_creator(q1,q2)
    result = model.predict(query)[0]

    if result:
        st.header('Duplicate so merge')
    else:
        st.header("Not Duplicate so don't merge")


